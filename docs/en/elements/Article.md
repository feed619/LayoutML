# Article

`Article` is a specialized class for creating the semantic HTML element <article>. The class inherits from [BaseElement](../base/BaseElement.md) and is intended for building self-contained, independent pieces of content such as blog posts, news articles, comments, or any other standalone information fragments.

---

## Import

```python
from layoutML.elements import Article
```

## Inheritance

- Parent class: BaseElement
- Element type: article (non-self-closing tag)
- Purpose: Creating semantic containers for independent content

## Constructor

### **init**(object_name=None, style=None, boolean_attributes=[], \*\*kwargs)

Creates a new article element with the specified parameters.

Parameters:

- object_name (optional): Element name/identifier
- style (optional): CSS string for inline styles
- boolean_attributes (optional): List of boolean attributes
- \*_kwargs: Additional HTML attributes (id, class\_, aria-_, etc.)

Automatically assigned properties:

- Tag: article
- self_closing: False (non-self-closing tag)
- object_type: "ArticleElement"

## Examples:

```python
# Simple article
article = Article()

# Article with name and classes
article = Article(
    object_name="blogPost",
    class_="post featured",
    id="post123"
)

# Article with inline styles
article = Article(
    style="margin-bottom: 20px; padding: 15px; border: 1px solid #ddd;",
    aria_label="Web development article"
)
```

## Usage Examples

```python
article = Article(object_name="styledPost")

# Adding inline styles
article.inline_styles.set_margin_bottom("30px")\
                     .set_padding("20px")\
                     .set_background_color("#f9f9f9")\
                     .set_border_radius("8px")\
                     .set_box_shadow("0 2px 8px rgba(0,0,0,0.1)")

# Adding CSS styles via object_styles
article.object_styles.set_font_family("Arial, sans-serif")\
                     .set_line_height("1.6")\
                     .set_color("#333")

# Adding content
article.get_html(content="<h2>Title</h2><p>Content...</p>")
```
