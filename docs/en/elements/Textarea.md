# Textarea

`Textarea` is a specialized class for creating the HTML <textarea> element. The class inherits from [BaseElement](../base/BaseElement.md) and provides a convenient interface for creating multi-line text fields with configurable size, placeholder text, and other attributes.

---

## Import

```python
from layoutML.elements import Textarea
```

## Inheritance

- Parent class: BaseElement
- Element type: textarea (non-self-closing tag)
- Purpose: Creating multi-line text fields for entering large amounts of text

## Constructor

### **init**(placeholder="", value="", rows=4, cols=50, name=None, id=None, object_name=None, style=None, boolean_attributes=[], \*\*kwargs)

Creates a new multi-line text field with the specified parameters.

Parameters:

- placeholder (str): Placeholder text inside the field. Defaults to empty string
- value (str): Pre-filled text in the field. Defaults to empty string
- rows (int): Number of visible rows. Defaults to 4
- cols (int): Number of visible columns. Defaults to 50
- name (str): Field name for form submission. Defaults to None
- id (str): Unique identifier for the field. Defaults to None
- object_name (optional): Element name/identifier
- style (optional): CSS string for inline styles
- boolean_attributes (optional): List of boolean attributes (required, disabled, readonly)
- \*\*kwargs: Additional HTML attributes

### Automatically assigned properties:

- Tag: textarea
- self_closing: False (non-self-closing tag)
- object_type: "TextareaElement"
- placeholder: placeholder text
- value: pre-filled text
- rows: number of rows
- cols: number of columns
- name: field name
- id: field identifier

## Example:

```python
# Simple textarea
textarea = Textarea()

# Configured textarea
textarea = Textarea(
    placeholder="Enter your feedback...",
    rows=6,
    cols=60,
    name="review",
    id="review-field"
)

# Pre-filled textarea
textarea = Textarea(
    value="This is pre-filled text.\nIt can span multiple lines.",
    rows=5,
    class_="form-textarea",
    required=True
)
```

## Usage examples

### Basic text areas

```python
# Comment field
comment = Textarea(
    placeholder="Leave your comment...",
    rows=5,
    cols=60,
    name="comment"
)

# Pre-filled feedback
feedback = Textarea(
    value="Great job! Thank you.",
    rows=4,
    name="feedback"
)
```

### Feedback form

```python
from layoutml import Form, Input, Button, Label

form = Form(action="/submit", method="post")

# Name
form.add_element(Label(for_id="name", text="Name:"))
form.add_element(Input(id="name", name="name", required=True))

# Email
form.add_element(Label(for_id="email", text="Email:"))
form.add_element(Input(type="email", id="email", name="email", required=True))

# Message
form.add_element(Label(for_id="message", text="Message:"))
message_field = Textarea(
    id="message",
    name="message",
    placeholder="Enter your message...",
    rows=6,
    required=True
)
form.add_element(message_field)

# Submit button
form.add_element(Button(text="Send", type="submit"))
```

### Styled textarea

```python
textarea = Textarea(
    object_name="styledTextarea",
    placeholder="Your feedback...",
    rows=5
)

# Inline styles
textarea.inline_styles.set_width("100%")\
                      .set_padding("12px")\
                      .set_border("2px solid #ddd")\
                      .set_border_radius("8px")\
                      .set_font_size("16px")\
                      .set_font_family("Arial, sans-serif")\
                      .set_resize("vertical")

# Focus styles
textarea.selectors_styles.add_selector("styledTextarea:focus")\
    .set_border_color("#007bff")\
    .set_outline("none")\
    .set_box_shadow("0 0 0 3px rgba(0,123,255,0.25)")

# Placeholder styles
textarea.selectors_styles.add_selector("styledTextarea::placeholder")\
    .set_color("#999")\
    .set_font_style("italic")
```

### Textarea with limits

