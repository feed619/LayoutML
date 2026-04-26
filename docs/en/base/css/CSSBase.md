# CSSBase

`CSSBase` is a Python class for working with CSS styles of HTML elements. The class provides methods for convenient management of CSS properties through method chaining and allows converting styles between string and dictionary representations.

---

## Import

```python
from LayoutML.base.css import CSSBase
```

---

## Constructor

### **init**(self, type="tag", style=None):

Parameters:

| Parameter | Type | Default | Description                                                  |
| --------- | ---- | ------- | ------------------------------------------------------------ |
| type      | str  | "tag"   | Element type                                                 |
| style     | str  | None    | CSS style string to parse. Format: "key:value; key2:value2". |

Example:

```python
# With empty styles
element = CSSBase()

# With initial styles
element = CSSBase(style="width: 100px; height: 200px; color: #333;")
```

---

## Core Methods

### parse_style_string(style_str: str) -> dict

Parses a CSS style string into a dictionary.

Parameters:

- style_str: CSS style string (e.g. "color: red; font-size: 16px;")

Returns:

- Dictionary with style keys and values

Example:

```python
css = CSSBase()
parsed = css.parse_style_string("color: red; font-size: 16px;")
# Result: {'color': 'red', 'font-size': '16px'}
```

---

### get_styles_string(space=False) -> str

Returns a string representation of styles.

Parameters:

- space (bool): If True, formats with spaces and line breaks

Example:

```python
css = CSSBase(style="color: red; font-size: 16px;")

print(css.get_styles_string())
# Result: "color:red;font-size:16px;"

print(css.get_styles_string(space=True))
# Result:
# "  color: red;
#   font-size: 16px;"
```

---

## CSS Property Methods

### Box Model

| Method                    | Description            | Example                      |
| ------------------------- | ---------------------- | ---------------------------- |
| set_width(value)          | Set width              | set_width("300px")           |
| set_height(value)         | Set height             | set_height("200px")          |
| set_min_width(value)      | Min width              | set_min_width("100px")       |
| set_min_height(value)     | Min height             | set_min_height("50px")       |
| set_max_width(value)      | Max width              | set_max_width("500px")       |
| set_max_height(value)     | Max height             | set_max_height("400px")      |
| set_margin(value)         | External margin        | set_margin("10px 20px")      |
| set_margin_top(value)     | Top margin             | set_margin_top("10px")       |
| set_margin_right(value)   | Right margin           | set_margin_right("15px")     |
| set_margin_bottom(value)  | Bottom margin          | set_margin_bottom("10px")    |
| set_margin_left(value)    | Left margin            | set_margin_left("15px")      |
| set_padding(value)        | Inner padding          | set_padding("20px")          |
| set_padding_top(value)    | Top padding            | set_padding_top("10px")      |
| set_padding_right(value)  | Right padding          | set_padding_right("15px")    |
| set_padding_bottom(value) | Bottom padding         | set_padding_bottom("10px")   |
| set_padding_left(value)   | Left padding           | set_padding_left("15px")     |
| set_box_sizing(value)     | Box model              | set_box_sizing("border-box") |
| set_display(value)        | Display type           | set_display("flex")          |
| set_visibility(value)     | Visibility             | set_visibility("hidden")     |
| set_overflow(value)       | Overflow               | set_overflow("auto")         |
| remove_padding_margin()   | Remove margins/padding | remove_padding_margin()      |

---

### Positioning

| Method              | Description   | Example                  |
| ------------------- | ------------- | ------------------------ |
| set_position(value) | Position type | set_position("relative") |
| set_top(value)      | Top offset    | set_top("10px")          |
| set_right(value)    | Right offset  | set_right("20px")        |
| set_bottom(value)   | Bottom offset | set_bottom("30px")       |
| set_left(value)     | Left offset   | set_left("40px")         |
| set_z_index(value)  | Z-index       | set_z_index(100)         |
| set_float(value)    | Float         | set_float("left")        |
| set_clear(value)    | Clear float   | set_clear("both")        |

---

### Flexbox

