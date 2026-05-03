# Router

`Router` is a class for managing HTTP request routing in LayoutML applications. It provides a mechanism for registering route handlers, supporting nested routers, and automatically extracting parameters from requests.

## Key Features

- Declarative routing via the `@router.route()` decorator
- Automatic extraction of parameters from the query string
- Support for nested routers with prefixes
- Integration with Starlette (`Request`, `Response` objects)
- Automatic detection of asynchronous handlers

## Import

```python
from layoutml.router import Router
```

## Constructor

### **init**(self, prefix: str = "")

Parameters:

- prefix (str): Prefix for all routes in this router. Defaults to an empty string

Example:

```python
# Router without a prefix
main_router = Router()

# Router with /api prefix
api_router = Router(prefix="/api")
```

### Attributes

| Attribute       | Type              | Description                     |
| --------------- | ----------------- | ------------------------------- |
| routes          | Dict[str, Dict]   | Dictionary of registered routes |
| prefix          | str               | Prefix for all router routes    |
| \_child_routers | Dict[str, Router] | Nested routers                  |

## Methods

### route(path: str) -> Callable

Decorator for registering a route handler.

Parameters:

- path (str): Route path

Returns:

- A decorator for the handler function

Example:

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

Includes another router into the current one with an optional prefix.

Parameters:

- router (Router): Router to include
- prefix (str): Additional route prefix

Features:

- Supports recursive inclusion of nested routers
- Checks for cyclic dependencies

Example:

```python
main_router = Router()
api_router = Router(prefix="/api")
v1_router = Router(prefix="/v1")

@v1_router.route("/users")
def get_users(): ...

api_router.include_router(v1_router)
main_router.include_router(api_router)

# Final route: /api/v1/users
```

### get_all_routes() -> Dict[str, Any]

Returns a copy of the dictionary containing all registered routes.

Example:

```python
routes = router.get_all_routes()

for path, info in routes.items():
    print(f"{path} -> {info['func'].__name__}")
```

### print_routes()

Prints all routes in a readable format to the console.

Example output:

```text
## Router: /api

/api/users -> get_users
/api/posts -> get_posts
/api/user/<id> -> get_user
```

## Usage Examples

### Example 1: Basic Routing

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

### Example 2: Query Parameters

```python
@router.route("/search")
def search(query: str, limit: int = 10, page: int = 1):
    # GET /search?query=python&limit=5&page=2
    # query="python", limit=5, page=2
    return {"results": [], "query": query, "limit": limit, "page": page}
```

### Example 3: Using Request and Response

```python
from layoutml import Request, Response

@router.route("/profile")
async def profile(request: Request, response: Response, user_id: int):
    # Reading cookies
    session = request.cookies.get("session_id")

    # Setting a cookie
    response.set_cookie("last_visited", "/profile", max_age=3600)

    return {"user_id": user_id, "session": session}
```

### Example 4: Nested Routers

```python
# Creating child routers
api = Router(prefix="/api")
admin = Router(prefix="/admin")
users = Router(prefix="/users")

# Registering routes in child routers
@api.route("/status")
def api_status():
    return {"status": "ok"}

@users.route("/")
def list_users():
    return [{"id": 1, "name": "John"}]

# Including routers
admin.include_router(users, prefix="/manage")
api.include_router(admin)

# Final routes:
# /api/status
# /api/admin/manage/users
# /api/admin/manage/users/123
```

### Example 5: Asynchronous Handlers

```python
import asyncio

@router.route("/async-data")
async def get_async_data(delay: int = 1):
    await asyncio.sleep(delay)
    return {"data": "Loaded after delay"}

@router.route("/db-query")
async def db_query(user_id: int):
    # Asynchronous database query
    result = await database.fetch_one(
        "SELECT * FROM users WHERE id = :id",
        {"id": user_id}
    )
    return result
```

### Example 6: Optional Parameters

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

## How It Works

### Automatic Parameter Extraction

The router automatically extracts parameters from the query string and passes them to the handler:

```python
@router.route("/api/search")
def search(q: str, page: int = 1, per_page: int = 10):
    # GET /api/search?q=python&page=2
    # q="python", page=2, per_page=10 (default value)
    return {"query": q, "page": page, "per_page": per_page}
```

### Parameter Validation

The router checks that all required parameters are present in the request:

```python
@router.route("/required")
def required_params(name: str, age: int):
    # GET /required?name=John -> Error (missing age)
    # GET /required?name=John&age=25 -> Success
    return {"name": name, "age": age}
```

### Request and Response Parameters

Starlette `Request` and `Response` objects are automatically injected when corresponding annotations are present:

```python
@router.route("/handle")
def handler(request: Request, response: Response, param: str):
    # request and response are automatically provided
    # param is extracted from the query string
    response.headers["X-Custom"] = "value"
    return {"param": param}
```
