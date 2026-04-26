# Router

`Router` is a class for URL routing in web applications. It provides a system for declarative route definition, path parameter support, nested routers, and request dispatching for both synchronous and asynchronous handlers.

---

## Class Attributes

| Attribute       | Type                | Description                                 |
| --------------- | ------------------- | ------------------------------------------- |
| routes          | Dict[str, Dict]     | Dictionary of all registered routes         |
| prefix          | str                 | Prefix applied to all routes in this router |
| \_child_routers | Dict[str, "Router"] | Dictionary of child routers                 |

---

## Constructor

### **init**(prefix: str = "")

Creates a new router with an optional prefix for all routes.

Parameters:

- prefix (str): Prefix for all routes in this router. Default is an empty string.

Examples:

```python
# Router without prefix
router = Router()

# Router with /api prefix
api_router = Router(prefix="/api")

# Router with /admin prefix
admin_router = Router(prefix="/admin")
```

---

## Core Methods

### route(path: str) decorator

Decorator for registering a function as a route handler.

Parameters:

- path (str): Route path (may contain parameters in `<name>` format)

Examples:

```python
router = Router()

# Simple route
@router.route("/")
def home():
    return "Home page"

# Route with parameter
@router.route("/user/<user_id>")
def get_user(user_id: str):
    return f"User {user_id}"

# Async route
@router.route("/data")
async def get_data():
    data = await fetch_from_db()
    return data
```

---

### add(endpoint: str) -> Callable

Alternative method for registering routes (alias for `route`).

```python
router = Router()

@router.add("/about")
def about():
    return "About us"
```

---

### include_router(router: "Router", prefix: str = "")

Includes another router into the current one with an optional prefix.

Parameters:

- router (Router): Router to include
- prefix (str): Additional prefix for included router routes

Features:

- Supports recursive inclusion (routers inside routers)
- Automatically handles prefixes
- Detects circular dependencies

Examples:

```python
# Main router
main_router = Router()

# API router
api_router = Router(prefix="/api")

@api_router.route("/users")
def get_users():
    return ["user1", "user2"]

# Include API router
main_router.include_router(api_router)
# Route available at /api/users

# Include with additional prefix
main_router.include_router(api_router, prefix="/v1")
# Route available at /v1/api/users
```

---

### dispatch(path: str, \*args, \*\*kwargs) -> Any

Executes a handler for the given path.

Parameters:

- path (str): Path to dispatch
- \*args: Positional arguments for handler
- \*\*kwargs: Keyword arguments for handler

Returns:

- Result of handler execution

Features:

- Automatically detects sync/async handlers
- Extracts path parameters
- Merges path parameters with provided arguments

Examples:

```python
router = Router()

@router.route("/hello/<name>")
def greet(name: str, greeting: str = "Hello"):
    return f"{greeting}, {name}!"

# Sync call
result = router.dispatch("/hello/John")
print(result)  # "Hello, John!"

# With extra parameters
result = router.dispatch("/hello/Maria", greeting="Hi")
print(result)  # "Hi, Maria!"
```

Async example:

```python
@router.route("/async")
async def async_handler():
    await asyncio.sleep(1)
    return "Done"

# Inside async context
result = await router.dispatch("/async")
```

---

### get_all_routes() -> Dict[str, Any]

Returns a dictionary of all registered routes.

```python
router = Router()
router.route("/home")(lambda: "Home")
router.route("/about")(lambda: "About")

routes = router.get_all_routes()

# {
#     '/home': {...},
#     '/about': {...}
# }
```

---

### print_routes()

Prints all routes in a readable format to the console.

```python id="router8"
router = Router()

router.route("/")(lambda: "Home")
router.route("/user/<id>")(lambda id: f"User {id}")

router.print_routes()

# Output:
# Router: /
# --------------------------------------------------
# [SYNC]  / -> <lambda>
# [SYNC]  /user/<id> -> <lambda>
```