| Method                     | Description          | Example                            |
| -------------------------- | -------------------- | ---------------------------------- |
| set_flex_direction(value)  | Flex direction       | set_flex_direction("row")          |
| set_flex_wrap(value)       | Wrap                 | set_flex_wrap("wrap")              |
| set_flex_flow(value)       | Flex flow shorthand  | set_flex_flow("row wrap")          |
| set_justify_content(value) | Main axis alignment  | set_justify_content("center")      |
| set_align_items(value)     | Cross axis alignment | set_align_items("center")          |
| set_align_content(value)   | Align lines          | set_align_content("space-between") |
| set_align_self(value)      | Self alignment       | set_align_self("flex-start")       |
| set_flex_grow(value)       | Grow factor          | set_flex_grow(1)                   |
| set_flex_shrink(value)     | Shrink factor        | set_flex_shrink(0)                 |
| set_flex_basis(value)      | Base size            | set_flex_basis("auto")             |
| set_flex(value)            | Shorthand            | set_flex("1 0 auto")               |
| set_order(value)           | Order                | set_order(2)                       |
| set_gap(value)             | Gap between elements | set_gap("10px")                    |

---

### Grid

| Method                           | Description         | Example                                                    |
| -------------------------------- | ------------------- | ---------------------------------------------------------- |
| set_grid_template_columns(value) | Column template     | set_grid_template_columns("1fr 2fr 1fr")                   |
| set_grid_template_rows(value)    | Row template        | set_grid_template_rows("100px auto")                       |
| set_grid_template_areas(value)   | Areas               | set_grid_template_areas("header header" "sidebar content") |
| set_grid_template(value)         | Shorthand           | set_grid_template("100px auto / 1fr 2fr")                  |
| set_grid_column_start(value)     | Column start        | set_grid_column_start("2")                                 |
| set_grid_column_end(value)       | Column end          | set_grid_column_end("4")                                   |
| set_grid_row_start(value)        | Row start           | set_grid_row_start("1")                                    |
| set_grid_row_end(value)          | Row end             | set_grid_row_end("3")                                      |
| set_grid_area(value)             | Grid area           | set_grid_area("header")                                    |
| set_justify_items(value)         | Item alignment      | set_justify_items("center")                                |
| set_place_items(value)           | Shorthand alignment | set_place_items("center center")                           |

---

### Background

| Method                           | Description      | Example                                                  |
| -------------------------------- | ---------------- | -------------------------------------------------------- |
| set_background_color(value)      | Background color | set_background_color("#f0f0f0")                          |
| set_background_image(value)      | Background image | set_background_image("url('bg.jpg')")                    |
| set_background_repeat(value)     | Repeat           | set_background_repeat("no-repeat")                       |
| set_background_position(value)   | Position         | set_background_position("center")                        |
| set_background_size(value)       | Size             | set_background_size("cover")                             |
| set_background_attachment(value) | Attachment       | set_background_attachment("fixed")                       |
| set_background(value)            | Shorthand        | set_background("#f0f0f0 url('bg.jpg') no-repeat center") |
| set_background_clip(value)       | Clip             | set_background_clip("content-box")                       |
| set_background_origin(value)     | Origin           | set_background_origin("padding-box")                     |

---

### Borders

| Method                                | Description         | Example                               |
| ------------------------------------- | ------------------- | ------------------------------------- |
| set_border(value)                     | Border              | set_border("1px solid #000")          |
| set_border_width(value)               | Width               | set_border_width("2px")               |
| set_border_style(value)               | Style               | set_border_style("dashed")            |
| set_border_color(value)               | Color               | set_border_color("#ccc")              |
| set_border_top(value)                 | Top border          | set_border_top("2px solid red")       |
| set_border_right(value)               | Right border        | set_border_right("1px dotted #999")   |
| set_border_bottom(value)              | Bottom border       | set_border_bottom("3px double blue")  |
| set_border_left(value)                | Left border         | set_border_left("1px solid green")    |
| set_border_radius(value)              | Radius              | set_border_radius("10px")             |
| set_border_top_left_radius(value)     | Top-left radius     | set_border_top_left_radius("5px")     |
| set_border_top_right_radius(value)    | Top-right radius    | set_border_top_right_radius("5px")    |
| set_border_bottom_left_radius(value)  | Bottom-left radius  | set_border_bottom_left_radius("5px")  |
| set_border_bottom_right_radius(value) | Bottom-right radius | set_border_bottom_right_radius("5px") |
| set_outline(value)                    | Outline             | set_outline("2px dashed red")         |

---

### Text

