# OrderedList

`OrderedList` is a specialized class for creating HTML ordered lists <ol>. The class inherits from [ListElement](ListElement.md) and is designed for building ordered lists where element order matters (e.g., step-by-step instructions, rankings, top lists).

---

## Import

```python
from layoutML.elements.list import OrderedList
```

## Inheritance

- Parent class: [ListElement](ListElement.md)
- Element type: ol (ordered list)
- Purpose: Creating numbered lists with automatic item numbering

## Class Attributes

| Attribute   | Type | Description                             | Default value        |
| ----------- | ---- | --------------------------------------- | -------------------- |
| items       | list | List items (inherited from ListElement) | []                   |
| object_type | str  | Object type                             | "OrderedListElement" |

## Constructor

### **init**(items=None, object_name=None, style=None, boolean_attributes=[], \*\*kwargs)

Creates a new ordered list with the specified parameters.

Parameters:

- items (list): Initial list items. Default is None
- object_name (optional): Name/identifier of the element
- style (optional): CSS string for inline styles
- boolean_attributes (optional): List of boolean attributes
- \*\*kwargs: Additional HTML attributes (id, class\_, start, reversed, type, etc.)

Automatically set properties:

- Tag: ol
- self_closing: False (not a self-closing tag)
- object_type: "OrderedListElement"
- items: list of elements

Examples:

```python
# Empty list
ol = OrderedList()

# List with items
ol = OrderedList(items=["First", "Second", "Third"])

# List with attributes
ol = OrderedList(
    items=["Step 1", "Step 2", "Step 3"],
    class_="steps",
    start="1",
    type="A",
    id="instruction-list"
)
```

## Core Methods

### add_item(item)

Adds an item to the list. Inherited from ListElement.

```python
ol = OrderedList()

ol.add_item("First item")
ol.add_item("Second item")

from layoutML import Anchor
ol.add_item(Anchor(href="/more", text="Learn more..."))
```

## Special HTML Attributes for OrderedList

| Attribute | Description                 | Example                                       |
| --------- | --------------------------- | --------------------------------------------- |
| start     | Starting number of the list | start="5" (starts from 5)                     |
| reversed  | Reverse numbering order     | reversed                                      |
| type      | Numbering style             | type="A" (letters), type="I" (Roman numerals) |

## Usage Examples

### Simple ordered list

```python
steps = OrderedList(items=[
    "Prepare ingredients",
    "Mix components",
    "Bake for 30 minutes",
    "Cool and serve"
])
```

### List with starting number

```python
top_five = OrderedList(
    items=[
        "Fifth place",
        "Fourth place",
        "Third place",
        "Second place",
        "First place"
    ],
    start="5",
    reversed=True
)
```

### Different numbering styles

```python
letter_list = OrderedList(
    items=["Point A", "Point B", "Point C"],
    type="A"
)

lower_letter_list = OrderedList(
    items=["Point a", "Point b", "Point c"],
    type="a"
)

roman_list = OrderedList(
    items=["Section I", "Section II", "Section III"],
    type="I"
)

lower_roman_list = OrderedList(
    items=["Part i", "Part ii", "Part iii"],
    type="i"
)
```

### Complex content list

```python
from layoutML.elements import Anchor, Span, Image

recipe = OrderedList(class_="recipe-steps")

recipe.add_item("Preheat oven to 180°C")

step2 = Span()
step2.get_html(content="Add <a href='/ingredients/flour'>flour</a> and mix")
recipe.add_item(step2)

step3_container = Span()
step3_container.get_html(content="Place dough into pan: ")

step3_img = Image(
    src="pan.jpg",
    alt="Baking pan",
    style="width: 50px; vertical-align: middle;"
)

step3_container.add_element(step3_img)
recipe.add_item(step3_container)

step4 = Span()
step4.get_html(content="Bake for 30 minutes ")

tip = Span(
    text="(do not open the oven!)",
    class_="tip",
    style="color: #666; font-style: italic;"
)

step4.add_element(tip)
recipe.add_item(step4)
```

### Styled ordered list

```python
ol = OrderedList(
    items=["Item 1", "Item 2", "Item 3"],
    object_name="styledOrderedList",
    class_="custom-list"
)

ol.inline_styles.set_padding_left("30px")\
                .set_margin_bottom("20px")

ol.selectors_styles.add_selector(".custom-list li")\
    .set_margin_bottom("10px")\
    .set_padding("8px 12px")\
    .set_background_color("#f8f9fa")\
    .set_border_radius("4px")

ol.selectors_styles.add_selector(".custom-list li::marker")\
    .set_color("#007bff")\
    .set_font_weight("bold")\
    .set_font_size("1.2em")
```

