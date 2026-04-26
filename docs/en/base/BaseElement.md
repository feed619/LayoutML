# BaseElement

`BaseElement` is an extended class for creating HTML elements with support for CSS styles through `CSSBase` and `CSSSelectors` objects. The class inherits from [HTMLElement](HTMLElement.md) and adds capabilities for managing external CSS styles, automatic class generation, and flexible HTML rendering.

---

## Inheritance

- Parent class: [HTMLElement](HTMLElement.md)
- Adds: CSS style management via objects, automatic class-style binding

---

## Class Attributes

| Attribute        | Type         | Description                                 | Origin           |
| ---------------- | ------------ | ------------------------------------------- | ---------------- |
| object_styles    | CSSBase      | Object for managing element CSS styles      | New              |
| selectors_styles | CSSSelectors | Container for CSS selectors and styles      | New              |
| tag              | str          | HTML tag (div, span, button, etc.)          | New              |
| self_closing     | bool         | Flag for self-closing tags (img, br, input) | New              |
| inline_styles    | CSSInline    | Inline styles for the element               | From HTMLElement |
| class\_          | list[str]    | List of CSS classes                         | From HTMLElement |
| object_name      | str          | Object name/identifier                      | From HTMLElement |
| object_type      | str          | Object type                                 | From HTMLElement |

---

## Constructor

### **init**(tag="", self_closing: bool = False, object_name=None, style=None, boolean_attributes=[], \*\*kwargs)

Creates a new base HTML element with CSS support.

Parameters:

- tag (str): HTML tag (e.g. "div", "span", "button"). Default is empty string
- self_closing (bool): If True, element is self-closing. Default is False
- object_name (optional): Name/identifier of the element
- style (optional): CSS string for inline styles
- boolean_attributes (optional): List of boolean attributes
- \*\*kwargs: Additional HTML attributes

Examples:

```python
# Simple div element
div_element = BaseElement(tag="div")

# Self-closing element (img)
img_element = BaseElement(
    tag="img",
    self_closing=True,
    src="image.jpg",
    alt="Description"
)

# Element with styles and attributes
button = BaseElement(
    tag="button",
    object_name="submitBtn",
    style="padding: 10px;",
    class_="btn-primary",
    onclick="submitForm()",
    disabled=True
)
```

---

## Core Methods

### get_html(content: str = "", tab: int = 0) -> str

Generates the HTML string for the element.

Parameters:

- content (str): Inner HTML content. Default is empty string
- tab (int): Indentation level for formatting. Default is 0

Examples:

```python
# Simple element
element = BaseElement(tag="div", object_name="container")
html = element.get_html()
# Result: <div class="container" ></div>

# Element with content
element = BaseElement(tag="p", object_name="description")
html = element.get_html(content="Hello World")
# Result: <p class="description" >Hello World</p>

# Self-closing element
element = BaseElement(tag="img", self_closing=True, src="photo.jpg")
html = element.get_html()
# Result: <img src="photo.jpg" >

# With indentation
element = BaseElement(tag="div", object_name="wrapper")
html = element.get_html(content="\n    <p>Content</p>\n", tab=1)
# Result:
# <div class="wrapper" >
#     <p>Content</p>
# </div>
```

---

### get_styles(space: bool = True) -> dict

Generates a dictionary of CSS styles for the element and binds them to classes.

Parameters:

- space (bool): If True, formats CSS with spaces and line breaks

Returns:

- Dictionary in format {selector: css_styles}

Examples:

```python
element = BaseElement(tag="div", object_name="myElement")

element.object_styles.set_width("100px")\
                     .set_height("100px")\
                     .set_background_color("red")

styles = element.get_styles()

# Result:
# {'.myElement': 'width:100px;height:100px;background-color:red;'}

formatted = element.get_styles(space=True)

# Result:
# {'.myElement': ' width: 100px;\n height: 100px;\n background-color: red;'}
```

---

## Examples

### Example 1: Modal window with animation

```python
modal = BaseElement(
    tag="div",
    object_name="modalOverlay",
    role="dialog",
    aria_modal="true",
    aria_labelledby="modalTitle",
    aria_hidden="true"
)

modal.object_styles.set_position("fixed")\
                   .set_top("0")\
                   .set_left("0")\
                   .set_width("100%")\
                   .set_height("100%")\
                   .set_background_color("rgba(0,0,0,0.5)")\
                   .set_display("flex")\
                   .set_justify_content("center")\
                   .set_align_items("center")\
                   .set_z_index("1000")\
                   .set_opacity("0")\
                   .set_visibility("hidden")\
                   .set_transition("opacity 0.3s, visibility 0.3s")

show_styles = CSSBase()
show_styles.set_opacity("1").set_visibility("visible")

modal.selectors_styles.add_selector("modalOverlay.show").merge_styles(show_styles.styles)

modal_content = BaseElement(
    tag="div",
    object_name="modalContent",
    role="document"
)

modal_content.object_styles.set_background_color("white")\
                           .set_padding("30px")\
                           .set_border_radius("8px")\
                           .set_max_width("500px")\
                           .set_width("90%")\
                           .set_transform("scale(0.9)")\
                           .set_transition("transform 0.3s")

content_show_styles = CSSBase()
content_show_styles.set_transform("scale(1)")

modal_content.selectors_styles.add_selector("modalContent.show").merge_styles(content_show_styles.styles)
```

---

### Example 2: Navigation menu

```python
nav = BaseElement(
    tag="nav",
    object_name="mainNav",
    role="navigation",
    aria_label="Main navigation"
)

nav.object_styles.set_background_color("#333")\
                 .set_padding("15px 0")\
                 .set_display("flex")\
                 .set_justify_content("center")\
                 .set_gap("30px")

menu_items = ["Home", "Products", "About", "Contact"]
menu_content = ""

for item in menu_items:
    menu_item = BaseElement(
        tag="a",
        object_name=f"nav{item}",
        href=f"/{item.lower()}",
        aria_current="page" if item == "Home" else None
    )

    menu_item.object_styles.set_color("white")\
                           .set_text_decoration("none")\
                           .set_padding("10px")\
                           .set_border_radius("4px")\
                           .set_transition("background-color 0.3s")

    menu_item.selectors_styles.add_selector(f"nav{item}:hover").set_background_color("#555")

    menu_content += menu_item.get_html(content=item) + "\n"

nav_html = nav.get_html(content=menu_content, tab=1)
```

---
