# Page

`Page` is a specialized subclass of the base class [BaseElement](base/BaseElement.md) for creating complete HTML documents. This class combines the Head and Body components into a unified structure and provides methods for rendering, saving, and managing the entire HTML document.

---

## Import

```python
from layoutml import Page
```

---

## Inheritance

- Parent class: BaseElement
- Element type: html (root document element)
- Purpose: Creation of full HTML pages with complete structure

---

## Class Attributes

| Attribute   | Type | Description                 | Default value                 |
| ----------- | ---- | --------------------------- | ----------------------------- |
| doctype     | str  | Document type               | "html"                        |
| head        | Head | Head section object         | Created with title "LayoutML" |
| body        | Body | Body section object         | Empty Body object             |
| object_type | str  | Object type (always "Page") | "Page"                        |

---

## Constructor

### **init**(doctype: str = "html", title: str = "LayoutML", lang="ru", object_name=None, \*\*kwargs)

Creates a new HTML page with base configuration.

#### Parameters

- doctype (str): Document type. Default is "html" (HTML5). Supported values can be found in [DocTypes](types/DocTypes.md)
- title (str): Page title. Default is "LayoutML"
- lang (str): Document language. Default is "ru"
- object_name (optional): Page identifier
- \*\*kwargs: Additional HTML attributes

#### Automatically created components

- Head object with provided title
- Body object for main content
- HTML tag with specified language

#### Examples

```python
# Simple page
page = Page()

# Custom page
page = Page(
    title="My website",
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

---

## Methods

### set_head(head: Head) -> "Page"

Replaces the page head object with a custom one.

```python
custom_head = Head(title="Custom title")

page = Page()
page.set_head(custom_head)
```

---

### set_body(body: Body) -> "Page"

Replaces the page body object with a custom one.

```python
custom_body = Body()
custom_body.add_content("<h1>Hello!</h1>")

page = Page()
page.set_body(custom_body)
```

---

### set_doctype(doctype: str) -> "Page"

Sets the document type.

```python
page = Page()

page.set_doctype("html5")        # HTML5
page.set_doctype("xhtml")        # XHTML 1.0 Transitional
page.set_doctype("strict")       # HTML 4.01 Strict
page.set_doctype("transitional")  # HTML 4.01 Transitional
```

---

### set_language(lang: str) -> "Page"

Sets the document language (lang attribute of the `<html>` tag).

```python
page = Page()

page.set_language("en")  # English
page.set_language("ru")  # Russian
page.set_language("es")  # Spanish
```

---

### add_element(element)

Adds an element to the body of the document.

#### Parameters

- element (BaseElement): HTML element to add

#### Note

This method is provided for backward compatibility and works with the document attribute that must be set.

```python
from layoutml import Paragraph

app = LayoutML()
app.add_element(Paragraph(text="Hello, world!"))
```

---

### add_script(src: Optional[str] = None, content: Optional[str] = None, \*\*attributes) -> "Page"

Adds a script tag to the head section.

#### Parameters

- src (optional): External script URL
- content (optional): Inline JavaScript code
- \*\*attributes: Additional attributes (defer, async, type, etc.)

```python
page = Page()

# External script
page.add_script(src="app.js", defer=True)

# Inline script
page.add_script(content="console.log('Page loaded');")

# Script with attributes
page.add_script(
    src="https://cdn.example.com/library.js",
    integrity="sha256-abc123",
    crossorigin="anonymous"
)
```

---

### get_html() -> str

Generates the full HTML document.

```python
page = Page(title="Test page")

html = page.get_html()  # Full HTML document
```

---

### render() -> str

Renders the full HTML document and automatically generates a CSS file.

#### Features

- Collects CSS styles from all components
- Creates a CSS file in the styles/ folder
- Adds a link to the generated CSS file in head
- Returns full HTML document

```python
page = Page()

page.body.add_element(BaseElement(tag="div", object_name="test"))

html = page.render()  # Creates CSS file and returns HTML
```

---

### get_css_text() -> str

Generates CSS text from all page components.

```python
page = Page()

css_text = page.get_css_text()
```

---

### get_styles() -> dict

Collects CSS styles from all page components into a dictionary.

```python
page = Page()

styles = page.get_styles()  # {selector: styles}
```

---

### save(filename: str, encoding: str = "utf-8") -> None

Saves the HTML document to a file.

```python
page = Page(title="My page")

page.save("index.html")
page.save("page.html", encoding="utf-8-sig")
```

---

## Usage Examples

### Example 1: Simple HTML Page

```python
page = Page(
    title="Welcome to my website",
    lang="ru",
    doctype="html5"
)

# Head configuration
page.head.add_meta(
    name="description",
    content="Personal website about programming and technology"
)

page.head.add_stylesheet("css/style.css")
page.head.add_script(src="js/app.js", defer=True)

# Body content
page.body.add_content("""
    <header>
        <h1>Hello, world!</h1>
    </header>

    <main>
        <p>This is my first page created with LayoutML.</p>
    </main>

    <footer>
        <p>&copy; 2024 My website</p>
    </footer>
""")

# Save file
page.save("index.html")

# Or get HTML string
html_code = page.get_html()
print(html_code)
```
