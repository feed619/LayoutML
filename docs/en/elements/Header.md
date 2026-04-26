# Header

`Header` is a specialized class for creating the semantic HTML element <header>. The class inherits from [BaseElement](../base/BaseElement.md) and is intended for creating page or section headers containing introductory information, navigation, logos, titles, and other elements typically placed at the top of a document.

---

## Import

```python
from layoutML.elements import Header
```

## Inheritance

- Parent class: BaseElement
- Element type: header (non-self-closing tag)
- Purpose: Creating semantic containers for page and section headers

## Constructor

### **init**(object_name=None, style=None, boolean_attributes=[], \*\*kwargs)

Creates a new header element with the specified parameters.

Parameters:

- object_name (optional): Element name/identifier
- style (optional): CSS string for inline styles
- boolean_attributes (optional): List of boolean attributes
- \*_kwargs: Additional HTML attributes (id, class\_, aria-_, etc.)

Automatically assigned properties:

- Tag: header
- self_closing: False (non-self-closing tag)
- object_type: "HeaderElement"

## Examples:

```python id="header_ex_01"
# Simple header
header = Header()

# Header with name and classes
header = Header(
    object_name="pageHeader",
    class_="header main-header",
    id="siteHeader"
)

# Header with inline styles
header = Header(
    style="background-color: #333; color: white; padding: 20px;",
    aria_label="Site header"
)
```
