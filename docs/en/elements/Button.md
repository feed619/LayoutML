# Button

`Button` is a specialized class for creating HTML buttons (<button>). The class inherits from [BaseElement](../base/BaseElement.md) and provides a simplified interface for creating buttons with text, styles, and attributes.

---

## Import

```python
from layoutML.elements import Button
```

## Inheritance

- Parent class: BaseElement
- Element type: button (non-self-closing tag)
- Purpose: Creating interactive buttons for forms, navigation, and actions

## Constructor

### **init**(text="", object_name=None, style=None, boolean_attributes=[], \*\*kwargs)

Creates a new button element with the specified text and attributes.

Parameters:

- text (str): Button text (displayed between tags). Defaults to empty string
- object_name (optional): Element name/identifier
- style (optional): CSS string for inline styles
- boolean_attributes (optional): List of boolean attributes (disabled, readonly, etc.)
- \*\*kwargs: Additional HTML attributes (type, onclick, id, class\_, etc.)

Automatically assigned properties:

- Tag: button
- self_closing: False (non-self-closing tag)
- object_type: "ButtonElement"
- text: button text

## Examples:

## Example 1: Basic buttons

```python
# Simple text button
simple_btn = Button(text="Click me")

# Button with type
submit_btn = Button(
    text="Submit",
    type="submit",
    class_="btn-submit"
)

reset_btn = Button(
    text="Reset",
    type="reset",
    class_="btn-reset"
)

# Button with JavaScript handler
action_btn = Button(
    text="Execute",
    onclick="doAction()",
    onmouseover="this.style.backgroundColor='yellow'"
)

# Button with data attributes
data_btn = Button(
    text="Delete",
    data_action="delete",
    data_id="123",
    data_confirm="Are you sure?"
)
```

## Example 2: Styled buttons with CSS

```python
# Creating a button with CSS classes
btn = Button(
    text="Styled button",
    object_name="fancyBtn",
    class_="btn btn-primary btn-large"
)

# Adding inline styles
btn.inline_styles.set_padding("10px 20px")\
                 .set_font_size("16px")\
                 .set_border_radius("5px")\
                 .set_cursor("pointer")

# Adding CSS styles via object_styles
btn.object_styles.set_background_color("#4CAF50")\
                 .set_color("white")\
                 .set_border("none")\
                 .set_transition("background-color 0.3s")

# Adding effects via selectors_styles
btn.selectors_styles.add_selector("fancyBtn:hover")\
    .set_background_color("#45a049")

btn.selectors_styles.add_selector("fancyBtn:active")\
    .set_transform("scale(0.98)")
```
