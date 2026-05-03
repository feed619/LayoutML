import re
from typing import Dict, Callable, Any, Optional
import inspect
from starlette.requests import Request
from starlette.responses import JSONResponse, Response

from layoutml import Page


def get_parameters(func) -> dict:
    sig: inspect.Signature = inspect.signature(func)
    parameters = {}
    for param_name, param in sig.parameters.items():
        annotation = param.annotation
        if annotation is Page:
            continue
        is_required = param.default == inspect.Parameter.empty

        param_info = {
            "name": param_name,
            "is_required": is_required,
            "default": param.default if param.default != inspect.Parameter.empty else None,
            "annotation": annotation if annotation != inspect.Parameter.empty else None,
            "type_name": annotation.__name__ if hasattr(annotation, "__name__") else str(annotation),
        }
        parameters[param_name] = param_info
    return parameters


class Router:
    def __init__(self, prefix: str = ""):
        self.routes: Dict[str, Dict] = {}
        self.prefix = prefix.rstrip("/")
        self._child_routers: Dict[str, "Router"] = {}

    def route(self, path: str):
        def decorator(func: Callable):
            full_path = f"{self.prefix}{path}"
            original_path = f"{self.prefix}{path}"
            parameters = get_parameters(func)
            self.routes[full_path] = {
                "func": func,
                "original_path": original_path,
                "pattern": None,
                "has_params": False if parameters else True,
                "parameters": parameters,
                "is_async": inspect.iscoroutinefunction(func),
            }
            return func

        return decorator

    def include_router(self, router: "Router", prefix: str = ""):
        """Включает другой роутер в текущий с опциональным префиксом"""
        if not isinstance(router, Router):
            router_type_name = type(router).__name__
            raise TypeError(
                f"router должен быть экземпляром класса Router, "
                f"получен: {router_type_name}. "
                f"Проверьте, что вы передаете именно объект Router, а не что-то другое."
            )
        if router is self:
            raise ValueError("Нельзя включить роутер сам в себя. " "Это приведет к бесконечной рекурсии.")
        prefix = prefix.rstrip("/")
        full_prefix = f"{self.prefix}{prefix}"
        self._child_routers[full_prefix] = router
        for route_path, route_info in router.routes.items():
            child_route_path = route_path.replace(router.prefix, "", 1)
            full_route_path = f"{full_prefix}{child_route_path}"
            self.routes[full_route_path] = {
                "func": route_info["func"],
                "original_path": full_route_path,
                "pattern": route_info["pattern"],
                "parameters": route_info["parameters"],
                "has_params": route_info["has_params"],
                "is_async": route_info["is_async"],
            }

        for child_prefix, child_router in router._child_routers.items():
            nested_child_prefix = child_prefix.replace(router.prefix, "", 1)
            new_prefix = f"{full_prefix}{nested_child_prefix}"
            self.include_router(child_router, new_prefix)

    def _match_route(self, path: str) -> Optional[Dict]:
        if path in self.routes:
            return self.routes[path]
        for route_path, route_info in self.routes.items():
            if route_info["has_params"] and route_info["pattern"]:
                match = route_info["pattern"].match(path)
                if match:
                    return {**route_info, "params": match.groupdict()}
        return None

    async def dispatch(self, request: Request, response: Response) -> Any:
        query_params = {}
        for param_name in request.query_params:
            query_params[param_name] = request.query_params[param_name]
        route_info = self._match_route(request.url.path)
        if not route_info:
            raise ValueError(f"Route not found: {request.url.path}")

        func = route_info["func"]
        for parameter_name in query_params:
            if parameter_name not in route_info["parameters"]:
                return JSONResponse(status_code=400, content={"error": f"Unexpected parameter: {parameter_name}"})

        for parameter_name, parameter_data in route_info["parameters"].items():
            if parameter_data["annotation"] is Request:
                query_params[parameter_name] = request
            elif parameter_data["annotation"] is Response:
                query_params[parameter_name] = response
            elif parameter_data["is_required"]:
                if parameter_name not in query_params:
                    return JSONResponse(
                        status_code=400,
                        content={"error": f"Missing required parameter: {parameter_name}"},
                    )
        if route_info["is_async"]:
            return await func(**query_params)
        else:
            return func(**query_params)

    def get_all_routes(self) -> Dict[str, Any]:
        return self.routes.copy()

    def print_routes(self):
        print(f"\nRouter: {self.prefix if self.prefix else '/'}")
        print("-" * 50)
        for path, info in self.routes.items():
            handler_name = info["func"].__name__
            print(f"{path} -> {handler_name}")

        if self._child_routers:
            print("\nIncluded routers:")
            for prefix, router in self._child_routers.items():
                print(f"  {prefix} -> {router.__class__.__name__}")
