# Label

`Label` is a specialized class for creating the HTML label element <label>. The class inherits from [BaseElement](../base/BaseElement.md) and is intended for creating text labels associated with form elements, improving accessibility and usability of web forms.

---

## Import

```python
from layoutML.elements import Label
```

## Inheritance

- Parent class: BaseElement
- Element type: label (non-self-closing tag)
- Purpose: Creating labels for form elements

## Constructor

### **init**(for_id=None, text="", object_name=None, style=None, boolean_attributes=[], \*\*kwargs)

Creates a new label element with the specified parameters.

### Parameters:

- for_id (str): Identifier of the form element the label is associated with. Defaults to None
- text (str): Label text. Defaults to empty string
- object_name (optional): Element name/identifier
- style (optional): CSS string for inline styles
- boolean_attributes (optional): List of boolean attributes
- \*_kwargs: Additional HTML attributes (class\_, aria-_, etc.)

### Automatically assigned properties:

- Tag: label
- self_closing: False (non-self-closing tag)
- object_type: "LabelElement"
- text: label text
- for_id: identifier of the associated form element

### Examples:

```python
# Simple label
label = Label(text="Username")

# Label associated with an input field
label = Label(
    for_id="username-field",
    text="Username",
    class_="form-label"
)

# Label with inline styles
label = Label(
    text="Email address",
    style="font-weight: bold; color: #333;",
    aria_label="Email input field"
)
```

## Usage Examples

### Basic labels

```python
# Basic label
label1 = Label(text="Username")

# Label with class
label2 = Label(
    text="Email",
    class_="form-label required"
)

# Label with identifier
label3 = Label(
    text="Password",
    id="password-label",
    for_id="password-field"
)
```

### Labels for different input types

```python
from layoutml import Input

# Label for text input
text_label = Label(
    for_id="username",
    text="Username:",
    class_="field-label"
)

text_input = Input(id="username", placeholder="Enter name")

# Label for email input
email_label = Label(
    for_id="user-email",
    text="Email address:",
    class_="field-label required"
)

email_input = Input(
    input_type="email",
    id="user-email",
    placeholder="user@example.com"
)

# Label for checkbox
checkbox_label = Label(
    for_id="agree-terms",
    text="I agree to the terms"
)

checkbox_input = Input(
    input_type="checkbox",
    id="agree-terms",
    value="yes"
)
```
