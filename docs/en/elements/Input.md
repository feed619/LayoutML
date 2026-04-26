# Input

`Input` is a specialized class for creating HTML input elements <input>. The class inherits from [Form](Form.md) and provides a convenient interface for creating input fields with commonly used attributes such as placeholder, value, name, and id.

---

## Import

```python
from layoutML.elements import Input
```

## Inheritance

- Parent class: Form (which inherits from BaseElement)
- Element type: input (self-closing tag)
- Purpose: Creating input fields for forms

## Constructor

### **init**(input_type="text", placeholder="", value="", name=None, id=None, object_name=None, style=None, boolean_attributes=[], \*\*kwargs)

Creates a new input element with the specified parameters.

### Parameters:

- input_type (str): Type of input field. Defaults to "text"
- placeholder (str): Placeholder text inside the field. Defaults to empty string
- value (str): Field value. Defaults to empty string
- name (str): Field name for form submission. Defaults to None
- id (str): Unique field identifier. Defaults to None
- object_name (optional): Element name/identifier
- style (optional): CSS string for inline styles
- boolean_attributes (optional): List of boolean attributes (disabled, readonly, required, etc.)
- \*\*kwargs: Additional HTML attributes

### Automatically assigned properties:

- Tag: input
- self_closing: True (self-closing tag)
- object_type: "InputElement"
- form_type: value of input_type parameter (passed to parent class)
- placeholder: placeholder text
- value: field value
- name: field name
- id: field identifier

## Examples:

```python
# Simple text field
input_text = Input(placeholder="Enter name")

# Full-featured input field
input_email = Input(
    input_type="email",
    placeholder="Your email",
    value="user@example.com",
    name="user_email",
    id="email-field",
    class_="form-input",
    required=True
)

# Input with inline styles
input_search = Input(
    input_type="search",
    placeholder="Search...",
    style="padding: 10px; border-radius: 5px;",
    aria_label="Search field"
)
```

## Supported input types

The Input class supports all standard HTML5 input types via the input_type parameter:

| Type             | Description                            |
| ---------------- | -------------------------------------- |
| "text"           | Single-line text field (default)       |
| "password"       | Password field (characters are hidden) |
| "email"          | Email address field                    |
| "number"         | Numeric input field                    |
| "tel"            | Telephone number field                 |
| "url"            | URL input field                        |
| "search"         | Search field                           |
| "date"           | Date picker                            |
| "time"           | Time picker                            |
| "datetime-local" | Local date and time picker             |
| "month"          | Month picker                           |
| "week"           | Week picker                            |
| "color"          | Color picker                           |
| "range"          | Slider control                         |
| "file"           | File upload field                      |
| "checkbox"       | Checkbox                               |
| "radio"          | Radio button                           |
| "hidden"         | Hidden input field                     |

## Examples

### Different input types

```python
# Date input
date_field = Input(
    input_type="date",
    name="birth_date",
    min="1900-01-01",
    max="2026-12-31"
)

# Color input
color_field = Input(
    input_type="color",
    name="theme_color",
    value="#007bff"
)

# Range slider
range_field = Input(
    input_type="range",
    name="volume",
    min="0",
    max="100",
    value="50",
    step="5"
)

# File upload
file_field = Input(
    input_type="file",
    name="document",
    accept=".pdf,.doc,.docx",
    multiple=True
)
```

## Inputs with validation

```python
# Email with validation
email_field = Input(
    input_type="email",
    placeholder="user@example.com",
    name="email",
    required=True,
    pattern="[a-z0-9._%+-]+@[a-z0-9.-]+\\.[a-z]{2,}$",
    title="Enter a valid email address"
)

# Number with constraints
quantity_field = Input(
    input_type="number",
    placeholder="Quantity",
    name="quantity",
    min="1",
    max="100",
    step="1",
    required=True
)

# URL with validation
url_field = Input(
    input_type="url",
    placeholder="https://example.com",
    name="website",
    pattern="https?://.+"
)
```