| Method                     | Description    | Example                              |
| -------------------------- | -------------- | ------------------------------------ |
| set_color(value)           | Text color     | set_color("#333")                    |
| set_font_family(value)     | Font family    | set_font_family("Arial, sans-serif") |
| set_font_size(value)       | Font size      | set_font_size("16px")                |
| set_font_weight(value)     | Font weight    | set_font_weight("bold")              |
| set_font_style(value)      | Font style     | set_font_style("italic")             |
| set_line_height(value)     | Line height    | set_line_height("1.5")               |
| set_text_align(value)      | Alignment      | set_text_align("center")             |
| set_text_decoration(value) | Decoration     | set_text_decoration("underline")     |
| set_text_transform(value)  | Transform      | set_text_transform("uppercase")      |
| set_letter_spacing(value)  | Letter spacing | set_letter_spacing("1px")            |
| set_word_spacing(value)    | Word spacing   | set_word_spacing("2px")              |

---

### Animations & Transitions

| Method                                | Description     | Example                                       |
| ------------------------------------- | --------------- | --------------------------------------------- |
| set_transition(value)                 | Transition      | set_transition("all 0.3s ease")               |
| set_transition_property(value)        | Property        | set_transition_property("opacity")            |
| set_transition_duration(value)        | Duration        | set_transition_duration("0.5s")               |
| set_transition_timing_function(value) | Timing function | set_transition_timing_function("ease-in-out") |
| set_transition_delay(value)           | Delay           | set_transition_delay("0.1s")                  |
| set_animation(value)                  | Animation       | set_animation("slide 2s infinite")            |
| set_animation_name(value)             | Name            | set_animation_name("fadeIn")                  |
| set_animation_duration(value)         | Duration        | set_animation_duration("1s")                  |
| set_animation_timing_function(value)  | Timing          | set_animation_timing_function("linear")       |
| set_animation_delay(value)            | Delay           | set_animation_delay("0.5s")                   |

---

### Transforms

| Method                         | Description         | Example                            |
| ------------------------------ | ------------------- | ---------------------------------- |
| set_transform(value)           | Transform           | set_transform("rotate(45deg)")     |
| set_transform_origin(value)    | Origin              | set_transform_origin("center")     |
| set_transform_style(value)     | Style               | set_transform_style("preserve-3d") |
| set_perspective(value)         | Perspective         | set_perspective("500px")           |
| set_backface_visibility(value) | Backface visibility | set_backface_visibility("hidden")  |

---

### Misc Properties

| Method                 | Description    | Example                                     |
| ---------------------- | -------------- | ------------------------------------------- |
| set_opacity(value)     | Opacity        | set_opacity(0.5)                            |
| set_filter(value)      | Filter         | set_filter("blur(5px)")                     |
| set_box_shadow(value)  | Box shadow     | set_box_shadow("0 2px 5px rgba(0,0,0,0.2)") |
| set_text_shadow(value) | Text shadow    | set_text_shadow("1px 1px 2px #000")         |
| set_cursor(value)      | Cursor         | set_cursor("pointer")                       |
| set_user_select(value) | Text selection | set_user_select("none")                     |

---

### Utility Methods

#### Style management

```python
# Add styles from string
element.add_styles_from_string("width: 100px; height: 200px; color: red;")

# Set custom style
element.add_style("custom-property", "value")

# Get style value
width = element.get_style("width")

# Check style existence
has_width = element.has_style("width")

# Remove style
element.remove_style("width")

# Clear all styles
element.clear_styles()

# Merge styles from dict
element.merge_styles({"margin": "10px", "padding": "20px"})

# Copy styles
styles_copy = element.copy_styles()
```

---

### Working with style strings

```python
# Compact style string
style_string = element.get_styles_string()
# width:300px;height:200px;color:#333;

# Formatted style string
formatted_style = element.get_styles_string(space=True)
#   width:300px;
#   height:200px;
#   color:#333;
```

---

### CSS Variables

```python
# Set CSS variable
element.set_css_variable("main-color", "#ff0000")
element.set_css_variable("padding-size", "20px")

# Get CSS variable
color = element.get_css_variable("main-color")  # "#ff0000"
```

---

## Examples

### Example 1: Basic usage

```python
css = CSSBase()
css.set_width("100px")\
   .set_height("200px")\
   .set_background_color("#f0f0f0")\
   .set_margin("10px")\
   .set_padding("20px")

print(css.get_styles_string())
# Result: "width:100px;height:200px;background-color:#f0f0f0;margin:10px;padding:20px;"
```

---

### Example 2: CSS variables

```python
css = CSSBase()
css.set_css_variable("primary-color", "#007bff")\
   .set_css_variable("border-radius", "4px")

color = css.get_css_variable("primary-color")  # Returns "#007bff"
```
