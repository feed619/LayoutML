# LayoutML

`LayoutML` is the core framework class that combines routing, style generation, and HTTP request handling. The class provides an ASGI-compatible interface for building web applications with automatic CSS file generation based on styles defined in pages.

---

## Import

```python
from layoutml import LayoutML
```

## Purpose

- Routing: Handles HTTP requests and calls corresponding handlers
- CSS generation: Automatically creates CSS files from styles defined in components
- Static files: Serves static resources (images, CSS, JS)
- ASGI compatibility: Supports asynchronous ASGI interface for integration with servers (Uvicorn, Hypercorn)

## Constructor

### **init**(styles_dirname: str = "styles")

Creates a new instance of the LayoutML application.

Parameters:

- styles_dirname (str): Name of the directory for storing generated CSS files. Default is "styles"

Automatically initialized attributes:

- \_router: Router instance for routing
- error_page: page displayed for 404 errors
- \_static_dirs: dictionary of file extensions and MIME types for static files
- styles_dirname: CSS directory name
- stylesheet_files: dictionary mapping routes to CSS files
- \_css_generated: CSS generation flag

### Examples:

```python
# Create application with default settings
app = LayoutML()

# Create application with custom styles directory
app = LayoutML(styles_dirname="assets/css")
```

## Class Attributes

| Attribute        | Type   | Description                              |
| ---------------- | ------ | ---------------------------------------- |
| \_router         | Router | Internal router for request handling     |
| error_page       | Page   | Page displayed for 404 errors            |
| \_static_dirs    | dict   | Mapping of file extensions to MIME types |
| styles_dirname   | str    | Directory for CSS files                  |
| stylesheet_files | dict   | Mapping of routes to CSS files           |
| \_css_generated  | bool   | CSS generation flag                      |

## Core Methods

### ensure_css_generated()

Generates CSS files if they have not been created yet.

```python
app = LayoutML()
app.ensure_css_generated()  # Creates CSS files in styles/ directory
```

### route(endpoint)

Registers a route handler.

Parameters:

- endpoint: name of the endpoint

```python
from layoutml import LayoutML, Page, Body, Paragraph

# Create application
app = LayoutML()

@app.route("/")
def home():
    page = Page(title="Home Page")
    page.body.get_html(content="<h1>Welcome!</h1>")
    return page
```

### print_routes()

Prints all registered routes in a readable format.

```python
app.print_routes()
```

### include_router(router: Router, prefix: str = "")

Includes a child router into the main application with an optional prefix.

Parameters:

- router (Router): Router to include
- prefix (str): Prefix for all router routes

```python
from layoutml import Router

# Create API router
api_router = Router(prefix="/api")

@api_router.route("/users")
def get_users():
    return Page(title="Users")

# Include into app
app = LayoutML()
app.include_router(api_router)
```

### set_error_page(page: Page)

Sets the page displayed for 404 errors.

Parameters:

- page (Page): Error page to display

```python
from layoutml import Page

error_page = Page(title="404 - Page Not Found")
error_page.body.get_html(content="<h1>404</h1><p>Page not found</p>")

app = LayoutML()
app.set_error_page(error_page)
```

### render_css_files()

Generates CSS files for all registered routes.

Features:

- Collects styles from all pages via get_styles()
- Creates separate CSS files for each page
- Stores route-to-CSS mapping in stylesheet_files

```python
app.render_css_files()  # Creates CSS files in styles_dirname
```

### start(host: str = "localhost", port: int = 5005)

Starts the built-in ASGI server in compatibility mode.

Parameters:

- host (str): Server host
- port (int): Server port

Note: This method is intended for simple startup and uses an asyncio server.

```python
app.start(host="0.0.0.0", port=8000)
```

### ASGI method **call**(scope, receive, send)

Main ASGI entry point that makes the application compatible with ASGI servers (Uvicorn, Hypercorn).

Parameters:

- scope (Dict[str, Any]): ASGI request scope
- receive (Callable): Function to receive request body
- send (Callable): Function to send response

```python
# Run with Uvicorn
import uvicorn

app = LayoutML()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

## Internal Methods

### \_is_static_file(path: str) -> bool

Checks whether the path is a static file.

### \_serve_html(scope, receive, send, html_content=None, path=None)

Serves an HTML page to the client.

### \_serve_static_file(path, scope, receive, send)

Serves static files (CSS, images, JS).

### \_serve_404(scope, receive, send)

Serves a 404 error page.

## Usage Examples

### Simple Application

```python
from layoutml import LayoutML, Page