```python
bio = Textarea(
    placeholder="Tell us about yourself...",
    rows=4,
    name="bio",
    maxlength="500",
    data_maxlength="500"
)

bio.add_event("oninput", "updateCounter(this)")

counter_script = """
function updateCounter(textarea) {
    const max = textarea.getAttribute('maxlength');
    const current = textarea.value.length;
    const counter = document.getElementById('charCounter');
    if (counter) {
        counter.textContent = current + ' / ' + max;
    }
}
"""
```

### Preview textarea

```python
preview_textarea = Textarea(
    placeholder="Enter text for preview...",
    rows=6,
    id="editor",
    name="content"
)

preview_btn = Button(text="Preview", onclick="showPreview()")

preview_container = BaseElement(tag="div", id="preview", class_="preview")

preview_script = """
function showPreview() {
    const content = document.getElementById('editor').value;
    const preview = document.getElementById('preview');
    preview.innerHTML = '<h3>Preview:</h3><div class="preview-content">' +
                        content.replace(/\\n/g, '<br>') + '</div>';
}
"""
```

### Responsive textarea

```python
responsive_textarea = Textarea(
    object_name="responsiveTextarea",
    placeholder="Responsive textarea...",
    rows=4
)

responsive_textarea.object_styles.set_width("100%")\
                                  .set_box_sizing("border-box")

desktop_media = responsive_textarea.selectors_styles.add_selector(
    "@media (min-width: 768px)",
    selector_type="media"
)
desktop_media.set_font_size("16px")

mobile_media = responsive_textarea.selectors_styles.add_selector(
    "@media (max-width: 480px)",
    selector_type="media"
)
mobile_media.set_font_size("14px")\
           .set_padding("8px")
```

### Boolean attributes

```python
required_textarea = Textarea(
    placeholder="Required field",
    boolean_attributes=["required"],
    name="required_field"
)

readonly_textarea = Textarea(
    value="This text cannot be edited",
    boolean_attributes=["readonly"],
    name="readonly_field"
)

disabled_textarea = Textarea(
    placeholder="Disabled field",
    boolean_attributes=["disabled"],
    name="disabled_field"
)
```

### Modal textarea

```python
from layoutml import VerticalLayout

modal_content = VerticalLayout(object_name="modalContent")

title = BaseElement(tag="h3")
title.get_html(content="Edit description")

description = Textarea(
    value="Current product description...",
    rows=8,
    name="description",
    id="edit-description"
)

buttons = BaseElement(tag="div")
buttons.get_html(content="""
    <button onclick="saveChanges()">Save</button>
    <button onclick="closeModal()">Cancel</button>
""")

modal_content.add_elements(title, description, buttons)
```

### Code editor textarea

```python
code_area = Textarea(
    placeholder="Enter code...",
    rows=10,
    name="code",
    class_="code-editor",
    data_language="python"
)

code_area.object_styles.set_font_family("'Courier New', monospace")\
                       .set_font_size("14px")\
                       .set_background_color("#1e1e1e")\
                       .set_color("#d4d4d4")\
                       .set_border("none")\
                       .set_border_radius("8px")\
                       .set_padding("15px")

code_area.selectors_styles.add_selector(".code-editor:focus")\
    .set_outline("2px solid #007acc")
```

## Best practices

### Size control

```python
good = Textarea(rows=5, cols=60)

better = Textarea(rows=5)
better.object_styles.set_width("100%").set_height("150px")

bad = Textarea(rows=1, cols=10)
```

### Good placeholders

```python
good = Textarea(
    placeholder="Write your product review...",
    rows=5
)

bad = Textarea(placeholder="Text", rows=5)
```

### Resizing control

```python
resizable = Textarea(rows=4)
resizable.object_styles.set_resize("vertical")

fixed = Textarea(rows=4)
fixed.object_styles.set_resize("none")
```

### Accessibility

```python
accessible = Textarea(
    placeholder="Comment",
    aria_label="Comment input field",
    aria_describedby="comment-help",
    aria_required="true"
)

help_text = BaseElement(tag="small", id="comment-help")
help_text.get_html(content="Max 500 characters")

accessible.value_attributes["aria-describedby"] = "comment-help"
```
