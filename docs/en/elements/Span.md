# Span

`Span` is a specialized class for creating the HTML element <span>. The class inherits from [BaseElement](../base/BaseElement.md) and is intended for creating inline containers used for grouping and styling text or other elements without adding semantic meaning.

---

## Import

```python
from layoutML.elements import Span
```

## Inheritance

- Parent class: BaseElement
- Element type: span (non-self-closing tag)
- Purpose: Creating inline containers for styling and grouping content

## Constructor

### **init**(text="", object_name=None, style=None, boolean_attributes=[], \*\*kwargs)

Creates a new inline span element with the specified parameters.

Parameters:

- text (str): Text inside the element. Defaults to empty string
- object_name (optional): Element name/identifier
- style (optional): CSS string for inline styles
- boolean_attributes (optional): List of boolean attributes
- \*_kwargs: Additional HTML attributes (id, class\_, aria-_, etc.)

### Automatically assigned properties:

- Tag: span
- self_closing: False (non-self-closing tag)
- object_type: "SpanElement"
- text: element text

## Examples:

```python
# Empty span
span = Span()

# Span with text
span = Span(text="Highlighted text")

# Span with text and attributes
span = Span(
    text="Important word",
    object_name="highlight",
    class_="important-text",
    style="color: red; font-weight: bold;"
)
```

## Usage examples

### Text highlighting

```python
# Color highlighting
highlight = Span(
    text="important text",
    class_="highlight",
    style="background-color: yellow; font-weight: bold;"
)

# Formatting inside a paragraph
paragraph = Paragraph()
paragraph.get_html(content=f'''
    This is normal text, and this is {highlight.get_html()} that deserves attention.
''')
```

### Icons and symbols

```python
# Icon via span
icon_span = Span(
    text="🔍",
    class_="icon",
    style="font-size: 20px; margin-right: 5px;"
)

# Icon with text
search_span = Span(
    text="Search",
    class_="search-label"
)

search_container = Span()
search_container.get_html(content=f"{icon_span.get_html()} {search_span.get_html()}")
```

### Styled text fragments

```python
# Different styles in one text
name_span = Span(
    text="Ivan Petrov",
    class_="name",
    style="font-weight: bold; color: #007bff;"
)

role_span = Span(
    text="(Developer)",
    class_="role",
    style="color: #666; font-size: 0.9em;"
)

user_info = Span()
user_info.get_html(content=f"{name_span.get_html()} {role_span.get_html()}")
```

### Interactive elements

```python
# Clickable span
clickable_span = Span(
    text="Click me",
    class_="clickable",
    style="cursor: pointer; color: blue; text-decoration: underline;"
)

# Adding event
clickable_span.add_event("onclick", "alert('Span clicked!')")
```

### Breadcrumbs

```python
# Breadcrumb separators
separator = Span(
    text="/",
    class_="separator",
    style="margin: 0 8px; color: #999;"
)

breadcrumb = Span()
breadcrumb.get_html(content=f'''
    <a href="/">Home</a>
    {separator.get_html()}
    <a href="/catalog">Catalog</a>
    {separator.get_html()}
    <span>Products</span>
''')
```
