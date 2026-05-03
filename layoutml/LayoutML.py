import os
import copy
import inspect
import logging

from starlette.responses import Response, HTMLResponse, PlainTextResponse, JSONResponse
from starlette.requests import Request
from starlette.exceptions import HTTPException
from functools import wraps
from typing import Callable

from layoutml.pages import get_404_page
from .Page import Page
from .router import Router

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class LayoutML:
    def __init__(
        self,
        styles_dirname: str = "styles",
    ):
        self.router: Router = Router()
        self.error_page: Page = get_404_page()
        self._pages = []
        self._static_dirs = {
            ".js": "application/javascript",
            ".css": "text/css",
            ".ico": "image/x-icon",
            ".png": "image/png",
            ".jpg": "image/jpeg",
            ".jpeg": "image/jpeg",
            ".gif": "image/gif",
            ".svg": "image/svg+xml",
        }
        self.styles_dirname = styles_dirname
        self._css_generated = False

    def render_css_files(self):
        all_pages_name = []
        page_index = 1

        for page in self._pages:
            if not page.render_css_file:
                continue
            page_styles: dict = page.get_styles()
            if not page_styles:
                continue
            page_name = page.get_object_name()
            if page_name in all_pages_name:
                page_name += str(page_index)
                page_index += 1
            css_text: str = ""
            for selector_name, css in page_styles.items():
                css_text += f"{selector_name} " + "{\n" + css + "}\n"
            css_file_name = f"{self.styles_dirname}/{page_name}.css"
            with open(css_file_name, "w") as f:
                f.write(css_text)
            page.head.add_stylesheet(css_file_name)

        if self.error_page and self.error_page.render_css_file:
            page_styles: dict = self.error_page.get_styles()
            if page_styles:
                page_name = self.error_page.get_object_name()
                if page_name in all_pages_name:
                    page_name += str(page_index)
                    page_index += 1
                css_text: str = ""
                for selector_name, css in page_styles.items():
                    css_text += f"{selector_name} " + "{\n" + css + "}\n"
                css_file_name = f"{self.styles_dirname}/{page_name}.css"
                with open(css_file_name, "w") as f:
                    f.write(css_text)
                self.error_page.head.add_stylesheet(css_file_name)

    def ensure_css_generated(self):
        if not self._css_generated:
            self.render_css_files()
            self._css_generated = True

    def include_page(self, Page: Page):
        self._pages.append(Page)

    def include_router(self, router: Router, prefix: str = ""):
        self.router.include_router(router=router, prefix=prefix)

    def route(self, endpoint: str):
        def decorator(func: Callable):
            @wraps(func)
            async def wrapper(**kwargs):
                if inspect.iscoroutinefunction(func):
                    return await func(**kwargs)
                else:
                    return func(**kwargs)

            return self.router.route(endpoint)(wrapper)

        return decorator

    def print_routes(self):
        self.router.print_routes()

    def set_error_page(self, page: Page):
        self.error_page = page

    def _is_static_file(self, path: str) -> bool:
        return any(path.endswith(ext) for ext in self._static_dirs)

    async def _serve_html(
        self,
        request: Request,
        html_content: str = None,
    ):
        if html_content:
            response = HTMLResponse(
                content=html_content,
                status_code=200,
                headers={"content-type": "text/html; charset=utf-8"},
            )
            return response

        else:
            response = HTMLResponse(
                status_code=200,
                headers={"content-type": "text/html; charset=utf-8"},
            )
            if request.url.path:
                answer: Page = await self.router.dispatch(request, response)
                if isinstance(answer, (Response, HTMLResponse, PlainTextResponse, JSONResponse)):
                    return answer
                elif isinstance(answer, Page):
                    html_content = answer.get_html()
                elif isinstance(page, str):
                    html_content = page
                else:
                    response.status_code = 404
                    html_content = self.error_page.get_html()
            response.body = response.render(html_content)
            response.headers["content-length"] = str(len(response.body))

            return response

    async def _serve_static_file(self, request: Request):
        file_path = "." + request.url.path

        # Безопасность: предотвращаем выход из корневой директории
        if ".." in file_path or not os.path.abspath(file_path).startswith(os.getcwd()):
            return Response(content=b"", status_code=403, headers={"content-type": "text/plain"})

        # Определяем content-type
        content_type = "text/plain"
        for ext, mime_type in self._static_dirs.items():
            if request.url.path.endswith(ext):
                content_type = mime_type
                break

        if not os.path.exists(file_path):
            return Response(content=b"", status_code=404, headers={"content-type": "text/plain"})

        if not os.access(file_path, os.R_OK):
            return Response(content=b"", status_code=403, headers={"content-type": "text/plain"})

        try:
            with open(file_path, "rb") as f:
                content = f.read()
            return Response(content=content, status_code=200, headers={"content-type": content_type})
        except Exception:
            return Response(content=b"", status_code=500, headers={"content-type": "text/plain"})

    async def _serve_404(self, request: Request):
        return Response(content="404 Not Found", status_code=404, headers={"content-type": "text/plain; charset=utf-8"})

    def _parse_http(self, request_str):
        lines = request_str.split("\r\n")
        method, path, version = lines[0].split(" ")

        headers = {}
        body = ""
        is_headers = True

        for line in lines[1:]:
            if is_headers and line == "":
                is_headers = False
                continue
            if is_headers:
                key, value = line.split(": ", 1)
                headers[key] = value
            else:
                body += line

        return method, path, version, headers, body

    async def __call__(self, request: Request) -> None:
        self.ensure_css_generated()
        if request.url.path in self.router.routes:
            try:
                response = await self._serve_html(request)
                return response
            except HTTPException as e:
                return Response(
                    status_code=e.status_code,
                    content=str({"detail": e.detail}),
                    headers={"Content-Type": "application/json"},
                )
            except Exception as e:
                return Response(
                    status_code=500,
                    content=str({"detail": e}),
                    headers={"Content-Type": "application/json"},
                )
        elif self._is_static_file(request.url.path):
            return await self._serve_static_file(request)
        else:
            if self.error_page:
                response = await self._serve_html(request, html_content=self.error_page.get_html())
                response.status_code = 404
                return response
            else:
                return await self._serve_404(request)

    async def _handle_client_compat(self, reader, writer):
        request_bytes = await reader.read(4096)
        request_str = request_bytes.decode("utf-8", errors="ignore")

        method, path, version, headers_dict, body = self._parse_http(request_str)
        query_string = b""
        if "?" in path:
            path_part, query_string_part = path.split("?", 1)
            query_string = query_string_part.encode()
            path = path_part
        else:
            path_part = path

        scope = {
            "type": "http",
            "method": method,
            "path": path_part,
            "headers": [(k.lower().encode(), v.encode()) for k, v in headers_dict.items()],
            "query_string": query_string,
            "client": writer.get_extra_info("peername"),
            "server": writer.get_extra_info("sockname"),
            "scheme": "http",
            "http_version": version,
        }

        async def receive():
            return {"type": "http.request", "body": body.encode() if body else b"", "more_body": False}

        request = Request(scope=scope)
        response: Response = await self(request)

        if not isinstance(response, Response):
            response = Response(content=response)
        if not self._is_static_file(request.url.path):
            logger.info(f"{method} {path_part} → {response.status_code}")
        if response is not None:
            status_line = f"HTTP/1.1 {response.status_code} OK\r\n".encode()
            headers = b""
            for key, value in response.headers.items():
                headers += f"{key}: {value}\r\n".encode()
            writer.write(status_line + headers + b"\r\n")
            body = response.body if hasattr(response, "body") else b""
            if body:
                writer.write(body if isinstance(body, bytes) else body.encode())
            await writer.drain()

            # except Exception as e:
            #     logger.error(f"{method} {path_part} → ERROR: {e} ")
            # finally:
            writer.close()

    def start(self, host: str = "localhost", port=3700):
        self.ensure_css_generated()
        import asyncio

        async def run_server():
            server = await asyncio.start_server(self._handle_client_compat, host, port)
            logger.info(f"Server is ready: http://{host}:{port}")
            async with server:
                await server.serve_forever()

        asyncio.run(run_server())
