# Layout

`Layout` is a specialized container class for creating flexible layouts based on Flexbox. It inherits from [BaseElement](../base/BaseElement.md) and provides a convenient interface for managing element composition with automatic HTML and CSS generation.

---

## Inheritance

- Parent class: BaseElement
- Element type: div with Flexbox
- Purpose: Container for organizing child elements

## Class Attributes

| Attribute     | Type              | Description                    | Inheritance |
| ------------- | ----------------- | ------------------------------ | ----------- |
| elements      | List[BaseElement] | List of child elements         | New         |
| is_stretched  | bool              | Stretched state flag           | New         |
| object_type   | str               | Object type (always "Layout")  | Overridden  |
| object_styles | CSSBase           | Layout styles (inherited) From | BaseElement |
| tag           | str               | HTML tag (always "div") From   | BaseElement |

## Constructor

### **init**(object_name=None, justify_content="center", align_items="center", \*\*kwargs)

Creates a new layout container with Flexbox settings.

Parameters:

- object_name (optional): Layout name/identifier
- justify_content (str): Main axis alignment. Default is `"center"`
- align_items (str): Cross axis alignment. Default is `"center"`
- \*\*kwargs: Additional HTML element attributes

Automatically assigned properties:

- Tag: div
- display: flex
- flex-direction: row
- flex-wrap: nowrap
- background: transparent

### Examples:

```python
from layoutml.layout import Layout
# Simple layout
layout = Layout()
# Layout with name and alignment settings
header_layout = Layout(
    object_name="headerLayout",
    justify_content="space-between",
    align_items="center",
    class_="container"
)
# Layout with additional attributes
main_layout = Layout(
    object_name="mainLayout",
    justify_content="flex-start",
    align_items="stretch",
    id="main",
    data_role="content"
)
```

## Main Methods

### Size Management

#### stretch(fullscreen: bool = True) -> "Layout"

Stretches the layout to full screen or available width.

Parameters:

- fullscreen (bool): If `True` - 100vw x 100vh, if `False` - 100% width

Example:

```python
layout = Layout()
# Full screen
layout.stretch()  # width: 100vw, height: 100vh
# Full available width
layout.stretch(fullscreen=False)  # width: 100%, height: auto
```

#### unstretch() -> "Layout"

Cancels layout stretching.

Example:

```python
layout = Layout()
layout.stretch()
print(layout.is_stretched)  # True
layout.unstretch()
print(layout.is_stretched)  # False
```

#### set_size(width: str = None, height: str = None) -> "Layout"

Sets explicit layout dimensions.

Parameters:

- width (optional): Width (e.g., `"500px"`, `"50%"`, `"100vw"`)
- height (optional): Height (e.g., `"300px"`, `"100vh"`)

Example:

```python
layout = Layout()
# Fixed dimensions
layout.set_size(width="800px", height="600px")
# Percentage dimensions
layout.set_size(width="90%", height="auto")
# Automatic stretched state detection
layout.set_size(width="100vw")  # is_stretched becomes True
```

### Element Management

#### add_element(element: Any) -> "Layout"

Adds a single element to the layout.

Example:

```python
layout = Layout()
button = BaseElement(tag="button", object_name="myButton")
layout.add_element(button)
print(len(layout))  # 1
```

#### add_elements(\*elements: Any) -> "Layout"

Adds multiple elements at once.

Example:

```python
layout = Layout()
button1 = BaseElement(tag="button", object_name="btn1")
button2 = BaseElement(tag="button", object_name="btn2")
div = BaseElement(tag="div", object_name="container")
layout.add_elements(button1, button2, div)
print(len(layout))  # 3
```

#### clear() -> "Layout"

Removes all elements from the layout.

Example:

```python
layout = Layout()
layout.add_elements(button1, button2)
print(len(layout))  # 2
layout.clear()
print(len(layout))  # 0
```

#### insert_element(index: int, element: Any) -> "Layout"

Inserts an element at the specified position.

Example:

```python
layout = Layout()
layout.add_elements(button1, button3)  # [btn1, btn3]
layout.insert_element(1, button2)      # [btn1, btn2, btn3]
```

#### remove_element(index: int) -> "Layout"

Removes an element by index.

Example:

```python
layout = Layout()
layout.add_elements(button1, button2, button3)
layout.remove_element(1)  # Removes button2
```

### remove_element_by_name(object_name: str) -> None

Removes an element by object name.

Parameters:

- object_name (str): Name of the object to remove

```python
layout.remove_element("myButton")
```

### get_element(object_name: str) -> Any

Finds and returns an element by its name.

Parameters:

- object_name (str): Name of the element to find

Returns:

- Found element

Exceptions:

- AttributeError: If the element is not found

```python
element = layout.get_element("submitButton")
```

### HTML and CSS Generation

#### get_html() -> str

Generates the HTML string of the layout with all child elements.

Features:

- Recursively calls `get_html()` on child elements
- Adds indentation for formatting
- Returns the full nested structure

Example:

```python
layout = Layout(object_name="mainLayout")
layout.add_element(BaseElement(tag="p", object_name="text").get_html(content="Hello"))

html = layout.get_html()
# Result:
# <div class="mainLayout" >
#     <p class="text" >Hello</p>
# </div>
```

#### get_styles() -> dict

Collects CSS styles of the layout and all child elements.

Features:

- Recursively collects styles from child elements
- Merges all styles into one dictionary
- Automatically processes nested layouts

Example:

```python
layout = Layout(object_name="container")
layout.object_styles.set_background_color("red")

child = BaseElement(tag="div", object_name="child")
child.object_styles.set_width("100px")

layout.add_element(child)

styles = layout.get_styles()
# Result: {
#   '.container': 'background-color:red;...',
#   '.child': 'width:100px;'
# }
```

### Special Python Methods

#### **len**() -> int

Returns the number of elements in the layout.

```python
layout = Layout()
layout.add_elements(btn1, btn2, btn3)
print(len(layout))  # 3
```

#### **getitem**(index: int) -> Any

Gets an element by index.

```python
layout = Layout()
layout.add_elements(btn1, btn2, btn3)
second_element = layout[1]  # btn2
```

#### **setitem**(index: int, element: Any) -> None

Replaces an element at the specified index.

```python
layout = Layout()
layout.add_elements(btn1, btn2, btn3)
layout[1] = new_button  # Replaces btn2 with new_button
```

#### **delitem**(index: int) -> None

Removes an element at the specified index.

```python
layout = Layout()
layout.add_elements(btn1, btn2, btn3)
del layout[1]  # Removes btn2
```

```

```