### Step-by-step tutorial

```python
tutorial = OrderedList(
    class_="tutorial",
    type="1",
    start="1"
)

steps = [
    "Install Python from the official website",
    "Create virtual environment: python -m venv venv",
    "Activate environment",
    "Install dependencies: pip install -r requirements.txt",
    "Run application: python app.py"
]

for step in steps:
    tutorial.add_item(step)

tutorial.object_styles.set_font_family("monospace")\
                      .set_background_color("#f4f4f4")\
                      .set_padding("20px")\
                      .set_border_radius("8px")

tutorial.selectors_styles.add_selector(".tutorial li")\
    .set_margin_bottom("15px")\
    .set_line_height("1.6")
```

### Nested ordered lists

```python
from layoutML.elements.list import OrderedList

main_list = OrderedList(class_="outline")

chapter1 = "Chapter 1: Introduction"
subpoints1 = OrderedList(
    items=[
        "What is web development",
        "Core technologies",
        "Developer tools"
    ],
    type="a"
)

main_list.add_item(chapter1)
main_list.add_item(subpoints1)

chapter2 = "Chapter 2: HTML Basics"
subpoints2 = OrderedList(
    items=[
        "HTML structure",
        "Basic tags",
        "Attributes"
    ],
    type="a"
)

main_list.add_item(chapter2)
main_list.add_item(subpoints2)

chapter3 = "Chapter 3: CSS Styling"
subpoints3 = OrderedList(
    items=[
        "Selectors",
        "Properties",
        "Responsive design"
    ],
    type="a"
)

main_list.add_item(chapter3)
main_list.add_item(subpoints3)
```

### Top list with descriptions

```python
top_list = OrderedList(
    class_="top-list",
    start="1"
)

top_items = [
    {"title": "Python", "description": "General-purpose beginner-friendly language"},
    {"title": "JavaScript", "description": "Language for web development"},
    {"title": "Java", "description": "Enterprise applications language"},
    {"title": "C++", "description": "High-performance systems language"},
    {"title": "Go", "description": "Modern language from Google"}
]

for item in top_items:
    container = BaseElement(tag="div")

    title = BaseElement(tag="strong")
    title.get_html(content=item["title"])

    description = BaseElement(tag="span")
    description.get_html(content=f" - {item['description']}")

    container.add_element(title)
    container.add_element(description)

    top_list.add_item(container)

top_list.selectors_styles.add_selector(".top-list li")\
    .set_margin_bottom("15px")\
    .set_padding("10px")\
    .set_background_color("#f8f9fa")\
    .set_border_radius("5px")

top_list.selectors_styles.add_selector(".top-list li::marker")\
    .set_color("#dc3545")\
    .set_font_size("1.3em")\
    .set_font_weight("bold")
```

### Custom numbered list (CSS-based)

```python
custom_ol = OrderedList(
    items=[
        "Important achievement",
        "Very important achievement",
        "Critical achievement"
    ],
    class_="achievements"
)

custom_ol.selectors_styles.add_selector(".achievements")\
    .set_counter_reset("achievement-counter")

custom_ol.selectors_styles.add_selector(".achievements li")\
    .set_counter_increment("achievement-counter")\
    .set_list_style_type("none")\
    .set_position("relative")\
    .set_padding_left("30px")

custom_ol.selectors_styles.add_selector(".achievements li::before")\
    .set_content("'🏆 ' counter(achievement-counter) '. '")\
    .set_position("absolute")\
    .set_left("0")\
    .set_color("#ffc107")\
    .set_font_weight("bold")
```

### Sidebar list

```python
from layoutML.elements import Aside

sidebar = Aside(class_="sidebar")

sidebar_title = BaseElement(tag="h3")
sidebar_title.get_html(content="Popular Articles")

popular_articles = OrderedList(
    class_="popular-list",
    type="1"
)

articles = [
    ("Best web development practices", "/articles/best-practices"),
    ("Learn Python in one month", "/articles/learn-python"),
    ("React basics for beginners", "/articles/react-basics"),
    ("Modern CSS: Grid and Flexbox", "/articles/css-grid-flex")
]

for title, url in articles:
    link = Anchor(href=url, text=title, class_="article-link")
    popular_articles.add_item(link)

sidebar.add_element(sidebar_title)
sidebar.add_element(popular_articles)

popular_articles.selectors_styles.add_selector(".popular-list li")\
    .set_margin_bottom("10px")

popular_articles.selectors_styles.add_selector(".popular-list a")\
    .set_color("#333")\
    .set_text_decoration("none")\
    .set_transition("color 0.3s")

popular_articles.selectors_styles.add_selector(".popular-list a:hover")\
    .set_color("#007bff")
```