app = LayoutML()

# Route registration
@app.route("/")
def home():
    page = Page(title="Home Page")
    page.body.get_html(content="<h1>Welcome!</h1>")
    return page

# Run application
app.start(host="localhost", port=5005)
```

### Multi-page Application

```python
from layoutml import LayoutML, Page

app = LayoutML()

# Home page
@app.route("/")
def home():
    page = Page(title="Home")
    page.body.get_html(content="""
    <h1>Home Page</h1>
    <nav>
        <a href="/about">About</a> |
        <a href="/contact">Contact</a>
    </nav>
    """)
    return page

# About page
@app.route("/about")
def about():
    page = Page(title="About")
    page.body.get_html(content="<h1>About Us</h1><p>We are the best!</p>")
    return page

# Contact page
@app.route("/contact")
def contact():
    page = Page(title="Contact")
    page.body.get_html(content="<h1>Contact</h1><p>Email: info@example.com</p>")
    return page

# Error page
error_page = Page(title="404")
error_page.body.get_html(content="<h1>404</h1><p>Page not found</p>")
app.set_error_page(error_page)

# Run
app.start()
```

### Styled Application

```python
from layoutml import LayoutML, Page, Header, Paragraph

app = LayoutML()

@app.route("/styled")
def styled_page():
    page = Page(title="Styled Page")

    header = Header(object_name="mainHeader")
    header.object_styles.set_background_color(
        "linear-gradient(135deg, #667eea 0%, #764ba2 100%)"
    ).set_color("white")\
     .set_padding("60px 20px")\
     .set_text_align("center")

    header.get_html(content="<h1>Styled Page</h1>")

    paragraph = Paragraph(text="This text is styled via CSS.")
    paragraph.object_styles.set_font_size("18px")\
                           .set_line_height("1.6")\
                           .set_color("#333")

    page.body.add_element(header)
    page.body.add_element(paragraph)

    return page

app.start()
```

### Nested Routers Application

```python
from layoutml import LayoutML, Router, Page

app = LayoutML()

# API router
api_router = Router(prefix="/api")

@api_router.route("/users")
def get_users():
    page = Page(title="API Users")
    page.body.get_html(content="""
    <h1>User List</h1>
    <ul>
        <li>Ivan Petrov</li>
        <li>Maria Ivanova</li>
    </ul>
    """)
    return page

@api_router.route("/posts")
def get_posts():
    return Page(title="Posts API")

# Admin router
admin_router = Router(prefix="/admin")

@admin_router.route("/dashboard")
def admin_dashboard():
    page = Page(title="Admin Panel")
    page.body.get_html(content="<h1>Welcome to admin panel!</h1>")
    return page

# Include routers
app.include_router(api_router)
app.include_router(admin_router)

# Main route
@app.route("/")
def home():
    page = Page(title="Home")
    page.body.get_html(content="""
    <h1>Welcome!</h1>
    <nav>
        <a href="/api/users">API Users</a> |
        <a href="/api/posts">API Posts</a> |
        <a href="/admin/dashboard">Admin Panel</a>
    </nav>
    """)
    return page

app.start()
```

### Uvicorn Integration

```python
import uvicorn
from layoutml import LayoutML, Page

app = LayoutML()

@app.route("/")
def home():
    return Page(title="Home")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

### Static Files Application

```python
from layoutml import LayoutML, Page

app = LayoutML()

@app.route("/image-page")
def image_page():
    page = Page(title="Images")
    page.body.get_html(content="""
    <h1>Image Gallery</h1>
    <img src="/static/logo.png" alt="Logo">
    <img src="/images/photo.jpg" alt="Photo">
    """)
    return page

# Static files are served automatically
# Files from project root: logo.png, images/photo.jpg, etc.
```

## Best Practices

### 1. Code organization

```python
# main.py
from layoutml import LayoutML

app = LayoutML(styles_dirname="static/css")

# Register routers
app.include_router(api_router, prefix="/api")
app.include_router(admin_router, prefix="/admin")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

### 2. Route separation

```python
# routers/users.py
from layoutml import Router, Page

users_router = Router(prefix="/users")

@users_router.route("/")
def list_users():
    return Page(title="Users")

@users_router.route("/<user_id>")
def user_detail(user_id: str):
    return Page(title=f"User {user_id}")

# main.py
app.include_router(users_router)
```
