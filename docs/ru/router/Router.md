# Router

`Router` - это класс для управления маршрутизацией HTTP запросов в приложениях LayoutML. Он предоставляет механизм для регистрации обработчиков маршрутов, поддержки вложенных роутеров и автоматического извлечения параметров из запросов.

## Основные возможности

- Декларативная маршрутизация через декоратор @router.route()
- Автоматическое извлечение параметров из query string
- Поддержка вложенных роутеров с префиксами
- Интеграция с Starlette (Request, Response объекты)
- Автоматическое определение асинхронных обработчиков

## Импорт

```python
from layoutml.router import Router
```

## Конструктор

### **init**(self, prefix: str = "")

Параметры:

- prefix (str): Префикс для всех маршрутов этого роутера. По умолчанию пустая строка

Пример:

```python
# Роутер без префикса
main_router = Router()
# Роутер с префиксом /api
api_router = Router(prefix="/api")
```

### Атрибуты

| Атрибут         | Тип               | Описание                             |
| --------------- | ----------------- | ------------------------------------ |
| routes          | Dict[str, Dict]   | Словарь зарегистрированных маршрутов |
| prefix          | str               | Префикс всех маршрутов роутера       |
| \_child_routers | Dict[str, Router] | Вложенные роутеры                    |

## Методы

### route(path: str) -> Callable

Декоратор для регистрации обработчика маршрута.

Параметры:

- path (str): Путь маршрута

Возвращает:

- Декоратор для функции-обработчика

Пример:

```python
router = Router()
@router.route("/")
def home():
    return "Hello, World!"

@router.route("/user")
async def get_user(request: Request, user_id: int):
    return {"id": user_id}
```

### include_router(router: Router, prefix: str = "")

Включает другой роутер в текущий с опциональным префиксом.

Параметры:

- router (Router): Роутер для включения
- prefix (str): Дополнительный префикс для маршрутов

Особенности:

- Поддерживает рекурсивное включение вложенных роутеров
- Проверяет на циклические зависимости

Пример:

```python
main_router = Router()
api_router = Router(prefix="/api")
v1_router = Router(prefix="/v1")

@v1_router.route("/users")
def get_users(): ...

api_router.include_router(v1_router)
main_router.include_router(api_router)

# Итоговый путь: /api/v1/users
```

### get_all_routes() -> Dict[str, Any]

Возвращает копию словаря всех зарегистрированных маршрутов.

Пример:

```python
routes = router.get_all_routes()
for path, info in routes.items():
    print(f"{path} -> {info['func'].**name**}")
```

### print_routes()

Выводит все маршруты в читаемом формате в консоль.

Пример вывода:

```text

## Router: /api

/api/users -> get_users
/api/posts -> get_posts
/api/user/<id> -> get_user
```

## Примеры использования

### Пример 1: Простая маршрутизация

```python
from layoutml import Router

router = Router()

@router.route("/")
def home():
    return "Welcome to the homepage"

@router.route("/about")
def about():
    return "About us"

@router.route("/contact")
def contact():
    return "Contact page"
```

### Пример 2: Параметры запроса

```python
@router.route("/search")
def search(query: str, limit: int = 10, page: int = 1):
    # GET /search?query=python&limit=5&page=2
    # query="python", limit=5, page=2
    return {"results": [], "query": query, "limit": limit, "page": page}
```

### Пример 3: Использование Request и Response

```python
from layoutml import Request, Response

@router.route("/profile")
async def profile(request: Request, response: Response, user_id: int):
    # Чтение cookies
    session = request.cookies.get("session_id")

    # Установка cookie
    response.set_cookie("last_visited", "/profile", max_age=3600)

    return {"user_id": user_id, "session": session}
```

### Пример 4: Вложенные роутеры

```python
# Создание дочерних роутеров
api = Router(prefix="/api")
admin = Router(prefix="/admin")
users = Router(prefix="/users")

# Регистрация маршрутов в дочерних роутерах
@api.route("/status")
def api_status():
    return {"status": "ok"}

@users.route("/")
def list_users():
    return [{"id": 1, "name": "John"}]

# Включение роутеров
admin.include_router(users, prefix="/manage")
api.include_router(admin)

# Итоговые пути:
# /api/status
# /api/admin/manage/users
# /api/admin/manage/users/123
```

### Пример 5: Асинхронные обработчики

```python
import asyncio

@router.route("/async-data")
async def get_async_data(delay: int = 1):
    await asyncio.sleep(delay)
    return {"data": "Loaded after delay"}

@router.route("/db-query")
async def db_query(user_id: int):
    # Асинхронный запрос к базе данных
    result = await database.fetch_one(
        "SELECT * FROM users WHERE id = :id",
        {"id": user_id}
    )
    return result
```

### Пример 6: Опциональные параметры

```python

@router.route("/filter")
def filter_items(
    category: str = "all",
    sort: str = "asc",
    limit: Optional[int] = None
):
    # GET /filter?category=books
    # category="books", sort="asc", limit=None

    # GET /filter?category=electronics&limit=20
    # category="electronics", sort="asc", limit=20

    return {"category": category, "sort": sort, "limit": limit}
```

## Особенности работы

### Автоматическое извлечение параметров

Роутер автоматически извлекает параметры из query string и передает их в обработчик:

```python
@router.route("/api/search")
def search(q: str, page: int = 1, per_page: int = 10):
    # GET /api/search?q=python&page=2
    # q="python", page=2, per_page=10 (значение по умолчанию)
    return {"query": q, "page": page, "per_page": per_page}
```

### Валидация параметров

Роутер проверяет, что все обязательные параметры присутствуют в запросе:

```python

@router.route("/required")
def required_params(name: str, age: int):
    # GET /required?name=John -> Ошибка (отсутствует age)
    # GET /required?name=John&age=25 -> Успешно
    return {"name": name, "age": age}
```

### Параметры Request и Response

Объекты Request и Response Starlette автоматически внедряются при наличии соответствующих аннотаций:

```python

@router.route("/handle")
def handler(request: Request, response: Response, param: str):
    # request и response будут автоматически переданы
    # param извлекается из query string
    response.headers["X-Custom"] = "value"
    return {"param": param}
```
