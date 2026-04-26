# Select

`Select` is a specialized class for creating the HTML dropdown element <select>. The class inherits from [BaseElement](../base/BaseElement.md) and provides a convenient interface for creating option lists, managing selected values, and generating corresponding <option> HTML tags.

---

## Import

```python
from layoutML.elements import Select
```

## Inheritance

- Parent class: BaseElement
- Element type: select (non-self-closing tag)
- Purpose: Creating dropdown lists for forms

## Constructor

### **init**(options=None, selected_value=None, name=None, id=None, object_name=None, style=None, boolean_attributes=[], \*\*kwargs)

Creates a new dropdown element with the specified parameters.

### Parameters:

- options (list): List of options in dictionary or tuple format. Defaults to None
- selected_value (str): Default selected option value. Defaults to None
- name (str): Field name for form submission. Defaults to None
- id (str): Unique field identifier. Defaults to None
- object_name (optional): Element name/identifier
- style (optional): CSS string for inline styles
- boolean_attributes (optional): List of boolean attributes (required, disabled, multiple)
- \*\*kwargs: Additional HTML attributes

### Automatically assigned properties:

- Tag: select
- self_closing: False (non-self-closing tag)
- object_type: "SelectElement"
- options: list of options
- selected_value: selected value
- name: field name
- id: field identifier

## Examples:

```python
# Empty select
select = Select()

# Select with options
select = Select(
    options=[
        {"value": "1", "text": "Option 1"},
        {"value": "2", "text": "Option 2"},
        {"value": "3", "text": "Option 3"}
    ],
    name="choice",
    id="select-choice"
)

# Select with default selected value
select = Select(
    options=[
        {"value": "ru", "text": "Russian"},
        {"value": "en", "text": "English"},
        {"value": "es", "text": "Spanish"}
    ],
    selected_value="ru",
    name="language",
    required=True
)
```

## Main methods

### add_option(value, text, selected=False)

Adds a new option to the dropdown list.

Parameters:

- value (str): Option value (sent to server)
- text (str): Display text for the user
- selected (bool): Whether this option is selected by default

```python
select = Select(name="country")
select.add_option("ru", "Russia")
select.add_option("us", "USA")
select.add_option("cn", "China", selected=True)  # China selected by default
```

## Usage examples

### Simple dropdown list

```python
# Country selector
country_select = Select(
    name="country",
    id="country",
    class_="form-select"
)

countries = [
    ("ru", "Russia"),
    ("us", "USA"),
    ("gb", "United Kingdom"),
    ("de", "Germany"),
    ("fr", "France")
]

for value, text in countries:
    country_select.add_option(value, text)
```

### Select with default value

```python
# Language selector with default Russian
language_select = Select(
    name="language",
    selected_value="ru",
    required=True
)

languages = [
    {"value": "ru", "text": "Russian"},
    {"value": "en", "text": "English"},
    {"value": "es", "text": "Spanish"},
    {"value": "de", "text": "German"},
    {"value": "fr", "text": "French"}
]

for lang in languages:
    language_select.add_option(lang["value"], lang["text"])
```
