# LayoutML

`LayoutML` is the core class of the framework that combines routing, style generation, and HTTP request handling. It provides an ASGI-compatible interface for building web applications with automatic CSS file generation based on styles defined in pages.

---

## Import

```python
from layoutml import LayoutML
```

## Purpose

- **Routing:** Handles HTTP requests and calls the appropriate handlers
- **CSS Generation:** Automatically creates CSS files from styles defined in components
- **Static Files:** Serves static resources (images, CSS, JS)
- **ASGI Compatibility:** Supports the asynchronous ASGI interface for integration with servers such as Uvicorn and Hypercorn

## Constructor

### **init**(self, styles_dirname: str = "styles")

Parameters:

- styles_dirname (str): Directory for storing generated CSS files. Defaults to `"styles"`

Example:

```python
app = LayoutML(styles_dirname="assets/css")
```

### Attributes

| Attribute       | Type   | Description                         |
| --------------- | ------ | ----------------------------------- |
| router          | Router | Router object for handling requests |
| error_page      | Page   | Page displayed for 404 errors       |
| \_pages         | list   | List of registered pages            |
| \_static_dirs   | dict   | MIME types for static files         |
| styles_dirname  | str    | Directory for CSS files             |
| \_css_generated | bool   | CSS file generation flag            |

## Methods

### include_page(page: Page)

Registers a page for pre-generating CSS and JavaScript.

Parameters:

- page (Page): Page instance to register

Important: This method is required to process the page and generate its CSS files before handling requests.

Example:

```python
from layoutml import Page

main_page = Page(title="Home")
main_page.body.add_content("<h1>Welcome!</h1>")

app.include_page(main_page)  # Registering the page
```

### include_router(router: Router, prefix: str = "")

Includes a sub-router in the main application.

Parameters:

- router (Router): Router instance to include
- prefix (str): Prefix for all sub-router routes

Example:

```python
api_router = Router(prefix="/api")
app.include_router(api_router, prefix="/v1")
```

### route(endpoint: str)

Decorator for registering a route handler.

Parameters:

- endpoint (str): Route path

Returns:

- A decorator for the handler function

Example:

```python
@app.route("/user")
async def get_user(request: Request, response: Response, user_id: int):
    page = main_page.copy()  # Important: always copy the page!
    page.body.add_content(f"<h1>User {user_id}</h1>")
    return page
```

### print_routes()

Prints the list of all registered routes to the console.

```python
app.print_routes()

# Router: /
# --------------------------------------------------
# / -> home
# /user -> get_user
```

### set_error_page(page: Page)

Sets a custom 404 error page.

Parameters:

- page (Page): Error page instance

Example:

```python
custom_404 = Page(title="Page Not Found")
custom_404.body.add_content("<h1>404 - Not Found</h1>")
app.set_error_page(custom_404)
```

### start(host: str = "localhost", port: int = 3700)

Starts a compatible HTTP server.

Parameters:

- host (str): Host to listen on
- port (int): Port to listen on

Example:

```python
if __name__ == "__main__":
    app.start(host="0.0.0.0", port=8000)
```

## Best Practices

### 1. Always Copy Pages

```python
# Always copy the page inside handlers
@app.route("/profile")
def profile_handler(request: Request, response: Response):
    page = base_page.copy()  # ✅
    return page
```

### 2. Register All Pages

```python
# Register all pages used in the application
app.include_page(home_page)
app.include_page(about_page)
app.include_page(contact_page)
```

### 3. Use a Base Page Class to Set a Shared Icon for All Pages

```python
class AppPage(Page):
    def __init__(self, title="App", **kwargs):
        super().__init__(title=title, **kwargs)
        self.head.set_icon("/static/favicon.ico")
        self.head.add_stylesheet("/static/app.css")
```

### 4. Handle Errors Properly

```python
@app.route("/protected")
async def protected(request: Request, response: Response):
    if not request.headers.get("Authorization"):
        raise HTTPException(status_code=401, detail="Unauthorized")
    return page.copy()
```
