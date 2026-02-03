import os
from .Page import Page
from typing import Dict, Any, Callable
from .router import Router


class LayoutML:
    def __init__(
        self,
        styles_dirname: str = "styles",
    ):

        self._router: Router = Router()
        self.error_page: Page = None
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
        self.stylesheet_files = {}
        self._css_generated = False

    def ensure_css_generated(self):
        """Генерирует CSS если еще не сгенерированы"""
        if not self._css_generated:
            self.render_css_files()
            self._css_generated = True

    def include_router(self, router: Router, prefix: str = ""):
        self._router.include_router(router=router, prefix=prefix)

    def add_element(self, element):
        self.document.body.add_element(element)

    def set_error_page(self, page: Page):
        self.error_page = page

    async def __call__(self, scope: Dict[str, Any], receive: Callable, send: Callable) -> None:

        self.ensure_css_generated()

        assert scope["type"] == "http"

        method = scope["method"]
        path = scope["path"]

        if path in self._router.routes:
            await self._serve_html(scope, receive, send, path=path)
            return

        # Статические файлы
        elif self._is_static_file(path):
            await self._serve_static_file(path, scope, receive, send)

        # 404 Not Found
        else:
            if self.error_page:
                await self._serve_html(scope, receive, send, html_content=self.error_page.get_html())
            else:
                await self._serve_404(scope, receive, send)

    def _is_static_file(self, path: str) -> bool:
        """Проверяет, является ли путь статическим файлом"""
        return any(path.endswith(ext) for ext in self._static_dirs)

    async def _serve_html(self, scope: Dict[str, Any], receive: Callable, send: Callable, html_content: str = None, path=None):
        """Отдает HTML страницу"""

        if path:
            try:
                page: Page = await self._router.dispatch(path)
                if path in self.stylesheet_files:
                    css_file_name = self.stylesheet_files[path]
                    page.head.add_stylesheet(css_file_name)

                html_content = page.get_html()
                print(f"{path}: {page}")
            except Exception as e:
                print(f"{path}: Error - {e}")

        if not html_content:
            html_content = ""

        await send(
            {
                "type": "http.response.start",
                "status": 200,
                "headers": [
                    [b"content-type", b"text/html; charset=utf-8"],
                ],
            }
        )
        await send(
            {
                "type": "http.response.body",
                "body": html_content.encode("utf-8"),
            }
        )

    async def _serve_static_file(self, path: str, scope: Dict[str, Any], receive: Callable, send: Callable):
        """Отдает статические файлы"""
        file_path = "." + path

        # Определяем content-type
        content_type = b"text/plain"
        for ext, mime_type in self._static_dirs.items():
            if path.endswith(ext):
                content_type = mime_type.encode()
                break

        if os.path.exists(file_path):
            try:
                with open(file_path, "rb") as f:
                    content = f.read()

                await send(
                    {
                        "type": "http.response.start",
                        "status": 200,
                        "headers": [
                            [b"content-type", content_type],
                        ],
                    }
                )
                await send(
                    {
                        "type": "http.response.body",
                        "body": content,
                    }
                )
            except Exception as e:
                await self._serve_404(scope, receive, send)
        else:
            await self._serve_404(scope, receive, send)

    async def _serve_404(self, scope: Dict[str, Any], receive: Callable, send: Callable):
        """Отдает 404 ошибку"""
        await send(
            {
                "type": "http.response.start",
                "status": 404,
                "headers": [
                    [b"content-type", b"text/plain; charset=utf-8"],
                ],
            }
        )
        await send(
            {
                "type": "http.response.body",
                "body": b"404 Not Found",
            }
        )

    def render_css_files(self):
        all_pages_name = []
        page_index = 1
        print(self._router.routes)
        for path in self._router.routes:
            page: Page = self._router.routes[path]["func"]()

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
            self.stylesheet_files[path] = css_file_name
            # page.head.add_stylesheet(css_file_name)
        print(self.stylesheet_files)

    # Совместимость со старым кодом
    def start(self, host: str = "localhost", port=5005):
        """Запуск в режиме совместимости (без Uvicorn)"""
        self.ensure_css_generated()
        import asyncio

        async def run_server():
            server = await asyncio.start_server(self._handle_client_compat, host, port)
            print(f"Server is ready: http://{host}:{port}")
            async with server:
                await server.serve_forever()

        asyncio.run(run_server())

    async def _handle_client_compat(self, reader, writer):
        """Совместимость со старым handle_client"""
        request = await reader.read(1024)
        request = request.decode()

        if not request:
            writer.close()
            return

        request_line = request.splitlines()[0]
        method, path, _ = request_line.split()

        # Имитируем ASGI scope
        scope = {
            "type": "http",
            "method": method,
            "path": path,
        }

        # Создаем простую реализацию receive/send для совместимости
        response_data = []

        async def send_compat(message):
            if message["type"] == "http.response.start":
                status = message["status"]
                headers = b""
                for header in message["headers"]:
                    headers += f"{header[0].decode()}: {header[1].decode()}\r\n".encode()
                response_data.append(f"HTTP/1.1 {status} OK\r\n".encode() + headers + b"\r\n")
            elif message["type"] == "http.response.body":
                response_data.append(message["body"])

        # Вызываем ASGI приложение
        await self(scope, None, send_compat)

        # Отправляем ответ
        for data in response_data:
            writer.write(data)
        await writer.drain()
        writer.close()
