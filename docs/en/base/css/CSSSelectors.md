

# CSSSelectors

`CSSSelectors` is a container class for managing a collection of CSS selectors and their styles. The class allows you to conveniently work with multiple selectors (classes, IDs, tags, media queries) and generate full CSS styles from them.

---

## Architecture

* Selector container: stores a collection of CSSBase objects
* Dynamic creation: selectors are created automatically on access
* Flexible configuration: supports classes, IDs, tags, and media queries
* Two output modes: raw CSS or HTML `<style>` tag

---

## Import

```python
from LayoutML.base.css import CSSInline
```

---

## Constructor

### **init**(inline: bool = False)

Creates a new CSS selector container.

Parameters:

* inline (bool): If True, `get_styles_str()` wraps CSS in a `<style>` tag. Default is False.

Examples:

```python
# Container for external CSS file
css = CSSSelectors()

# Container for inline HTML styles
css_inline = CSSSelectors(inline=True)
```

---

## Class Attributes

| Attribute | Type          | Description                         | Default |
| --------- | ------------- | ----------------------------------- | ------- |
| selectors | dict[CSSBase] | Dictionary containing all selectors | {}      |
| inline    | bool          | Output mode flag                    | False   |

---

## Methods

### add_selector(name, type="class", style=None)

Explicitly adds a selector with a given type and initial styles.

Parameters:

* name (str): Selector name
* type (str): Selector type. Allowed: `"class"`, `"id"`, `"tag"` (default: `"class"`)
* style (str, optional): Initial CSS style string

Returns:

* CSSBase: Instance of the added selector

Examples:

```python
# Add class selector
css_input.add_selector("container", "class", "width: 100%;")

# Add ID selector
css_input.add_selector("header", "id", "background: #333;")

# Add tag selector
css_input.add_selector("p", "tag", "margin: 10px 0;")

# Without initial styles
css_input.add_selector("button", "class")
```

---

### delete_selector(name)

Removes a selector from `self.selectors`.

Parameters:

* name (str): Name of the selector to remove

Example:

```python
css = CSSSelectors()
css.add_selector("temp-class")

print("temp-class" in css.selectors)  # True

css.delete_selector("temp-class")

print("temp-class" in css.selectors)  # False
```

---

### clear() -> CSSBase

Clears `self.selectors`, removing all selectors.

Example:

```python
css = CSSSelectors()
css.add_selector("class1")
css.add_selector("class2")

print(len(css.selectors))  # 2

css.clear()

print(len(css.selectors))  # 0
print(css.selectors)  # {}
```

---

### selector_exists(name: str) -> tuple[bool, str]

Checks whether a selector exists in `self.selectors`.

Parameters:

* name (str): Selector name to check

Returns:

* Tuple (bool, str): whether the selector exists and its type

Example:

```python
css = CSSSelectors()
css.add_selector("my-class")

exists = css.selector_exists("my-class")   # (True, "class")
not_exists = css.selector_exists("other")  # (False, "")
```

---

### add_styles(selector_name: str, styles: dict | CSSBase)

Adds styles to an existing selector in `self.selectors`.

Parameters:

* selector_name (str): Selector name
* styles (dict | CSSBase): Styles to add

Example:

```python
css = CSSSelectors()
css.add_selector("box")

print(css.selectors["box"].styles)  # {}

css.add_styles("box", {"width": "100px", "height": "100px"})

print(css.selectors["box"].styles)
# {'width': '100px', 'height': '100px'}
```

---

### get_styles(space=True) -> dict

Generates a dictionary of styles for all selectors in `self.selectors`.

Parameters:

* space (bool): If True, formats with indentation and line breaks

Returns:

* Dictionary where keys are selectors with prefixes, values are CSS strings

Example:

```python
css = CSSSelectors()
css.add_selector("container", "class").set_width("100%")
css.add_selector("header", "id").set_background_color("blue")

styles_dict = css.get_styles()

# Result:
# {
#   '.container': 'width:100%;',
#   '#header': 'background-color:blue;'
# }
```

---

### get_styles_str() -> str

Generates a CSS string. Uses the `inline` attribute to determine output format.

Logic:

* Retrieves styles via `self.get_styles()`
* Builds CSS blocks per selector
* If `inline == True`, wraps result in `<style>` tag

Examples:

```python
# External CSS mode
css = CSSSelectors(inline=False)
css.add_selector("container").set_width("100%")

print(css.get_styles_str())

# Result:
# .container {
# width:100%;
# }

# Inline HTML mode
css_inline = CSSSelectors(inline=True)
css_inline.add_selector("container").set_width("100%")

print(css_inline.get_styles_str())

# Result:
# <style>
# .container {
# width:100%;
# }
# </style>
```

---

## Python Special Methods

### Dynamic selector access via attributes

```python
css = CSSSelectors()

css.container.set_width("100%")  
css.header.set_background_color("blue")

print(css.selectors.keys())
# dict_keys(['container', 'header'])
```

---

### Dictionary-like usage

```python
css = CSSSelectors()

selector = css["my-class"]
print("my-class" in css.selectors)  # True

css["my-class"] = CSSBase().set_width("100px")
css["another"] = {"width": "100px"}
css["third"] = "width: 100px;"

del css["my-class"]

count = len(css)

if css:
    print("Selectors exist")

for name, selector in css:
    print(name, selector.get_styles_string())
```

---

## Selector Types and Prefixes

Stored in `type` attribute of CSSBase objects:

| Type    | Prefix | CSS Example               |
| ------- | ------ | ------------------------- |
| "class" | .      | .container                |
| "id"    | #      | #header                   |
| "tag"   | none   | div                       |
| "media" | none   | @media (max-width: 768px) |

---

## Examples

### Example 1: Button component using attribute access

```python
css = CSSSelectors(inline=True)

print(f"Inline mode: {css.inline}")
print(f"Initial selectors: {len(css.selectors)}")

css.btn.set_display("inline-block")\
       .set_padding("10px 20px")\
       .set_background_color("#007bff")

css["btn:hover"].set_background_color("#0056b3")

print(f"Final selectors: {len(css.selectors)}")
print(list(css.selectors.keys()))

print(css.get_styles_str())
```

---

### Example 2: Using inline flag

```python
def generate_page_styles(inline_mode=False):
    css = CSSSelectors(inline=inline_mode)

    css.container.set_width("100%").set_max_width("1200px")
    css.header.set_background_color("#333").set_color("white")

    return css.get_styles_str()

# External file
external_css = generate_page_styles(False)

with open("styles.css", "w") as f:
    f.write(external_css)

# Inline HTML
inline_css = generate_page_styles(True)

html_template = f"""
<!DOCTYPE html>
<html>
<head>
    {inline_css}
</head>
<body>
</body>
</html>
"""
```

---
