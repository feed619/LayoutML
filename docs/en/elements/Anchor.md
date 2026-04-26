# Anchor

`Anchor` is a specialized class for creating HTML links (<a>). The class inherits from [BaseElement](../base/BaseElement.md) and provides a convenient interface for creating hyperlinks with automatic assignment of required attributes href and target.

---

## Import

```python
from layoutML.elements import Anchor
```

## Inheritance

- Parent class: BaseElement
- Element type: a (non-self-closing tag)
- Purpose: Creating hyperlinks for navigation

## Class Attributes

| Attribute   | Type | Description                          | Default value      |
| ----------- | ---- | ------------------------------------ | ------------------ |
| href        | str  | URL or anchor of the link            | Required parameter |
| text        | str  | Link text                            | Empty string       |
| target      | str  | How the link is opened               | "\_self"           |
| object_type | str  | Object type (always "AnchorElement") | "AnchorElement"    |
| tag         | str  | HTML tag (always "a")                | "a"                |

## Constructor

### **init**(href, text="", target="\_self", object_name=None, style=None, boolean_attributes=[], \*\*kwargs)

Creates a new link element with the specified parameters.

Parameters:

- href (str): URL or anchor the link points to. Required parameter
- text (str): Link text (displayed between tags). Defaults to empty string
- target (str): How the link is opened. Defaults to "\_self". Possible values: "\_self", "\_blank", "\_parent", "\_top"
- object_name (optional): Element name/identifier
- style (optional): CSS string for inline styles
- boolean_attributes (optional): List of boolean attributes
- \*\*kwargs: Additional HTML attributes (id, class\_, rel, download, etc.)

Automatically assigned properties:

- Tag: a
- self_closing: False (non-self-closing tag)
- object_type: "AnchorElement"
- href: link URL
- text: link text
- target: link opening behavior

## Examples:

```python
# Simple link
link = Anchor(href="https://example.com", text="Visit site")

# Link with additional attributes
link = Anchor(
    href="/about",
    text="About us",
    target="_blank",
    class_="nav-link",
    id="aboutLink",
    rel="noopener noreferrer"
)

# Link with inline styles
link = Anchor(
    href="#section1",
    text="Go to section",
    style="color: blue; text-decoration: none;",
    class_="anchor-link"
)
```

## Usage Examples

### Internal Links

```python
# Home page link
home_link = Anchor(href="/", text="Home")

# About page link
about_link = Anchor(href="/about", text="About us", class_="nav-link")

# In-page section link
section_link = Anchor(href="#services", text="Our services")
```

### External Links

```python
# External link opening in a new tab
external_link = Anchor(
    href="https://google.com",
    text="Google",
    target="_blank",
    rel="noopener noreferrer"
)

# Secure external link with extra attributes
secure_link = Anchor(
    href="https://example.com",
    text="Example",
    target="_blank",
    rel="noopener noreferrer nofollow"
)
```

### Anchor Links

```python
# Back to top link
top_link = Anchor(href="#top", text="↑ Top")

# Link to a specific element
section_link = Anchor(href="#comments", text="Go to comments")
```

### Download Links

```python
# File download link
download_link = Anchor(
    href="/files/document.pdf",
    text="Download PDF",
    download="",
    target="_blank"
)

# Download with specified filename
image_link = Anchor(
    href="/images/photo.jpg",
    text="Download photo",
    download="my_photo.jpg"
)
```

### Email and Phone Links

```python
# Email link
email_link = Anchor(
    href="mailto:info@example.com",
    text="Email us"
)

# Phone link
phone_link = Anchor(
    href="tel:+79991234567",
    text="+7 (999) 123-45-67"
)
```
