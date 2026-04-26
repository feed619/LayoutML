# DocTypes

`DocTypes` contains constants representing different document types (DOCTYPE) supported in the `doctype` parameter of the `Document` class.

---

## Purpose

This class provides a set of predefined document types for use when creating HTML/XML documents, ensuring type safety and preventing errors in DOCTYPE value spelling.

## Import

```python
from layoutml.types import DocTypes
```

## Full Constant Reference

| Constant     | Value          | Description                                                                       |
| ------------ | -------------- | --------------------------------------------------------------------------------- |
| HTML         | "html"         | Standard HTML DOCTYPE (no version)                                                |
| HTML5        | "html5"        | DOCTYPE for HTML5 (modern standard)                                               |
| XHTML        | "xhtml"        | Base DOCTYPE for XHTML                                                            |
| STRICT       | "strict"       | Strict DOCTYPE (typically HTML 4.01 Strict or XHTML 1.0 Strict)                   |
| TRANSITIONAL | "transitional" | Transitional DOCTYPE (typically HTML 4.01 Transitional or XHTML 1.0 Transitional) |

## Usage Examples

```python
# Import the class
from layoutml.types import DocTypes
from layoutml import Document

# Create a document with HTML5 DOCTYPE
document = Document(doctype=DocTypes.HTML5)

# Create a document with strict XHTML DOCTYPE
document = Document(doctype=DocTypes.STRICT)

# Create a document with transitional DOCTYPE
document = Document(doctype=DocTypes.TRANSITIONAL)
```
