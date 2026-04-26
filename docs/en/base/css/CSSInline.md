# CSSInline

`CSSInline` is a specialized class that inherits from [CSSBase](CSSBase.md) and is designed for generating inline styles for HTML elements. The class provides a convenient way to create a CSS style string in a format suitable for insertion into an HTML `style` attribute.

---

## Import

```python
from LayoutML.base.css import CSSInline
```

---

## Inheritance

- Parent class: [CSSBase](CSSBase.md)
- Inherits all methods from [CSSBase](CSSBase.md)
- Adds special methods for working with inline styles

---

## Constructor

### **init**(style=None)

Creates a new instance of CSSInline for working with inline styles.

Parameters:

- style (optional): CSS style string to parse

Examples:

```python
# Create an empty object
css = CSSInline()

# Create with initial styles
css = CSSInline(style="color: red; font-size: 16px;")

# Use inherited CSSBase methods
css.set_width("100px").set_background_color("blue")
```

---

## Core Methods

### get_styles_str(space=False) -> str

Generates a ready-to-use HTML `style` attribute string.

Parameters:

- space (bool): If True, formats with spaces and line breaks inside the attribute

Returns:

- A `style` attribute string or an empty string if no styles are set

Examples:

```python
css = CSSInline()
css.set_color("red").set_font_size("16px")

# Without formatting
print(css.get_styles_str())
# Result: 'style="color:red;font-size:16px;"'

# With formatting
print(css.get_styles_str(space=True))
# Result: 'style="  color: red;\n  font-size: 16px;"'

# Empty styles
css_empty = CSSInline()
print(css_empty.get_styles_str())
# Result: ""
```

---

## Inherited Methods

CSSInline inherits all methods from CSSBase, including:

### Method categories:

- Box model: set_width(), set_height(), set_margin(), etc.
- Positioning: set_position(), set_top(), set_left(), etc.
- Flexbox: set_flex_direction(), set_justify_content(), etc.
- Grid: set_grid_template_columns(), set_grid_area(), etc.
- Text: set_color(), set_font_family(), set_text_align(), etc.
- CSS variables: set_css_variable(), get_css_variable()
- Utility methods: add_style(), remove_style(), clear_styles(), etc.
