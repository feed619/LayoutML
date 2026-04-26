# Nav

`Nav` is a specialized class for creating the semantic HTML element <nav>. The class inherits from [BaseElement](../base/BaseElement.md) and is intended for creating navigation blocks that contain links for navigating through a website or within a page.

---

## Import

```python
from layoutML.elements import Nav
```

## Inheritance

* Parent class: BaseElement
* Element type: nav (non-self-closing tag)
* Purpose: Creating semantic containers for navigation elements

## Constructor

### **init**(object_name=None, style=None, boolean_attributes=[], **kwargs)

Creates a new navigation element with the specified parameters.

### Parameters:

* object_name (optional): Element name/identifier
* style (optional): CSS string for inline styles
* boolean_attributes (optional): List of boolean attributes
* **kwargs: Additional HTML attributes (id, class_, aria-*, etc.)

### Automatically assigned properties:

* Tag: nav
* self_closing: False (non-self-closing tag)
* object_type: "NavElement"

### Examples:

```python
# Simple navigation block
nav = Nav()

# Navigation with name and classes
nav = Nav(
    object_name="mainNav",
    class_="navigation main-nav",
    id="siteNavigation"
)

# Navigation with inline styles
nav = Nav(
    style="background-color: #333; padding: 15px;",
    aria_label="Main site navigation"
)
```