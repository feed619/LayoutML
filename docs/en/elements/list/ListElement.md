# ListElement

`ListElement` is the base class for creating HTML list elements. The class inherits from [BaseElement](../base/BaseElement.md) and provides common functionality for working with ordered (<ol>) and unordered (<ul>) lists, including item management and rendering.

---

## Import

```python
from layoutML.list import ListElement
```

## Purpose

This class is intended to be used as a parent for specific list types:

- UnorderedList (bulleted list <ul>)
- OrderedList (numbered list <ol>)

## Inheritance

- Parent class: BaseElement
- Element type: Depends on the provided tag (ul or ol)
- Purpose: Creation and management of list elements

## Class Attributes

| Attribute | Type | Description | Default |
| --------- | ---- | ----------- | ------- |
| items     | list | List items  | []      |

## Constructor

### **init**(tag, items=None, object_name=None, style=None, boolean_attributes=[], \*\*kwargs)

Creates a new list element with the specified parameters.

Parameters:

- tag (str): HTML list tag (ul or ol). Required parameter
- items (list): Initial list items. Default is None
- object_name (optional): Name/identifier of the element
- style (optional): CSS string for inline styles
- boolean_attributes (optional): List of boolean attributes
- \*_kwargs: Additional HTML attributes (id, class\_, aria-_, etc.)

Automatically set properties:

- self_closing: False (not a self-closing tag)
- items: list of list items

Examples:

```python
# Unordered list
ul = ListElement(tag="ul", items=["Item 1", "Item 2", "Item 3"])

# Ordered list with initial items
ol = ListElement(
    tag="ol",
    items=["First", "Second", "Third"],
    class_="numbered-list"
)

# Empty list for later population
list_element = ListElement(tag="ul", object_name="myList")
```

## Core Methods

### add_item(item)

Adds an item to the list.

Parameters:

- item (str or BaseElement): Item to add. Can be a string or an object derived from BaseElement

```python
list_element = ListElement(tag="ul")

# Adding a string item
list_element.add_item("Simple text")

# Adding an HTML element
from layoutml import Anchor
link_item = Anchor(href="/page", text="Link")
list_element.add_item(link_item)
```

## Usage Examples

### Creating an unordered list

```python
from layoutml import UnorderedList

# Using constructor
ul = UnorderedList(items=["Apple", "Banana", "Orange"])

# Adding items dynamically
ul = UnorderedList()
ul.add_item("First item")
ul.add_item("Second item")
ul.add_item("Third item")
```

### Creating an ordered list

```python
from layoutml import OrderedList

# Using constructor
ol = OrderedList(items=["First", "Second", "Third"])

# With settings
ol = OrderedList(
    items=["Step 1", "Step 2", "Step 3"],
    class_="steps",
    start="1"
)
```

### Nested lists

```python
from layoutml import UnorderedList

# Outer list
main_list = UnorderedList()

# First item with nested list
item1 = "Fruits"
nested_list1 = UnorderedList(items=["Apple", "Pear", "Banana"])

main_list.add_item(item1)
main_list.add_item(nested_list1)

# Second item with nested list
item2 = "Vegetables"
nested_list2 = UnorderedList(items=["Tomato", "Cucumber", "Carrot"])

main_list.add_item(item2)
main_list.add_item(nested_list2)

html = main_list.get_html()
```

### Lists with complex content

```python
from layoutml import UnorderedList, Anchor, Span, Image

menu = UnorderedList(class_="nav-menu")

# Link with icon
home = Anchor(href="/", text="🏠 Home")
menu.add_item(home)

# Link with description
about_container = Span()
about_link = Anchor(href="/about", text="About us")
about_desc = Span(text=" (more about the company)", class_="description")

about_container.get_html(content=f"{about_link.get_html()} {about_desc.get_html()}")
menu.add_item(about_container)

# Image link
logo_link = Anchor(href="/")
logo_img = Image(src="logo.png", alt="Logo")
logo_link.get_html(content=logo_img.get_html())

menu.add_item(logo_link)
```

