# Head

`Head` is a specialized subclass of the base class [BaseElement](base/BaseElement.md), designed for creating the HTML `<head>` element with a full set of meta tags, styles, scripts, and other resources required for a web page. This class provides a convenient object-oriented interface for managing page metadata and resources.

---

## Import

```python
from layoutml import Head
```

---

## Inheritance

- Parent class: BaseElement
- Element type: head
- Purpose: Management of HTML page metadata and resources

---

## Constructor

### **init**(title: str = "", \*\*kwargs)

Initializes a new Head element with base configuration.

#### Parameters

| Parameter   | Type | Default | Description                            |
| ----------- | ---- | ------- | -------------------------------------- |
| title       | str  | ""      | Page title (shown in browser tab)      |
| object_name | str  | None    | Unique element identifier              |
| \*\*kwargs  | dict | -       | Additional attributes for `<head>` tag |

#### Automatically set properties

- Tag: head
- Encoding: UTF-8 (`<meta charset="UTF-8">`)
- Viewport: responsive (`<meta name="viewport" content="width=device-width, initial-scale=1.0">`)

#### Examples

```python id="h1k9qa"
# Simple head
head = Head()

# Head with title
head = Head(title="My Website")

# Head with additional attributes
head = Head(
    title="Documentation",
    object_name="pageHead",
    lang="ru"
)
```

---

## Class Attributes

| Attribute   | Type          | Description                             | Default value               |
| ----------- | ------------- | --------------------------------------- | --------------------------- |
| title       | str           | Page title (<title> tag)                | Empty string                |
| meta_tags   | List[Dict]    | List of meta tags                       | charset + viewport included |
| links       | List[Dict]    | List of link tags (styles, icons, etc.) | Empty list                  |
| scripts     | List[Dict]    | List of script tags                     | Empty list                  |
| styles_css  | List[str]     | Inline CSS styles                       | Empty list                  |
| base_url    | Optional[str] | Base URL for relative paths             | None                        |
| object_type | str           | Object type (always "Head")             | "Head"                      |

---

## Methods

### set_title(title: str) -> "Head"

Sets or updates the page title.

#### Parameters

- title (str): New page title

#### Examples

```python id="t2v9qz"
head = Head(title="Initial title")

head.set_title("New page title")

head.set_title("Products").add_meta(
    name="description",
    content="Product catalog"
)
```

---

### add_meta(\*\*attributes) -> "Head"

Adds a meta tag with specified attributes.

#### Parameters

- \*\*attributes: key-value pairs for meta tag attributes

#### Examples

```python id="m9x1ab"
# Charset (already added by default)
head.add_meta(charset="UTF-8")

# Viewport (already added by default)
head.add_meta(
    name="viewport",
    content="width=device-width, initial-scale=1.0"
)

# SEO description
head.add_meta(
    name="description",
    content="Online electronics store with delivery"
)

# SEO keywords
head.add_meta(
    name="keywords",
    content="electronics, smartphones, laptops, online store"
)
```

---

### add_link(rel: str, href: str, \*\*attributes) -> "Head"

Adds a link tag for external resources.

#### Parameters

- rel: Resource relation (stylesheet, icon, canonical, etc.)
- href: Resource URL
- \*\*attributes: Additional attributes

#### Examples

```python id="l4c8qp"
head = Head()

# Stylesheets
head.add_link(rel="stylesheet", href="style.css")
head.add_link(rel="stylesheet", href="mobile.css", media="(max-width: 768px)")

# Icons
head.add_link(rel="icon", href="favicon.ico", type="image/x-icon")
head.add_link(rel="apple-touch-icon", href="apple-touch-icon.png")

# Canonical URL
head.add_link(rel="canonical", href="https://example.com/page")

# Preload fonts
head.add_link(
    rel="preload",
    href="font.woff2",
    as_="font",
    type="font/woff2",
    crossorigin=True
)

# RSS feed
head.add_link(
    rel="alternate",
    href="rss.xml",
    type="application/rss+xml",
    title="RSS"
)
```

---

### add_stylesheet(href: str, media: str = "all") -> "Head"

Simplified method for adding CSS files.

```python id="s7d1mm"
head = Head()

head.add_stylesheet("style.css")
head.add_stylesheet("print.css", media="print")
```

---

### set_icon(href: str, type: str = "image/x-icon") -> "Head"

Simplified method for setting a favicon.

```python id="i3p8vn"
head = Head()

head.set_icon("favicon.ico")
head.set_icon("icon.png", type="image/png")
```

---

### add_script(src: Optional[str] = None, content: Optional[str] = None, \*\*attributes) -> "Head"

Adds a `<script>` tag with specified parameters.

#### Parameters

- src (Optional[str]): External script URL
- content (Optional[str]): Inline JavaScript code
- \*\*attributes: Additional attributes

#### Examples

```python id="sc9x2a"
# External script with defer
head.add_script(src="/js/main.js", defer=True)

# External script with async
head.add_script(src="/js/analytics.js", async=True)

# Module script
head.add_script(src="/js/app.js", type="module")

# Inline script
head.add_script(
    content="""
        console.log('Page loading');
        window.APP_CONFIG = {
            apiUrl: 'https://api.example.com',
            debug: false
        };
    """,
    type="application/javascript"
)
```

---

### get_css_text() -> str

Generates inline CSS styles from selectors_styles.

```python id="css1ab"
head = Head()
head.object_styles.set_background_color("red")

css_text = head.get_css_text()  # <style>...</style>
```

---

### get_html() -> str

Generates full HTML code for the `<head>` section.

```python id="html9zz"
head = Head(title="Page")
html = head.get_html()  # <head>...</head>
```

---

## Examples

### Example 1: Basic Page Setup

```python id="ex1hd9"
head = Head(title="Welcome to my website")

# Meta tags
head.add_meta(name="description", content="Personal blog about programming and tech")
head.add_meta(name="keywords", content="programming, python, blog, technology")
head.add_meta(name="author", content="Ivan Petrov")

# Styles
head.add_stylesheet("css/main.css")
head.add_stylesheet("css/mobile.css", media="(max-width: 768px)")

# Icons
head.set_icon("favicon.ico")
head.add_link(rel="apple-touch-icon", href="apple-touch-icon.png")

# Scripts
head.add_script(src="js/app.js", defer=True)

print(head.get_html())
```
