# FormTypes

`FormTypes` contains constants for all possible HTML form input field types defined in the HTML5 specification. This class provides a centralized and type-safe storage for form element types, simplifying development and preventing errors caused by string literals.

---

## Import

```python
# Import the entire class
from LayoutML.types import FormTypes

# Using constants
text_field = Form(form_type=FormTypes.TEXT)
email_field = Form(form_type=FormTypes.EMAIL)
submit_button = Form(form_type=FormTypes.SUBMIT)
```

## Full Constant Reference

### Text Fields

| Constant | Value      | Description                              |
| -------- | ---------- | ---------------------------------------- |
| TEXT     | "text"     | Standard single-line text input field    |
| PASSWORD | "password" | Password input field (characters hidden) |
| EMAIL    | "email"    | Email address input field                |
| NUMBER   | "number"   | Numeric input field                      |
| TEL      | "tel"      | Telephone number input field             |
| URL      | "url"      | URL input field                          |
| SEARCH   | "search"   | Search query input field                 |

### Selection Elements

| Constant | Value      | Description                       |
| -------- | ---------- | --------------------------------- |
| CHECKBOX | "checkbox" | Checkbox for multiple selection   |
| RADIO    | "radio"    | Radio button for single selection |
| SELECT   | "select"   | Dropdown selection list           |
| DATALIST | "datalist" | Autocomplete suggestion list      |

### Special Fields

| Constant       | Value            | Description                      |
| -------------- | ---------------- | -------------------------------- |
| DATE           | "date"           | Date picker (calendar)           |
| TIME           | "time"           | Time picker                      |
| DATETIME_LOCAL | "datetime-local" | Date and time picker             |
| MONTH          | "month"          | Month and year picker            |
| WEEK           | "week"           | Week picker                      |
| COLOR          | "color"          | Color picker                     |
| RANGE          | "range"          | Slider for selecting a value     |
| FILE           | "file"           | File upload field                |
| HIDDEN         | "hidden"         | Hidden input field (not visible) |
| TEXTAREA       | "textarea"       | Multi-line text input            |

### Buttons

| Constant | Value    | Description            |
| -------- | -------- | ---------------------- |
| SUBMIT   | "submit" | Form submission button |
| RESET    | "reset"  | Form reset button      |
| BUTTON   | "button" | Generic button         |
| IMAGE    | "image"  | Image-based button     |

---

## Characteristics of Each Type

### Text Field Characteristics

#### FormTypes.TEXT

- Default type for general text input
- Recommended to use `maxlength` and `minlength` for validation
- Supports `pattern` for regular expression validation

#### FormTypes.EMAIL

- Automatically validates email format
- On mobile devices, shows a keyboard optimized for email input (@ included)
- Recommended to use `autocomplete="email"`

#### FormTypes.PASSWORD

- Characters are masked (dots or asterisks)
- Use `autocomplete="new-password"` for new passwords
- Use `autocomplete="current-password"` for existing passwords

#### FormTypes.NUMBER

- Accepts only numeric input
- Use `min`, `max`, and `step` for constraints
- Shows numeric keyboard on mobile devices

---

### Selection Element Characteristics

#### FormTypes.CHECKBOX

- Allows multiple selections
- Requires a `value` attribute
- Use `checked` for default selection

#### FormTypes.RADIO

- Only one option can be selected per group (same `name`)
- Requires a `value` attribute
- Use `checked` for default selection

#### FormTypes.SELECT

- Used for dropdown lists
- Use `multiple` for multi-selection
- Use `size` to define visible options

---

### Special Field Characteristics

#### Date/Time Inputs (DATE, TIME, etc.)

- Modern browsers provide specialized UI pickers
- Value format depends on the type
- Use `min` and `max` to restrict range

#### FormTypes.FILE

- Opens file selection dialog
- Use `accept` to restrict file types
- Use `multiple` for selecting multiple files
- Use `capture` for camera access on mobile devices

#### FormTypes.RANGE

- Creates a slider input
- Use `min`, `max`, and `step` for configuration
- Does not display current value by default (requires JavaScript)

---

### Button Characteristics

#### FormTypes.SUBMIT

- Submits the form
- Supports attributes like `formaction`, `formenctype`, `formmethod`, `formtarget`
- Validates the form before submission by default

#### FormTypes.IMAGE

- Image-based submit button
- Requires `src` and `alt` attributes
- Sends click coordinates (x, y) upon submission
