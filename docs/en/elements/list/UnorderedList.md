# UnorderedList

`UnorderedList` is a specialized class for creating HTML bulleted (unordered) lists <ul>. The class inherits from [ListElement](ListElement.md) and is intended for creating lists where the order of elements does not matter (e.g., product lists, menus, categories, features).

---

## Import

```python
from layoutML.elements.list import UnorderedList
```

## Inheritance

- Parent class: [ListElement](ListElement.md)
- Element type: ul (unordered list)
- Purpose: Creating bulleted lists with markers (dots, circles, squares)

## Class Attributes

| Attribute   | Type | Description                             | Default value          |
| ----------- | ---- | --------------------------------------- | ---------------------- |
| items       | list | List items (inherited from ListElement) | []                     |
| object_type | str  | Object type                             | "UnorderedListElement" |

## Constructor

### **init**(items=None, object_name=None, style=None, boolean_attributes=[], \*\*kwargs)

Creates a new unordered list with the specified parameters.

Parameters:

- items (list): Initial list items. Default is None
- object_name (optional): Name/identifier of the element
- style (optional): CSS string for inline styles
- boolean_attributes (optional): List of boolean attributes
- \*_kwargs: Additional HTML attributes (id, class\_, aria-_, etc.)

Automatically set properties:

- Tag: ul
- self_closing: False (not a self-closing tag)
- object_type: "UnorderedListElement"
- items: list of elements

Examples:

```python
# Empty list
ul = UnorderedList()

# List with items
ul = UnorderedList(items=["Apple", "Banana", "Orange"])

# List with attributes
ul = UnorderedList(
    items=["Home", "About", "Contact"],
    class_="nav-menu",
    id="main-menu",
    aria_label="Main navigation menu"
)
```

## Core Methods

### add_item(item)

Adds an item to the list. Inherited from ListElement.

```python
ul = UnorderedList()

ul.add_item("First item")
ul.add_item("Second item")

from layoutML import Anchor
ul.add_item(Anchor(href="/more", text="Learn more..."))
```

## Usage Examples

### Simple unordered list

```python
fruits = UnorderedList(items=["Apple", "Banana", "Orange", "Pear"])

features = UnorderedList(
    items=[
        "Free delivery",
        "Quality guarantee",
        "24/7 support"
    ],
    class_="features-list"
)
```

### Navigation menu

```python
from layoutML.elements import Anchor

nav_menu = UnorderedList(class_="main-nav")

menu_items = [
    ("Home", "/"),
    ("About", "/about"),
    ("Services", "/services"),
    ("Blog", "/blog"),
    ("Contact", "/contact")
]

for text, url in menu_items:
    link = Anchor(href=url, text=text, class_="nav-link")
    nav_menu.add_item(link)

nav_menu.object_styles.set_display("flex")\
                      .set_list_style_type("none")\
                      .set_padding("0")\
                      .set_margin("0")\
                      .set_gap("20px")
```

### List with icons

```python
icon_list = UnorderedList(class_="icon-list")

items_with_icons = [
    ("✓", "High quality"),
    ("🚀", "Fast delivery"),
    ("💎", "Best price"),
    ("🛡️", "Money-back guarantee")
]

for icon, text in items_with_icons:
    item_content = BaseElement(tag="span")
    item_content.get_html(content=f"{icon} {text}")
    icon_list.add_item(item_content)

icon_list.selectors_styles.add_selector(".icon-list")\
    .set_list_style_type("none")\
    .set_padding_left("0")

icon_list.selectors_styles.add_selector(".icon-list li")\
    .set_padding("8px 0")\
    .set_font_size("16px")
```

### Styled list with custom markers

```python
styled_ul = UnorderedList(
    items=[
        "Learn Python basics",
        "Practice daily",
        "Build a portfolio",
        "Get first job"
    ],
    class_="todo-list"
)

styled_ul.selectors_styles.add_selector(".todo-list")\
    .set_list_style_type("none")\
    .set_padding_left("0")

styled_ul.selectors_styles.add_selector(".todo-list li")\
    .set_padding("8px 0 8px 30px")\
    .set_position("relative")

styled_ul.selectors_styles.add_selector(".todo-list li::before")\
    .set_content("'✓ '")\
    .set_position("absolute")\
    .set_left("0")\
    .set_color("#28a745")\
    .set_font_weight("bold")
```

### Nested lists

```python
main_list = UnorderedList(class_="categories")

main_list.add_item("Fruits")

fruits_sublist = UnorderedList(
    items=["Apples", "Bananas", "Oranges", "Pears"],
    class_="sub-list"
)

main_list.add_item(fruits_sublist)

main_list.add_item("Vegetables")

vegetables_sublist = UnorderedList(
    items=["Tomatoes", "Cucumbers", "Carrots", "Onions"],
    class_="sub-list"
)

main_list.add_item(vegetables_sublist)

main_list.selectors_styles.add_selector(".sub-list")\
    .set_margin_top("5px")\
    .set_margin_left("20px")\
    .set_list_style_type("circle")
```

