# Page

`Page` is a specialized descendant of the base class [BaseElement](base/BaseElement.md), designed for creating complete HTML documents. The class combines the Head and Body components into a single structure and provides methods for rendering, saving, and managing the entire HTML document.

---

## Import

```python
from layoutml import Page
```

## Inheritance

- Parent class: BaseElement
- Element type: html (document root element)
- Purpose: Creating complete HTML pages with all required structure

## Class Attributes

| Attribute       | Type | Description                   | Default Value                   |
| --------------- | ---- | ----------------------------- | ------------------------------- |
| doctype         | str  | HTML document type            | `"html"`                        |
| head            | Head | Head section object           | Created with title `"LayoutML"` |
| body            | Body | Body section object           | Empty Body object               |
| object_type     | str  | Object type (always `"Page"`) | `"Page"`                        |
| render_css_file | bool | CSS file generation flag      |

## Constructor

### **init**(doctype: str = "html", title: str = "LayoutML", lang="ru", object_name=None, \*\*kwargs)

Creates a new HTML page with basic settings.

Parameters:

- doctype (str): Document type. Default is `"html"` (HTML5). Supported values can be found in [DocTypes](types/DocTypes.md)
- title (str): Page title. Default is `"LayoutML"`
- lang (str): Document language. Default is `"ru"`
- object_name (optional): Page name/identifier
- \*\*kwargs: Additional HTML element attributes

Automatically created components:

- Head object with the specified title
- Body object for main content
- Sets the html tag with the specified language

Examples:

```python
# Simple page
page = Page()

# Customized page
page = Page(
    title="My Website",
    lang="ru",
    doctype="html5",
    object_name="homePage"
)

# Page with additional attributes
page = Page(
    title="Documentation",
    class_="documentation",
    data_theme="dark"
)
```

## Methods

### set_head(head: Head) -> "Page"

Replaces the page head object with a custom one.

```python
custom_head = Head(title="Custom Title")
page = Page()
page.set_head(custom_head)
```

### set_body(body: Body) -> "Page"

Replaces the page body object with a custom one.

```python
custom_body = Body()
custom_body.add_content("<h1>Hello!</h1>")
page = Page()
page.set_body(custom_body)
```

### set_doctype(doctype: str) -> "Page"

Sets the document type.

```python
page = Page()
page.set_doctype("html5")      # HTML5
page.set_doctype("xhtml")      # XHTML 1.0 Transitional
page.set_doctype("strict")     # HTML 4.01 Strict
page.set_doctype("transitional")  # HTML 4.01 Transitional
```

### set_language(lang: str) -> "Page"

Sets the document language (lang attribute of the `<html>` tag).

```python
page = Page()
page.set_language("en")    # English
page.set_language("ru")    # Russian
page.set_language("es")    # Spanish
```

### get_element(object_name: str) -> Layout | BaseElement

Finds and returns an element by its name.

Exceptions:

- AttributeError: If the element is not found

```python
element = page.get_element("submitButton")
```

### remove_element(object_name: str) -> None

Removes an element from body by object name.

```python
page.remove_element("oldButton")
```

### add_element(element)

Adds an element to the document body.

Parameters:

- element (BaseElement): HTML element to add

Note: This method is intended for compatibility with legacy code and works with the document attribute, which must be set.

```python
from layoutml import Paragraph

app = LayoutML()
app.add_element(Paragraph(text="Hello, world!"))
```

### add_stylesheet(href: str, media: str = "all") -> Head

Adds a CSS file to the head section.

```python
page.add_stylesheet("css/style.css")
page.add_stylesheet("css/print.css", media="print")
```

### add_script(src: Optional[str] = None, content: Optional[str] = None, \*\*attributes) -> "Page"

Adds a script tag to the head section.

Parameters:

- src (optional): External script URL
- content (optional): Inline JavaScript code
- \*\*attributes: Additional attributes (defer, async, type, etc.)

```python
page = Page()

# External script
page.add_script(src="app.js", defer=True)

# Inline script
page.add_script(content="console.log('Page loaded');")

# Script with custom attributes
page.add_script(
    src="https://cdn.example.com/library.js",
    integrity="sha256-abc123",
    crossorigin="anonymous"
)
```

### get_html() -> str

Generates the complete HTML code of the document.

```python
page = Page(title="Test Page")
html = page.get_html()  # Full HTML document
```

### render() -> str

Renders the complete HTML document with automatic CSS file generation.

Features:

- Collects CSS styles from all components
- Creates a CSS file in the styles/ folder
- Adds a link to the generated CSS file in head
- Returns the complete HTML document

```python
page = Page()
page.body.add_element(BaseElement(tag="div", object_name="test"))
html = page.render()  # Creates CSS file and returns HTML
```

### get_css_text() -> str

Generates the CSS text from all page components.

```python
page = Page()
css_text = page.get_css_text()  # All CSS styles in one string
```

### get_styles() -> dict

Collects CSS styles from all page components into a dictionary.

```python
page = Page()
styles = page.get_styles()  # Dictionary {selector: styles}
```

### save(filename: str, encoding: str = "utf-8") -> None

Saves the HTML document to a file.

```python
page = Page(title="My Page")
page.save("index.html")               # Saves to index.html
page.save("page.html", encoding="utf-8-sig")  # With specified encoding
```

## Usage Examples

### Example 1: Simple HTML Page

```python
# Creating a basic page
page = Page(
    title="Welcome to My Website",
    lang="ru",
    doctype="html5"
)

# Configuring head
page.head.add_meta(
    name="description",
    content="Personal website about programming and technology"
)
page.head.add_stylesheet("css/style.css")
page.head.add_script(src="js/app.js", defer=True)

# Adding content to body
page.body.add_content("""
    <header>
        <h1>Hello, world!</h1>
    </header>

    <main>
        <p>This is my first page created with LayoutML.</p>
    </main>

    <footer>
        <p>&copy; 2024 My Website</p>
    </footer>
""")

# Saving to file
page.save("index.html")

# Or getting HTML code
html_code = page.get_html()
print(html_code)
```
