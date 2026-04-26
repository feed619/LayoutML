# Aside

`Aside` is a specialized class for creating the semantic HTML element <aside>. The class inherits from [BaseElement](../base/BaseElement.md) and is intended for creating side panels that contain content indirectly related to the main content of the page (sidebars, blocks with additional information, advertisement blocks, lists of related links, etc.).

---

## Import

```python
from layoutML.elements import Aside
```

## Inheritance

- Parent class: BaseElement
- Element type: aside (non-self-closing tag)
- Purpose: Creating semantic containers for supplementary content

## Constructor

### **init**(object_name=None, style=None, boolean_attributes=[], \*\*kwargs)

Creates a new sidebar element with the specified parameters.

Parameters:

- object_name (optional): Element name/identifier
- style (optional): CSS string for inline styles
- boolean_attributes (optional): List of boolean attributes
- \*_kwargs: Additional HTML attributes (id, class\_, aria-_, etc.)

Automatically assigned properties:

- Tag: aside
- self_closing: False (non-self-closing tag)
- object_type: "AsideElement"

## Examples:

```python
# Simple sidebar
aside = Aside()

# Sidebar with name and classes
aside = Aside(
    object_name="sidebar",
    class_="sidebar right-sidebar",
    id="mainSidebar"
)

# Sidebar with inline styles
aside = Aside(
    style="width: 300px; padding: 20px; background-color: #f5f5f5;",
    aria_label="Additional information"
)
```

## Styled Sidebar

```python
sidebar = Aside(object_name="styledSidebar")

# Inline styles
sidebar.inline_styles.set_width("280px")\
                     .set_padding("20px")\
                     .set_background_color("#f8f9fa")\
                     .set_border_radius("8px")\
                     .set_box_shadow("0 2px 10px rgba(0,0,0,0.1)")

# CSS styles via object_styles
sidebar.object_styles.set_font_family("Arial, sans-serif")\
                     .set_color("#555")\
                     .set_line_height("1.6")

# Adding content
sidebar.get_html(content="""
    <h3 style="margin-top: 0; color: #333;">Interesting</h3>
    <p>This could be your ad or useful information.</p>
""")
```
