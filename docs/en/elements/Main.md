# Main

`Main` is a specialized class for creating the semantic HTML element <main>. The class inherits from [BaseElement](../base/BaseElement.md) and is intended to represent the main, unique content of a document, which does not repeat across other pages of a site (unlike headers, footers, navigation, and sidebars).

---

## Import

```python
from layoutML.elements import Main
```

## Inheritance

- Parent class: BaseElement
- Element type: main (non-self-closing tag)
- Purpose: Wrapper for the main unique content of a page

## Semantic meaning

The <main> element represents the main content of a document or application. A page should contain only one <main> element, and it should not include content that is repeated across pages (such as sidebars, navigation, copyright information, site logos, or search forms).

---

## Constructor

### **init**(object_name=None, style=None, boolean_attributes=[], \*\*kwargs)

Creates a new main content element with the specified parameters.

Parameters:

- object_name (optional): Element name/identifier
- style (optional): CSS string for inline styles
- boolean_attributes (optional): List of boolean attributes
- \*_kwargs: Additional HTML attributes (id, class\_, aria-_, etc.)

---

### Automatically assigned properties:

- Tag: main
- self_closing: False (non-self-closing tag)
- object_type: "MainElement"

---

## Examples:

```python
# Simple main element
main = Main()

# Main with name and classes
main = Main(
    object_name="mainContent",
    class_="content-wrapper",
    id="pageMain"
)

# Main with inline styles
main = Main(
    style="max-width: 1200px; margin: 0 auto; padding: 20px;",
    aria_label="Main page content"
)
```

---

## Class attributes

| Attribute    | Type | Description                        | Default value |
| ------------ | ---- | ---------------------------------- | ------------- |
| object_type  | str  | Object type (always "MainElement") | "MainElement" |
| tag          | str  | HTML tag (always "main")           | "main"        |
| self_closing | bool | Self-closing flag (always False)   | False         |
