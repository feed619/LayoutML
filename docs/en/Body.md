# Body

`Body` is a specialized class for creating the HTML `<body>` element. It is a subclass of the base class [HTMLElement](base/HTMLElement.md). This class provides a convenient interface for managing the main content of a web page, including adding HTML elements, text content, and scripts that should be executed after the DOM is loaded.

---

## Import

```python
from layoutml import Body
```

## Inheritance

- Parent class: BaseElement
- Element type: body
- Purpose: Container for the main content of the page

## Class Attributes

| Attribute      | Type              | Description                                 | Default value |
| -------------- | ----------------- | ------------------------------------------- | ------------- |
| content        | str               | Text content of the body                    | Empty string  |
| elements       | List[BaseElement] | List of HTML elements                       | Empty list    |
| scripts_footer | List[Dict]        | List of script tags for the end of the body | Empty list    |
| object_type    | str               | Object type (always "Body")                 | "Body"        |
| links          | dict              | Reserved for future use                     | Empty dict    |

## Constructor

### **init**(content: str = "", \*\*kwargs)

Initializes a new Body element with initial content and attributes.

Parameters:

| Parameter   | Type | Default | Description                        |
| ----------- | ---- | ------- | ---------------------------------- |
| content     | str  | ""      | Initial body text content          |
| object_name | str  | None    | Unique element identifier          |
| \*\*kwargs  | dict | -       | Additional attributes for `<body>` |

Initialization examples:

```python
# Empty body with basic attributes
body = Body()

# Body with initial content
body = Body(content="Welcome to our website!")

# Body with class attributes
body = Body(
    content="Page content",
    class_="main-body dark-theme",
    id="pageBody",
    data_page="home"
)

# Body with event handlers
body = Body(
    onload="initPage()",
    onscroll="handleScroll()",
    onresize="handleResize()"
)
```

## Methods

### add_content(content: str) -> "Body"

Adds text content to the body.

Parameters:

- content (str): Text to add

Returns:

- self: Allows method chaining

Examples:

```python
# Simple text addition
body = Body()
body.add_content("Welcome to our website!")

# Method chaining
body.add_content("Main content").add_content("Additional text")

# Adding formatted text
body.add_content("<h1>Title</h1>")
body.add_content("<p>Paragraph with <strong>highlight</strong>.</p>")

# Multiline content
body.add_content("""
    <div class="intro">
        <h2>Introduction</h2>
        <p>This is the first page of our website.</p>
    </div>
""")
```

### add_element(element: Any) -> "Body"

Adds an HTML element to the body.

Supported element types:

- BaseElement objects and their subclasses
- Layout, HorizontalLayout, VerticalLayout objects
- Form objects
- Any objects with a get_html() method
- Strings (raw HTML)

```python
body = Body()

# Adding different types of elements
body.add_element(BaseElement(tag="div", object_name="container"))
body.add_element(Form(form_type="text", object_name="search"))
body.add_element(Layout(object_name="mainLayout"))
```

### add_html(html: str) -> "Body"

Adds raw HTML code to the body.

```python
body = Body()

body.add_html("<div class='custom'>Custom HTML</div>")
body.add_html("<!-- Comment -->")
```

### add_script(src: Optional[str] = None, content: Optional[str] = None, \*\*attributes) -> "Body"

Adds a script tag to the end of the body (before the closing </body> tag).

Parameters:

- src (optional): URL of external script
- content (optional): Inline JavaScript code
- \*\*attributes: Additional attributes

```python
body = Body()

# External script
body.add_script(src="app.js", defer=True)
body.add_script(src="analytics.js", async=True)

# Inline script
body.add_script(content="console.log('DOM loaded');")

# Script with custom attributes
body.add_script(
    src="https://cdn.example.com/library.js",
    integrity="sha256-abc123",
    crossorigin="anonymous"
)

# Script with type="module"
body.add_script(src="module.js", type="module")
```

### get_html() -> str

Generates full HTML code of the <body> section.

```python
body = Body()
body.add_content("<h1>Title</h1>")

html = body.get_html()  # <body>...</body>
```

### get_styles() -> dict

Collects CSS styles from all body elements.

```python
body = Body()

div = BaseElement(tag="div", object_name="test")
div.object_styles.set_width("100px")

body.add_element(div)
styles = body.get_styles()  # Dictionary of styles
```

## Special Python Methods

### **str**() -> str

Returns HTML representation of the body.

```python
body = Body(content="Hello")
print(str(body))  # Outputs HTML
```

### **repr**() -> str

Returns string representation for debugging.

```python
body = Body()
body.add_element(BaseElement(tag="div"))

print(repr(body))  # Body(elements=1, content_length=0)
```

### **iadd**(other: Any) -> "Body"

Overloads the += operator for convenient element addition.

```python
body = Body()

body += BaseElement(tag="div", object_name="box1")
body += "<span>Text</span>"
# Equivalent to body.add_element(...)
```
