# Paragraph

`Paragraph` is a specialized class for creating the HTML paragraph element <p>. The class inherits from [BaseElement](../base/BaseElement.md) and provides a convenient interface for creating text paragraphs, with the ability to set text either through the constructor or during HTML generation.

---

## Import

```python
from layoutML.elements import Paragraph
```

## Inheritance

- Parent class: BaseElement
- Element type: p (non-self-closing tag)
- Purpose: Creating text paragraphs for structuring content

## Constructor

### **init**(text="", object_name=None, style=None, boolean_attributes=[], \*\*kwargs)

Creates a new paragraph element with the specified parameters.

### Parameters:

- text (str): Paragraph text. Defaults to empty string
- object_name (optional): Element name/identifier
- style (optional): CSS string for inline styles
- boolean_attributes (optional): List of boolean attributes
- \*_kwargs: Additional HTML attributes (id, class\_, aria-_, etc.)

### Automatically assigned properties:

- Tag: p
- self_closing: False (non-self-closing tag)
- object_type: "ParagraphElement"
- text: paragraph text

### Examples:

```python
# Empty paragraph
p = Paragraph()

# Paragraph with text
p = Paragraph(text="This is paragraph text.")

# Paragraph with text and attributes
p = Paragraph(
    text="Welcome to our website!",
    object_name="welcomeMessage",
    class_="intro-text",
    style="font-size: 16px; line-height: 1.5;"
)
```

## Examples

### Basic paragraphs

```python
# Basic paragraph
p1 = Paragraph(text="This is a normal text paragraph.")

# Paragraph with class
p2 = Paragraph(
    text="This is important text.",
    class_="important"
)

# Paragraph with id
p3 = Paragraph(
    text="Unique paragraph",
    id="unique-paragraph"
)
```

### Styled paragraphs

```python
p = Paragraph(
    text="A styled paragraph with beautiful formatting.",
    object_name="styledParagraph"
)

# Inline styles
p.inline_styles.set_font_family("Georgia, serif")\
               .set_font_size("18px")\
               .set_line_height("1.8")\
               .set_color("#333")\
               .set_margin_bottom("20px")

# CSS styles via object_styles
p.object_styles.set_text_indent("20px")\
               .set_letter_spacing("0.5px")

# Pseudo-elements
p.selectors_styles.add_selector("styledParagraph::first-letter")\
    .set_font_size("24px")\
    .set_font_weight("bold")\
    .set_color("#007bff")

p.selectors_styles.add_selector("styledParagraph::first-line")\
    .set_font_weight("bold")
```
