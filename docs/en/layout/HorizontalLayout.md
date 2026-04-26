# HorizontalLayout

`HorizontalLayout` is a specialized class for creating horizontal layouts using Flexbox. It inherits from the base class [Layout](Layout.md) and provides additional methods for controlling horizontal element arrangement.

---

## Inheritance

- Parent class: Layout
- Direction: Horizontal (`flex-direction: row`)
- Specialization: Manages elements in a row with optional reverse ordering

---

## Class Attributes

| Attribute                       | Type | Description                             | Inheritance                  |
| ------------------------------- | ---- | --------------------------------------- | ---------------------------- |
| object_type                     | str  | Object type (always "HorizontalLayout") | Overridden                   |
| object_styles["flex-direction"] | str  | Direction of elements (row/row-reverse) | Inherited but fixed as "row" |
| All other attributes            | —    | Inherited from Layout                   | Layout                       |

---

## Constructor

### **init**(justify_content="center", align_items="center", object_name=None, \*\*kwargs)

Creates a new horizontal layout with specified alignment settings.

Parameters:

- justify_content (str): Main axis alignment (horizontal). Default is `"center"`
- align_items (str): Cross-axis alignment (vertical). Default is `"center"`
- object_name (optional): Name/identifier of the layout
- \*\*kwargs: Additional HTML element attributes

Automatically applied properties:

- Inherits all Layout properties
- `flex-direction: row` (horizontal layout)
- `object_type: "HorizontalLayout"`

### Examples:

```python
# Simple horizontal layout
h_layout = HorizontalLayout()

# Navigation bar with custom alignment
nav_bar = HorizontalLayout(
    object_name="navbar",
    justify_content="space-between",
    align_items="center",
    class_="navigation"
)

# Toolbar with additional attributes
toolbar = HorizontalLayout(
    object_name="mainToolbar",
    justify_content="flex-start",
    align_items="stretch",
    id="toolbar",
    data_role="toolbar"
)
```

---

## Main Methods

### set_reverse(reverse: bool = True) -> "HorizontalLayout"

Sets the direction of element ordering.

Parameters:

- reverse (bool): If True → elements are arranged right-to-left (`row-reverse`), otherwise left-to-right (`row`). Default is True

Returns:

- The HorizontalLayout instance for method chaining

### Examples:

```python
layout = HorizontalLayout()

# Normal direction (left to right)
layout.set_reverse(False)
print(layout.object_styles["flex-direction"])  # "row"

# Reversed direction (right to left)
layout.set_reverse(True)
print(layout.object_styles["flex-direction"])  # "row-reverse"
```

---

## Inherited Methods

HorizontalLayout inherits all methods from Layout, including:

### Size control:

- stretch(fullscreen: bool = True) -> "Layout" — stretch layout
- unstretch() -> "Layout" — remove stretching
- set_size(width: str = None, height: str = None) -> "Layout" — set dimensions

### Element management:

- add_element(element: Any) -> "Layout" — add one element
- add_elements(\*elements: Any) -> "Layout" — add multiple elements
- clear() -> "Layout" — remove all elements
- insert_element(index: int, element: Any) -> "Layout" — insert element
- remove_element(index: int) -> "Layout" — remove element

### Rendering:

- get_html() -> str — generate HTML output
- get_styles() -> dict — collect CSS styles

### Python magic methods:

- **len**() -> int — number of elements
- **getitem**(index: int) -> Any — get element by index
- **setitem**(index: int, element: Any) -> None — replace element
- **delitem**(index: int) -> None — delete element
