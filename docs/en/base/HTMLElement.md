# HTMLElement

`HTMLElement` is the base class for creating HTML elements in the LayoutML system. It encapsulates all core HTML element attributes, including classes, styles, events, and standard HTML attributes, providing a convenient object-oriented interface for working with HTML.

The class is designed to generate a correct HTML attribute string and can be used in template engines, HTML generators, or custom UI frameworks.

---

## Import

```python
from LayoutML.base_elements.HTMLElement import HTMLElement
from LayoutML.html_core.HTMLAttributes import ValueAttributes
from LayoutML.html_core.HTMLEvents import MouseEvents, KeyboardEvents, FormEvents, etc.
```

---

## Constructor

### **init**(boolean_attributes=[], \*\*kwargs)

Initializes a new HTML element with the specified attributes.

| Parameter          | Type | Default | Description                          | Example            |
| ------------------ | ---- | ------- | ------------------------------------ | ------------------ |
| object_name        | str  | None    | Unique identifier of the element     | "container"        |
| boolean_attributes | str  | []      | Boolean attributes                   | "main-container"   |
| inline_styles      | str  | []      | Inline CSS styles (string format)    | "property: value;" |
| \*\*kwargs         | str  | -       | CSS classes (space-separated string) | "btn btn-primary"  |

### Special \*\*kwargs parameters:

- `class_` - CSS classes (space-separated string)
- Any other attributes defined in `ValueAttributes` from [HTMLAttributes](HTMLAttributes.md)

---

### Examples:

```python
# Simple element with classes and styles
element1 = HTMLElement(
    object_name="element1",
    class_="container primary",
    style="color: red; font-size: 14px;",
    id="main",
    title="Main element"
)

# Element with boolean attributes
element2 = HTMLElement(
    object_name="element2",
    boolean_attributes=["disabled", "readonly", "required"],
    id="inputField",
    name="username",
    placeholder="Enter name"
)

# Element with custom attributes
element3 = HTMLElement(
    object_name="element3",
    data_id="123",
    aria_label="Description",
    custom_attribute="value"
)
```

---

## Class Attributes

| Attribute          | Type      | Description                            |
| ------------------ | --------- | -------------------------------------- |
| object_name        | str       | Unique identifier of the element       |
| object_type        | str       | Type name of the object                |
| class\_            | list[str] | List of CSS classes                    |
| inline_styles      | CSSInline | [CSSInline](../css/CSSInline.md) class |
| events             | dict      | Event handlers (event_name → handler)  |
| aria_attrs         | dict      | Accessibility attributes (ARIA)        |
| data_attrs         | dict      | Custom data attributes                 |
| value_attributes   | dict      | Standard HTML attributes with values   |
| custom_attributes  | dict      | Custom attributes (data-, aria-, etc.) |
| boolean_attributes | list[str] | List of boolean HTML attributes        |

---

## Supported Attributes

### From HTMLAttributes.ValueAttributes

The class supports all attributes defined in [HTMLAttributes](../html_core/HTMLAttributes.md), including:

- Basic: id, name, title, lang, dir, translate
- Styles: class, style
- Links: href, src, srcset, action, formaction
- Sizes: width, height
- Inputs: value, placeholder, min, max, pattern
- Meta: charset, content, http_equiv
- Tables: colspan, rowspan, scope
- And many others...

---

### Boolean attributes

Passed via `boolean_attributes`:

- Visibility: hidden, inert
- Forms: required, disabled, readonly, checked, selected
- Media: controls, autoplay, loop, muted
- Others: contenteditable, draggable, async, defer

---

### Events (HTMLEvents)

Supported via `add_event()`:

- MouseEvents: onclick, ondblclick, onmouseover, etc.
- KeyboardEvents: onkeydown, onkeyup, oninput
- FormEvents: onsubmit, onchange, onfocus, onblur
- MediaEvents: onplay, onpause, onerror

---

## Methods

### add_classname(classname)

Adds a CSS class to the element.

```python
element = HTMLElement(classname="container")
element.add_classname("active")
element.add_classname("highlight")

# Result: class="container active highlight"
```

---

### del_class(classname)

Removes a CSS class from the element.

```python
element = HTMLElement(classname="container active highlight")
element.del_class("active")

# Result: class="container highlight"
```

---

### add_event(event_name, handler)

Adds an event handler to the element.

```python
from LayoutML.html_core.HTMLEvents import MouseEvents, KeyboardEvents, FormEvents

element = HTMLElement()

element.add_event(MouseEvents.onclick, "handleClick(event)")
element.add_event(KeyboardEvents.onkeydown, "handleKeyPress(event)")
element.add_event(FormEvents.onfocus, "highlightField()")
```

---

### del_event(event_name)

Removes an event handler.

```python
element.del_event("onclick")
```

---

### add_aria(key, value)

Adds an ARIA attribute for accessibility.

```python
element.add_aria("label", "Main menu")
element.add_aria("expanded", "false")
```

---

### del_aria(key)

Removes an ARIA attribute.

```python
element.del_aria("label")
```

---

### add_data(key, value)

Adds a data-\* attribute.

```python
element.add_data("user_id", "12345")
element.add_data("role", "admin")
```

---

### del_data(key)

Removes a data-\* attribute.

```python
element.del_data("role")
```

---

### add_attributes(boolean_attributes=[], \*\*kwargs)

Adds multiple attributes at once.

```python
element.add_attributes(
    boolean_attributes=["required"],
    id="email",
    name="email",
    placeholder="Enter email"
)
```

---

### del_attributes(\*args)

Removes multiple attributes.

```python
element.del_attributes("id", "name", "required")
```

---

### get_attributes_string()

Generates a string of HTML attributes.

```python
element = HTMLElement(
    class_="btn btn-primary",
    id="submit"
)

print(f'<button {element.get_attributes_string()}>Send</button>')
```

---

## Examples

### Example 1: Form input

```python
element = HTMLElement(
    boolean_attributes=["required", "autofocus"],
    class_="form-control",
    id="username",
    name="username",
    placeholder="Enter username"
)

element.add_event("oninput", "validate()")
```

---

### Example 2: Button with events

```python
button = HTMLElement(
    class_="btn btn-primary",
    id="submitButton",
    type="button"
)

button.add_event("onclick", "submitForm()")
button.add_event("onmouseover", "showTooltip()")
```

---

## Attribute order

Attributes are generated in this order:

1. CSS classes
2. Inline styles
3. Events
4. Boolean attributes
5. Data attributes
6. ARIA attributes
7. Standard attributes

---

## Security

- Avoid unsafe inline JavaScript with user input
- Prefer `add_event()` for handlers
- Validate all external data

---

## Performance

- Cache attribute strings for static elements
- Use `add_classname()` instead of rebuilding classes
- Avoid excessive inline styles

---

## Accessibility

- Always use ARIA attributes for interactive elements
- Use `tabindex` for focus control
- Provide `aria-label` when needed

---

## Limitations

- No nested elements support
- No automatic validation of attributes
- Inline JS should be minimal

---

## Compatibility

Generates standard HTML5-compliant attributes compatible with all modern browsers (W3C HTML5 standard).
