import re
from typing import Dict, Callable, Any, Optional, Union
import inspect


class Router:
    def __init__(self, prefix: str = ""):
        self.routes: Dict[str, Dict] = {}
        self.prefix = prefix.rstrip("/")
        self._child_routers: Dict[str, "Router"] = {}  # Для хранения дочерних роутеров

    def route(self, path: str):
        def decorator(func: Callable):
            full_path = f"{self.prefix}{path}"
            original_path = f"{self.prefix}{path}"

            # Обрабатываем параметры пути /user/<id>
            if "<" in full_path and ">" in full_path:
                # Создаем regex паттерн для извлечения параметров
                pattern = re.sub(r"<(\w+)>", r"(?P<\1>[^/]+)", full_path)
                pattern = f"^{pattern}$"  # Добавляем начало и конец строки
                compiled_pattern = re.compile(pattern)

                self.routes[full_path] = {
                    "func": func,
                    "original_path": original_path,
                    "pattern": compiled_pattern,
                    "has_params": True,
                    "is_async": inspect.iscoroutinefunction(func),
                }
            else:
                self.routes[full_path] = {
                    "func": func,
                    "original_path": original_path,
                    "pattern": None,
                    "has_params": False,
                    "is_async": inspect.iscoroutinefunction(func),
                }
            return func

        return decorator

    def add(self, endpoint: str):
        return self.route(endpoint)

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

        # Копируем все маршруты из дочернего роутера с учетом префикса
        for route_path, route_info in router.routes.items():
            # Удаляем префикс дочернего роутера из пути маршрута
            # т.к. он будет добавлен через full_prefix
            child_route_path = route_path.replace(router.prefix, "", 1)

            # Формируем полный путь
            full_route_path = f"{full_prefix}{child_route_path}"

            # Обрабатываем параметры пути
            if route_info["has_params"]:
                # Обновляем паттерн для нового префикса
                pattern = re.sub(r"<(\w+)>", r"(?P<\1>[^/]+)", child_route_path)
                pattern = f"^{full_prefix}{pattern}$"
                compiled_pattern = re.compile(pattern)

                self.routes[full_route_path] = {
                    "func": route_info["func"],
                    "original_path": full_route_path,
                    "pattern": compiled_pattern,
                    "has_params": True,
                    "is_async": route_info["is_async"],
                }
            else:
                self.routes[full_route_path] = {
                    "func": route_info["func"],
                    "original_path": full_route_path,
                    "pattern": None,
                    "has_params": False,
                    "is_async": route_info["is_async"],
                }

        # Рекурсивно включаем дочерние роутеры из включаемого роутера
        for child_prefix, child_router in router._child_routers.items():
            # Вычисляем новый префикс для вложенного роутера
            nested_child_prefix = child_prefix.replace(router.prefix, "", 1)
            new_prefix = f"{full_prefix}{nested_child_prefix}"
            self.include_router(child_router, new_prefix)

    def _match_route(self, path: str) -> Optional[Dict]:
        """Находит подходящий маршрут для пути"""
        # Прямое совпадение
        if path in self.routes:
            return self.routes[path]

        # Проверяем маршруты с параметрами
        for route_path, route_info in self.routes.items():
            if route_info["has_params"] and route_info["pattern"]:
                match = route_info["pattern"].match(path)
                if match:
                    return {**route_info, "params": match.groupdict()}

        return None

    async def dispatch(self, path: str, *args, **kwargs) -> Any:
        """Выполняет обработчик для указанного пути"""
        route_info = self._match_route(path)

        if not route_info:
            raise ValueError(f"Route not found: {path}")

        func = route_info["func"]
        params = route_info.get("params", {})

        # Объединяем переданные аргументы с параметрами из пути
        all_kwargs = {**params, **kwargs}

        if route_info["is_async"]:
            # Для асинхронных функций
            return await func(*args, **all_kwargs)
        else:
            # Для синхронных функций
            return func(*args, **all_kwargs)

    def get_all_routes(self) -> Dict[str, Any]:
        """Возвращает все маршруты включая дочерние"""
        return self.routes.copy()

    def print_routes(self):
        """Выводит все маршруты в читаемом формате"""
        print(f"\nRouter: {self.prefix if self.prefix else '/'}")
        print("-" * 50)
        for path, info in self.routes.items():
            handler_name = info["func"].__name__
            async_prefix = "[ASYNC] " if info["is_async"] else "[SYNC]  "
            print(f"{async_prefix}{path} -> {handler_name}")

        if self._child_routers:
            print("\nIncluded routers:")
            for prefix, router in self._child_routers.items():
                print(f"  {prefix} -> {router.__class__.__name__}")
