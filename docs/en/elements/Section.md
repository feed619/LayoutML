# Section

`Section` is a specialized class for creating the semantic HTML element <section>. The class inherits from [BaseElement](../base/BaseElement.md) and is intended for creating thematic groups of content, usually with their own heading, that form part of a larger document or application.

---

## Import

```python
from layoutML.elements import Section
```

## Inheritance

- Parent class: BaseElement
- Element type: section (non-self-closing tag)
- Purpose: Creating semantic containers for thematically related content

## Constructor

### **init**(object_name=None, style=None, boolean_attributes=[], \*\*kwargs)

Creates a new section element with the specified parameters.

### Parameters:

- object_name (optional): Element name/identifier
- style (optional): CSS string for inline styles
- boolean_attributes (optional): List of boolean attributes
- \*_kwargs: Additional HTML attributes (id, class\_, aria-_, etc.)

### Automatically assigned properties:

- Tag: section
- self_closing: False (non-self-closing tag)
- object_type: "SectionElement"

### Examples:

```python
# Simple section
section = Section()

# Section with name and classes
section = Section(
    object_name="featuresSection",
    class_="features highlight",
    id="mainFeatures"
)

# Section with inline styles
section = Section(
    style="background-color: #f8f9fa; padding: 40px 20px;",
    aria_label="Main advantages"
)
```
