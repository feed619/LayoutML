# Footer

`Footer` is a specialized class for creating the semantic HTML element <footer>. The class inherits from [BaseElement](../base/BaseElement.md) and is intended for creating page or section footers that contain information about the author, copyright, links to related documents, contact information, and other elements typically placed at the bottom of a document.

---

## Import

```python
from layoutML.elements import Footer
```

## Inheritance

- Parent class: BaseElement
- Element type: footer (non-self-closing tag)
- Purpose: Creating semantic containers for page and section footers

## Constructor

### **init**(object_name=None, style=None, boolean_attributes=[], \*\*kwargs)

Creates a new footer element with the specified parameters.

Parameters:

- object_name (optional): Element name/identifier
- style (optional): CSS string for inline styles
- boolean_attributes (optional): List of boolean attributes
- \*_kwargs: Additional HTML attributes (id, class\_, aria-_, etc.)

Automatically assigned properties:

- Tag: footer
- self_closing: False (non-self-closing tag)
- object_type: "FooterElement"

## Examples:

```python id="footer_ex_01"
# Simple footer
footer = Footer()

# Footer with name and classes
footer = Footer(
    object_name="pageFooter",
    class_="footer main-footer",
    id="siteFooter"
)

# Footer with inline styles
footer = Footer(
    style="background-color: #333; color: white; padding: 20px;",
    aria_label="Site footer"
)
```

## Styled Footer

```python id="footer_ex_02"
footer = Footer(object_name="styledFooter")

# Inline styles
footer.inline_styles.set_background_color("#2c3e50")\
                     .set_color("white")\
                     .set_padding("40px 20px 20px")\
                     .set_margin_top("50px")\
                     .set_font_family("Arial, sans-serif")

# CSS styles via object_styles
footer.object_styles.set_text_align("center")\
                     .set_border_top("3px solid #3498db")
```