### Styled lists

```python
from layoutml import UnorderedList

styled_list = UnorderedList(
    items=["Item 1", "Item 2", "Item 3"],
    object_name="styledList"
)

# Inline styles
styled_list.inline_styles.set_list_style_type("none")\
                         .set_padding_left("0")

# Styles for list items
styled_list.selectors_styles.add_selector("styledList li")\
    .set_padding("8px 12px")\
    .set_margin_bottom("5px")\
    .set_background_color("#f8f9fa")\
    .set_border_radius("4px")

# Custom markers via pseudo-elements
styled_list.selectors_styles.add_selector("styledList li::before")\
    .set_content("'✓ '")\
    .set_color("#28a745")\
    .set_font_weight("bold")
```

### Horizontal menu

```python
from layoutml import UnorderedList

horizontal_menu = UnorderedList(
    items=[
        Anchor(href="/", text="Home"),
        Anchor(href="/about", text="About"),
        Anchor(href="/services", text="Services"),
        Anchor(href="/contact", text="Contact")
    ],
    class_="horizontal-nav"
)

# Styling horizontal menu
horizontal_menu.object_styles.set_display("flex")\
                             .set_list_style_type("none")\
                             .set_padding("0")\
                             .set_margin("0")\
                             .set_gap("20px")

horizontal_menu.selectors_styles.add_selector(".horizontal-nav li")\
    .set_display("inline-block")

horizontal_menu.selectors_styles.add_selector(".horizontal-nav a")\
    .set_text_decoration("none")\
    .set_color("#333")\
    .set_padding("10px 15px")\
    .set_border_radius("4px")\
    .set_transition("background-color 0.3s")

horizontal_menu.selectors_styles.add_selector(".horizontal-nav a:hover")\
    .set_background_color("#007bff")\
    .set_color("white")
```

### List with custom markers

```python
from layoutml import UnorderedList

custom_list = UnorderedList(
    items=[
        "Task 1: Create project",
        "Task 2: Write code",
        "Task 3: Test",
        "Task 4: Deploy"
    ],
    class_="task-list"
)

# Custom markers via CSS
custom_list.selectors_styles.add_selector(".task-list")\
    .set_list_style_type("none")\
    .set_padding_left("0")

custom_list.selectors_styles.add_selector(".task-list li")\
    .set_padding("8px 0 8px 30px")\
    .set_position("relative")

custom_list.selectors_styles.add_selector(".task-list li::before")\
    .set_content("'☐ '")\
    .set_position("absolute")\
    .set_left("0")\
    .set_color("#007bff")\
    .set_font_size("18px")
```

### Definition list (via BaseElement)

```python
from layoutml import BaseElement

# For definition lists (<dl>) a separate approach is used
dl = BaseElement(tag="dl", class_="definition-list")

terms_and_defs = [
    ("HTML", "HyperText Markup Language"),
    ("CSS", "Cascading Style Sheets"),
    ("Python", "Programming language")
]

for term, definition in terms_and_defs:
    dt = BaseElement(tag="dt")
    dt.get_html(content=term)

    dd = BaseElement(tag="dd")
    dd.get_html(content=definition)

    dl.add_element(dt)
    dl.add_element(dd)
```

### Dynamic list creation from data

```python
from layoutml import UnorderedList, Anchor

def create_nav_list(items):
    """Creates a navigation list from data"""
    nav = UnorderedList(class_="dynamic-nav")

    for item in items:
        if isinstance(item, dict):
            link = Anchor(
                href=item.get("url", "#"),
                text=item.get("title", "Link")
            )
            nav.add_item(link)
        else:
            nav.add_item(str(item))

    return nav

# Menu data
menu_items = [
    {"title": "Home", "url": "/"},
    {"title": "Products", "url": "/products"},
    {"title": "About", "url": "/about"},
    {"title": "Contact", "url": "/contact"}
]

# Create menu
main_menu = create_nav_list(menu_items)
```
