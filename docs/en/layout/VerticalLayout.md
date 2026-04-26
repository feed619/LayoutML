# VerticalLayout

`VerticalLayout` is a specialized class for creating vertical layouts using Flexbox. It inherits from the base class [Layout](Layout.md) and is designed to arrange elements in a column. It is ideal for forms, lists, navigation panels, and other vertically structured interfaces.

---

## Inheritance

- Parent class: Layout
- Direction: Vertical (`flex-direction: column`)
- Specialization: Manages elements in a column with optional reverse ordering
- Additional: Automatically sets `box-sizing: border-box` for correct size calculations

---

## Class Attributes

| Attribute                       | Type | Description                           | Inheritance                     |
| ------------------------------- | ---- | ------------------------------------- | ------------------------------- |
| object_type                     | str  | Object type (always "VerticalLayout") | Overridden                      |
| object_styles["flex-direction"] | str  | Element direction                     | Inherited but fixed as "column" |
| object_styles["box-sizing"]     | str  | Box sizing model                      | New                             |
| All other attributes            | —    | Inherited from Layout                 | Layout                          |

---

## Constructor

### **init**(justify_content="center", align_items="center", object_name=None, \*\*kwargs)

Creates a new vertical layout with specified alignment settings.

Parameters:

- justify_content (str): Main axis alignment (vertical). Default is `"center"`
- align_items (str): Cross-axis alignment (horizontal). Default is `"center"`
- object_name (optional): Name/identifier of the layout
- \*\*kwargs: Additional HTML element attributes

Automatically applied properties:

- Inherits all Layout properties
- `flex-direction: column` (vertical layout)
- `box-sizing: border-box` (for correct sizing behavior)
- `object_type: "VerticalLayout"`

Important:  
In a vertical layout, `justify_content` controls vertical alignment, while `align_items` controls horizontal alignment.

### Examples:

```python
# Simple vertical layout
v_layout = VerticalLayout()

# Sidebar layout with custom alignment
sidebar = VerticalLayout(
    object_name="sidebar",
    justify_content="flex-start",  # Align items to top
    align_items="stretch",         # Full width elements
    class_="navigation-sidebar"
)

# Form container
form_container = VerticalLayout(
    object_name="signupForm",
    justify_content="center",
    align_items="stretch",
    id="signup-form",
    data_role="form-container"
)
```

---

## Main Methods

### set_reverse(reverse: bool = True) -> "VerticalLayout"

Sets the reverse direction of elements in the column.

Parameters:

- reverse (bool): If True → elements are arranged bottom-to-top (`column-reverse`), otherwise top-to-bottom (`column`). Default is True

Returns:

- The VerticalLayout instance for method chaining

### Examples:

```python
layout = VerticalLayout()

# Normal direction (top to bottom)
layout.set_reverse(False)
print(layout.object_styles["flex-direction"])  # "column"

# Reverse direction (bottom to top)
layout.set_reverse(True)
print(layout.object_styles["flex-direction"])  # "column-reverse"
```

---

## Inherited Methods

VerticalLayout inherits all methods from Layout, including:

### Size control:

- stretch(fullscreen: bool = True) -> "Layout" — stretch layout
- unstretch() -> "Layout" — remove stretching
- set_size(width: str = None, height: str = None) -> "Layout" — set dimensions

### Element management:

- add_element(element: Any) -> "Layout" — add a single element
- add_elements(\*elements: Any) -> "Layout" — add multiple elements
- clear() -> "Layout" — remove all elements
- insert_element(index: int, element: Any) -> "Layout" — insert element
- remove_element(index: int) -> "Layout" — remove element

### Rendering:

- get_html() -> str — generate HTML
- get_styles() -> dict — collect CSS styles

### Python special methods:

- **len**() -> int — number of elements
- **getitem**(index: int) -> Any — get element by index
- **setitem**(index: int, element: Any) -> None — replace element
- **delitem**(index: int) -> None — delete element
