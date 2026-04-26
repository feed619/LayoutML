# Form

`Form` is a specialized class for creating HTML form elements. It inherits from [BaseElement](../base/BaseElement.md) and is designed to simplify the creation of input fields, buttons, and other form elements with automatic type assignment and support for specific form-related attributes.

---

## Import

```python
from layoutML.elements import Form
# Form inherits from HTMLElement, so all its features are available
```

## Inheritance

- Parent class: BaseElement
- Inherits: All methods and attributes of BaseElement and HTMLElement
- Specialization: HTML form elements (<input>, <textarea>, <select>, etc.)

## Class Attributes

| Attribute    | Type | Description                                                | Inheritance |
| ------------ | ---- | ---------------------------------------------------------- | ----------- |
| form_type    | str  | Type of form element (text, email, password, submit, etc.) | New         |
| object_type  | str  | Object type (always "Form")                                | Overridden  |
| tag          | str  | HTML tag (always "input")                                  | BaseElement |
| self_closing | bool | Self-closing tag flag (always True)                        | BaseElement |
| object_name  | str  | Object name                                                | BaseElement |

## Constructor

### **init**(form_type: str = "text", boolean_attributes=[], \*\*kwargs)

Initializes a new form element with the specified parameters.

Parameters:

| Parameter          | Type      | Default | Description                     | Example                              |
| ------------------ | --------- | ------- | ------------------------------- | ------------------------------------ |
| form_type          | str       | "text"  | Type of form element            | "email", "password", "date"          |
| boolean_attributes | list[str] | []      | List of boolean HTML attributes | ["required", "disabled", "readonly"] |
| object_name        | str       | None    | Unique element identifier       | "form_element"                       |
| \*\*kwargs         | dict      | -       | Additional element attributes   | id\_="email", name="user_email"      |

### Constructor features:

- Automatically sets HTML tag to "input"
- Adds a type attribute with the provided form_type value. All possible values are defined in the [FormTypes](../types/FormTypes.md) class
- Inherits all features of the parent HTMLElement class (classes, styles, events, ARIA, data attributes)

### Note: The class also inherits all attributes from HTMLElement:

- class\_ - list of CSS classes
- styles - dictionary of CSS styles
- events - dictionary of event handlers
- value_attributes - dictionary of standard HTML attributes
- custom_attributes - dictionary of custom attributes
- boolean_attributes - list of boolean attributes

## Methods

### get_attributes_string()

Generates a complete attribute string for the HTML tag, combining form-specific attributes with those inherited from the parent class.

Returns:

- str: Attribute string ready for HTML output

Format example:

```text
type="email" class="form-control" id="emailInput" name="email" required placeholder="Enter email" aria-label="Email address" data-validation="email"
```

## Initialization examples:

```python
# Simple text field
text_field = Form(
    form_type="text",
    id="username",
    name="username",
    placeholder="Enter name"
)

# Email field with validation
email_field = Form(
    form_type="email",
    id="user_email",
    name="email",
    required=True,
    pattern="[a-z0-9._%+-]+@[a-z0-9.-]+\\.[a-z]{2,}$"
)

# Password field with additional attributes
password_field = Form(
    form_type="password",
    boolean_attributes=["required"],
    id="user_password",
    name="password",
    minlength="8",
    autocomplete="new-password",
    aria_label="User password"
)

# Checkbox with default state
newsletter_checkbox = Form(
    form_type="checkbox",
    boolean_attributes=["checked"],
    id="subscribe",
    name="newsletter",
    value="yes"
)

# Date field with constraints
birthday_field = Form(
    form_type="date",
    id="birth_date",
    name="birthday",
    min="1900-01-01",
    max="2024-12-31",
    required=True
)

# Creating and rendering elements
text_field = Form(
    form_type="text",
    id="name",
    name="full_name",
    placeholder="Ivan Ivanov"
)

email_field = Form(
    form_type="email",
    id="email",
    name="email",
    required=True
)

submit_button = Form(
    form_type="submit",
    value="Submit",
    class_="btn btn-primary"
)
```
