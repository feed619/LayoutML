# Image

`Image` is a specialized class for creating the HTML image element <img>. The class inherits from [BaseElement](../base/BaseElement.md) and provides a convenient interface for inserting images with automatic handling of required attributes src and alt.

---

## Import

```python
from layoutML.elements import Image
```

## Inheritance

- Parent class: BaseElement
- Element type: img (self-closing tag)
- Purpose: Inserting images into an HTML document

## Constructor

### **init**(src, alt="", object_name=None, style=None, boolean_attributes=[], \*\*kwargs)

Creates a new image element with the specified parameters.

## Parameters:

- src (str): Path to the image file. Required parameter
- alt (str): Alternative text for the image. Defaults to empty string
- object_name (optional): Element name/identifier
- style (optional): CSS string for inline styles
- boolean_attributes (optional): List of boolean attributes
- \*\*kwargs: Additional HTML attributes (width, height, loading, decoding, etc.)

## Automatically assigned properties:

- Tag: img
- self_closing: True (self-closing tag)
- object_type: "ImageElement"
- src: image path
- alt: alternative text

## Examples:

```python
# Simple image
img = Image(src="photo.jpg", alt="Photograph")

# Image with additional attributes
img = Image(
    src="images/logo.png",
    alt="Company logo",
    object_name="companyLogo",
    class_="logo",
    width="200",
    height="100",
    loading="lazy"
)

# Image with inline styles
img = Image(
    src="banner.jpg",
    alt="Banner",
    style="border-radius: 8px; box-shadow: 0 2px 10px rgba(0,0,0,0.1);",
    decoding="async"
)
```

## Usage Examples

### Basic Images

```python
# Regular image
img1 = Image(src="photo.jpg", alt="Landscape")

# Image with dimensions
img2 = Image(
    src="avatar.png",
    alt="User avatar",
    width="100",
    height="100"
)

# Image with classes
img3 = Image(
    src="banner.jpg",
    alt="Advertisement banner",
    class_="banner responsive",
    id="mainBanner"
)
```

### Lazy-loaded Images

```python
# Lazy loading for performance optimization
lazy_img = Image(
    src="large-image.jpg",
    alt="Large image",
    loading="lazy",
    decoding="async",
    fetchpriority="low"
)

# Critical image (loads immediately)
hero_img = Image(
    src="hero.jpg",
    alt="Main image",
    loading="eager",
    fetchpriority="high",
    decoding="sync"
)
```

### Responsive Images

```python
# Image with srcset for different resolutions
responsive_img = Image(
    src="image-medium.jpg",  # Fallback
    alt="Responsive image",
    srcset="""
        image-small.jpg 300w,
        image-medium.jpg 600w,
        image-large.jpg 900w,
        image-xlarge.jpg 1200w
    """,
    sizes="(max-width: 600px) 300px, (max-width: 900px) 600px, 900px"
)

# Image with multiple formats
webp_img = Image(
    src="image.jpg",
    alt="Modern format image",
    srcset="image.webp, image.jpg"
)
```

### Styled Images

```python
# Image with CSS classes
styled_img = Image(
    src="profile.jpg",
    alt="Profile photo",
    class_="profile-photo"
)

# Inline styles
styled_img.inline_styles.set_border_radius("50%")\
                         .set_border("3px solid #007bff")\
                         .set_box_shadow("0 4px 12px rgba(0,0,0,0.15)")

# CSS styles via object_styles
styled_img.object_styles.set_width("150px")\
                         .set_height("150px")\
                         .set_object_fit("cover")

# Hover effect via selectors_styles
styled_img.selectors_styles.add_selector("profile-photo:hover")\
    .set_transform("scale(1.05)")\
    .set_transition("transform 0.3s")
```