### Product feature list

```python
product_features = UnorderedList(class_="product-specs")

specs = [
    ("Processor", "Intel Core i7-12700K"),
    ("RAM", "32 GB DDR5"),
    ("GPU", "NVIDIA RTX 4080"),
    ("Storage", "1 TB NVMe SSD"),
    ("OS", "Windows 11 Pro")
]

for spec_name, spec_value in specs:
    spec_item = BaseElement(tag="span")
    spec_item.get_html(content=f"<strong>{spec_name}:</strong> {spec_value}")
    product_features.add_item(spec_item)

product_features.selectors_styles.add_selector(".product-specs li")\
    .set_margin_bottom("8px")\
    .set_padding("5px")\
    .set_border_bottom("1px solid #eee")
```

### List with links and descriptions

```python
from layoutML import Anchor, Span

resource_list = UnorderedList(class_="resources")

resources = [
    {"title": "Python Docs", "url": "https://docs.python.org", "desc": "Official documentation"},
    {"title": "Stack Overflow", "url": "https://stackoverflow.com", "desc": "Developer Q&A"},
    {"title": "GitHub", "url": "https://github.com", "desc": "Code hosting platform"},
    {"title": "MDN Web Docs", "url": "https://developer.mozilla.org", "desc": "Web technology docs"}
]

for resource in resources:
    item_container = BaseElement(tag="div")

    link = Anchor(
        href=resource["url"],
        text=resource["title"],
        target="_blank"
    )

    desc = Span(
        text=f" - {resource['desc']}",
        class_="description"
    )

    item_container.add_element(link)
    item_container.add_element(desc)

    resource_list.add_item(item_container)

resource_list.selectors_styles.add_selector(".resources li")\
    .set_margin_bottom("12px")

resource_list.selectors_styles.add_selector(".resources .description")\
    .set_color("#666")\
    .set_font_size("0.9em")
```

### Horizontal menu

```python
horizontal_menu = UnorderedList(
    items=[
        Anchor(href="/", text="Home"),
        Anchor(href="/catalog", text="Catalog"),
        Anchor(href="/about", text="About"),
        Anchor(href="/contact", text="Contact")
    ],
    class_="horizontal-nav"
)

horizontal_menu.object_styles.set_display("flex")\
                             .set_list_style_type("none")\
                             .set_padding("0")\
                             .set_margin("0")\
                             .set_gap("30px")

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

### List with badges

```python
notification_list = UnorderedList(class_="notifications")

notifications = [
    {"text": "New message from Ivan", "badge": "2", "color": "#dc3545"},
    {"text": "System update ready", "badge": "1", "color": "#28a745"},
    {"text": "Backup completed", "badge": "✓", "color": "#17a2b8"}
]

for notif in notifications:
    item_container = BaseElement(tag="div", class_="notification-item")

    text = Span(text=notif["text"])

    badge = Span(
        text=str(notif["badge"]),
        class_="badge",
        style=f"background-color: {notif['color']}; color: white; padding: 2px 8px; border-radius: 12px; margin-left: 10px; font-size: 12px;"
    )

    item_container.add_element(text)
    item_container.add_element(badge)

    notification_list.add_item(item_container)

notification_list.selectors_styles.add_selector(".notifications li")\
    .set_padding("10px")\
    .set_border_bottom("1px solid #eee")

notification_list.selectors_styles.add_selector(".notifications li:hover")\
    .set_background_color("#f8f9fa")
```

### Sidebar list

```python
from layoutML.elements import Aside

sidebar = Aside(class_="sidebar")

sidebar_title = BaseElement(tag="h3")
sidebar_title.get_html(content="Categories")

categories = UnorderedList(class_="categories-list")

category_links = [
    ("Electronics", "/category/electronics", 25),
    ("Clothing", "/category/clothing", 18),
    ("Books", "/category/books", 12),
    ("Sports", "/category/sports", 8),
    ("Toys", "/category/toys", 15)
]

for cat_name, cat_url, count in category_links:
    link_container = BaseElement(tag="span")

    link = Anchor(href=cat_url, text=cat_name)
    count_span = Span(
        text=f" ({count})",
        class_="count",
        style="color: #666; font-size: 0.9em;"
    )

    link_container.add_element(link)
    link_container.add_element(count_span)

    categories.add_item(link_container)

sidebar.add_element(sidebar_title)
sidebar.add_element(categories)

categories.selectors_styles.add_selector(".categories-list")\
    .set_list_style_type("none")\
    .set_padding_left("0")

categories.selectors_styles.add_selector(".categories-list li")\
    .set_margin_bottom("10px")

categories.selectors_styles.add_selector(".categories-list a")\
    .set_color("#333")\
    .set_text_decoration("none")\
    .set_display("block")\
    .set_padding("5px")\
    .set_border_radius("4px")

categories.selectors_styles.add_selector(".categories-list a:hover")\
    .set_background_color("#007bff")\
    .set_color("white")
```
