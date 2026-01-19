from typing import Dict, Any, Optional, Union, List


class CSSBase:
    """Класс с методами для работы с CSS стилями HTML элементов"""

    styles: dict

    def __init__(self, type="tag", style=None):
        self.styles: Dict[str, str] = {}
        self.type = type

        if style:
            self.styles = self.parse_style_string(style)

    def parse_style_string(self, style_str: str) -> dict:
        """Парсит CSS-строку стилей в словарь."""
        styles = {}

        for item in style_str.split(";"):
            item = item.strip()
            if not item:
                continue

            if ":" not in item:
                continue
            key, value = item.split(":", 1)
            styles[key.strip()] = value.strip()

        return styles

    # ============ БЛОЧНАЯ МОДЕЛЬ ============

    def set_width(self, width: str) -> "CSSBase":
        """Установить ширину: 100px, 50%, auto, etc."""
        self.styles["width"] = width
        return self

    def set_height(self, height: str) -> "CSSBase":
        """Установить высоту: 100px, 50%, auto, etc."""
        self.styles["height"] = height
        return self

    def set_min_width(self, min_width: str) -> "CSSBase":
        """Установить минимальную ширину"""
        self.styles["min-width"] = min_width
        return self

    def set_min_height(self, min_height: str) -> "CSSBase":
        """Установить минимальную высоту"""
        self.styles["min-height"] = min_height
        return self

    def set_max_width(self, max_width: str) -> "CSSBase":
        """Установить максимальную ширину"""
        self.styles["max-width"] = max_width
        return self

    def set_max_height(self, max_height: str) -> "CSSBase":
        """Установить максимальную высоту"""
        self.styles["max-height"] = max_height
        return self

    def set_margin(self, margin: str) -> "CSSBase":
        """Установить внешние отступы: 10px, 10px 20px, 10px 20px 30px 40px"""
        self.styles["margin"] = margin
        return self

    def set_margin_top(self, margin: str) -> "CSSBase":
        """Установить верхний внешний отступ"""
        self.styles["margin-top"] = margin
        return self

    def set_margin_right(self, margin: str) -> "CSSBase":
        """Установить правый внешний отступ"""
        self.styles["margin-right"] = margin
        return self

    def set_margin_bottom(self, margin: str) -> "CSSBase":
        """Установить нижний внешний отступ"""
        self.styles["margin-bottom"] = margin
        return self

    def set_margin_left(self, margin: str) -> "CSSBase":
        """Установить левый внешний отступ"""
        self.styles["margin-left"] = margin
        return self

    def set_padding(self, padding: str) -> "CSSBase":
        """Установить внутренние отступы: 10px, 10px 20px, 10px 20px 30px 40px"""
        self.styles["padding"] = padding
        return self

    def set_padding_top(self, padding: str) -> "CSSBase":
        """Установить верхний внутренний отступ"""
        self.styles["padding-top"] = padding
        return self

    def set_padding_right(self, padding: str) -> "CSSBase":
        """Установить правый внутренний отступ"""
        self.styles["padding-right"] = padding
        return self

    def set_padding_bottom(self, padding: str) -> "CSSBase":
        """Установить нижний внутренний отступ"""
        self.styles["padding-bottom"] = padding
        return self

    def set_padding_left(self, padding: str) -> "CSSBase":
        """Установить левый внутренний отступ"""
        self.styles["padding-left"] = padding
        return self

    def set_box_sizing(self, box_sizing: str = "border-box") -> "CSSBase":
        """Установить box-sizing: content-box, border-box"""
        self.styles["box-sizing"] = box_sizing
        return self

    def set_display(self, display: str) -> "CSSBase":
        """Установить display: block, inline, inline-block, flex, grid, none, etc."""
        self.styles["display"] = display
        return self

    def set_visibility(self, visibility: str) -> "CSSBase":
        """Установить visibility: visible, hidden, collapse"""
        self.styles["visibility"] = visibility
        return self

    def set_overflow(self, overflow: str) -> "CSSBase":
        """Установить overflow: visible, hidden, scroll, auto"""
        self.styles["overflow"] = overflow
        return self

    def set_overflow_x(self, overflow: str) -> "CSSBase":
        """Установить overflow-x"""
        self.styles["overflow-x"] = overflow
        return self

    def set_overflow_y(self, overflow: str) -> "CSSBase":
        """Установить overflow-y"""
        self.styles["overflow-y"] = overflow
        return self

    def set_overflow_wrap(self, overflow_wrap: str) -> "CSSBase":
        """Установить overflow-wrap: normal, break-word, anywhere"""
        self.styles["overflow-wrap"] = overflow_wrap
        return self

    # ============ ПОЗИЦИОНИРОВАНИЕ ============

    def set_position(self, position: str) -> "CSSBase":
        """Установить position: static, relative, absolute, fixed, sticky"""
        self.styles["position"] = position
        return self

    def set_top(self, top: str) -> "CSSBase":
        """Установить top"""
        self.styles["top"] = top
        return self

    def set_right(self, right: str) -> "CSSBase":
        """Установить right"""
        self.styles["right"] = right
        return self

    def set_bottom(self, bottom: str) -> "CSSBase":
        """Установить bottom"""
        self.styles["bottom"] = bottom
        return self

    def set_left(self, left: str) -> "CSSBase":
        """Установить left"""
        self.styles["left"] = left
        return self

    def set_z_index(self, z_index: Union[int, str]) -> "CSSBase":
        """Установить z-index"""
        self.styles["z-index"] = str(z_index)
        return self

    def set_float(self, float_val: str) -> "CSSBase":
        """Установить float: left, right, none"""
        self.styles["float"] = float_val
        return self

    def set_clear(self, clear: str) -> "CSSBase":
        """Установить clear: left, right, both, none"""
        self.styles["clear"] = clear
        return self

    # ============ FLEXBOX ============

    def set_flex_direction(self, direction: str) -> "CSSBase":
        """Установить flex-direction: row, row-reverse, column, column-reverse"""
        self.styles["flex-direction"] = direction
        return self

    def set_flex_wrap(self, wrap: str) -> "CSSBase":
        """Установить flex-wrap: nowrap, wrap, wrap-reverse"""
        self.styles["flex-wrap"] = wrap
        return self

    def set_flex_flow(self, flow: str) -> "CSSBase":
        """Установить flex-flow (сокращение для flex-direction и flex-wrap)"""
        self.styles["flex-flow"] = flow
        return self

    def set_justify_content(self, justify: str) -> "CSSBase":
        """
        Установить выравнивание по главной оси

        Args:
            justify: flex-start, center, flex-end, space-between, space-around, space-evenly
        """
        valid_values = ["flex-start", "center", "flex-end", "space-between", "space-around", "space-evenly"]
        if justify in valid_values:
            self.styles["justify-content"] = justify
        else:
            raise ValueError(f"Недопустимое значение justify-content: {justify}. " f"Допустимые значения: {', '.join(valid_values)}")
        return self

    def set_align_items(self, align: str) -> "CSSBase":
        """
        Установить выравнивание по поперечной оси
        Args:
            align: stretch, flex-start, center, flex-end, baseline
        """
        valid_values = ["stretch", "flex-start", "center", "flex-end", "baseline"]
        if align in valid_values:
            self.styles["align-items"] = align
        else:
            raise ValueError(f"Недопустимое значение align-items: {align}. " f"Допустимые значения: {', '.join(valid_values)}")
        return self

    def set_align_content(self, align: str) -> "CSSBase":
        """Установить align-content: flex-start, flex-end, center, space-between, space-around, stretch"""
        self.styles["align-content"] = align
        return self

    def set_align_self(self, align: str) -> "CSSBase":
        """Установить align-self: auto, flex-start, flex-end, center, baseline, stretch"""
        self.styles["align-self"] = align
        return self

    def set_flex_grow(self, grow: Union[int, str]) -> "CSSBase":
        """Установить flex-grow"""
        self.styles["flex-grow"] = str(grow)
        return self

    def set_flex_shrink(self, shrink: Union[int, str]) -> "CSSBase":
        """Установить flex-shrink"""
        self.styles["flex-shrink"] = str(shrink)
        return self

    def set_flex_basis(self, basis: str) -> "CSSBase":
        """Установить flex-basis: auto, 100px, 50%, etc."""
        self.styles["flex-basis"] = basis
        return self

    def set_flex(self, flex: str) -> "CSSBase":
        """Установить flex (сокращение для flex-grow, flex-shrink, flex-basis)"""
        self.styles["flex"] = flex
        return self

    def set_order(self, order: Union[int, str]) -> "CSSBase":
        """Установить order"""
        self.styles["order"] = str(order)
        return self

    def set_gap(self, gap: str) -> "CSSBase":
        """Установить gap (для flexbox и grid)"""
        self.styles["gap"] = gap
        return self

    def set_row_gap(self, gap: str) -> "CSSBase":
        """Установить row-gap"""
        self.styles["row-gap"] = gap
        return self

    def set_column_gap(self, gap: str) -> "CSSBase":
        """Установить column-gap"""
        self.styles["column-gap"] = gap
        return self

    # ============ GRID ============

    def set_grid_template_columns(self, columns: str) -> "CSSBase":
        """Установить grid-template-columns"""
        self.styles["grid-template-columns"] = columns
        return self

    def set_grid_template_rows(self, rows: str) -> "CSSBase":
        """Установить grid-template-rows"""
        self.styles["grid-template-rows"] = rows
        return self

    def set_grid_template_areas(self, areas: str) -> "CSSBase":
        """Установить grid-template-areas"""
        self.styles["grid-template-areas"] = areas
        return self

    def set_grid_template(self, template: str) -> "CSSBase":
        """Установить grid-template"""
        self.styles["grid-template"] = template
        return self

    def set_grid_column_start(self, column: str) -> "CSSBase":
        """Установить grid-column-start"""
        self.styles["grid-column-start"] = column
        return self

    def set_grid_column_end(self, column: str) -> "CSSBase":
        """Установить grid-column-end"""
        self.styles["grid-column-end"] = column
        return self

    def set_grid_row_start(self, row: str) -> "CSSBase":
        """Установить grid-row-start"""
        self.styles["grid-row-start"] = row
        return self

    def set_grid_row_end(self, row: str) -> "CSSBase":
        """Установить grid-row-end"""
        self.styles["grid-row-end"] = row
        return self

    def set_grid_area(self, area: str) -> "CSSBase":
        """Установить grid-area"""
        self.styles["grid-area"] = area
        return self

    def set_justify_items(self, justify: str) -> "CSSBase":
        """Установить justify-items (для grid)"""
        self.styles["justify-items"] = justify
        return self

    def set_align_items_grid(self, align: str) -> "CSSBase":
        """Установить align-items (для grid)"""
        self.styles["align-items"] = align
        return self

    def set_place_items(self, place: str) -> "CSSBase":
        """Установить place-items (сокращение для align-items и justify-items)"""
        self.styles["place-items"] = place
        return self

    # ============ ФОН ============

    def set_background_color(self, color: str) -> "CSSBase":
        """Установить background-color: #fff, rgb(255,255,255), rgba(255,255,255,0.5), etc."""
        self.styles["background-color"] = color
        return self

    def set_background_image(self, image: str) -> "CSSBase":
        """Установить background-image: url('image.jpg'), linear-gradient(), etc."""
        self.styles["background-image"] = f'url("{image}")'
        return self

    def set_background_repeat(self, repeat: str) -> "CSSBase":
        """Установить background-repeat: repeat, no-repeat, repeat-x, repeat-y"""
        self.styles["background-repeat"] = repeat
        return self

    def set_background_position(self, position: str) -> "CSSBase":
        """Установить background-position: center, top left, 50% 50%, etc."""
        self.styles["background-position"] = position
        return self

    def set_background_size(self, size: str) -> "CSSBase":
        """Установить background-size: cover, contain, auto, 100% 100%, etc."""
        self.styles["background-size"] = size
        return self

    def set_background_attachment(self, attachment: str) -> "CSSBase":
        """Установить background-attachment: scroll, fixed, local"""
        self.styles["background-attachment"] = attachment
        return self

    def set_background(self, background: str) -> "CSSBase":
        """Установить background (сокращенная запись)"""
        self.styles["background"] = background
        return self

    def set_background_clip(self, clip: str) -> "CSSBase":
        """Установить background-clip: border-box, padding-box, content-box"""
        self.styles["background-clip"] = clip
        return self

    def set_background_origin(self, origin: str) -> "CSSBase":
        """Установить background-origin: border-box, padding-box, content-box"""
        self.styles["background-origin"] = origin
        return self

    # ============ ГРАНИЦЫ ============

    def set_border(self, border: str) -> "CSSBase":
        """Установить border: 1px solid #000"""
        self.styles["border"] = border
        return self

    def set_border_width(self, width: str) -> "CSSBase":
        """Установить border-width: 1px, thin, medium, thick, etc."""
        self.styles["border-width"] = width
        return self

    def set_border_style(self, style: str) -> "CSSBase":
        """Установить border-style: solid, dashed, dotted, double, none, etc."""
        self.styles["border-style"] = style
        return self

    def set_border_color(self, color: str) -> "CSSBase":
        """Установить border-color: #000, red, rgb(0,0,0), etc."""
        self.styles["border-color"] = color
        return self

    def set_border_top(self, border: str) -> "CSSBase":
        """Установить border-top"""
        self.styles["border-top"] = border
        return self

    def set_border_right(self, border: str) -> "CSSBase":
        """Установить border-right"""
        self.styles["border-right"] = border
        return self

    def set_border_bottom(self, border: str) -> "CSSBase":
        """Установить border-bottom"""
        self.styles["border-bottom"] = border
        return self

    def set_border_left(self, border: str) -> "CSSBase":
        """Установить border-left"""
        self.styles["border-left"] = border
        return self

    def set_border_radius(self, radius: str) -> "CSSBase":
        """Установить border-radius: 5px, 50%, 10px 20px 30px 40px"""
        self.styles["border-radius"] = radius
        return self

    def set_border_top_left_radius(self, radius: str) -> "CSSBase":
        """Установить border-top-left-radius"""
        self.styles["border-top-left-radius"] = radius
        return self

    def set_border_top_right_radius(self, radius: str) -> "CSSBase":
        """Установить border-top-right-radius"""
        self.styles["border-top-right-radius"] = radius
        return self

    def set_border_bottom_left_radius(self, radius: str) -> "CSSBase":
        """Установить border-bottom-left-radius"""
        self.styles["border-bottom-left-radius"] = radius
        return self

    def set_border_bottom_right_radius(self, radius: str) -> "CSSBase":
        """Установить border-bottom-right-radius"""
        self.styles["border-bottom-right-radius"] = radius
        return self

    def set_border_collapse(self, collapse: str) -> "CSSBase":
        """Установить border-collapse: collapse, separate (для таблиц)"""
        self.styles["border-collapse"] = collapse
        return self

    def set_border_spacing(self, spacing: str) -> "CSSBase":
        """Установить border-spacing (для таблиц)"""
        self.styles["border-spacing"] = spacing
        return self

    def set_outline(self, outline: str) -> "CSSBase":
        """Установить outline: 1px solid red"""
        self.styles["outline"] = outline
        return self

    def set_outline_width(self, width: str) -> "CSSBase":
        """Установить outline-width"""
        self.styles["outline-width"] = width
        return self

    def set_outline_style(self, style: str) -> "CSSBase":
        """Установить outline-style"""
        self.styles["outline-style"] = style
        return self

    def set_outline_color(self, color: str) -> "CSSBase":
        """Установить outline-color"""
        self.styles["outline-color"] = color
        return self

    def set_outline_offset(self, offset: str) -> "CSSBase":
        """Установить outline-offset"""
        self.styles["outline-offset"] = offset
        return self

    # ============ ТЕНЬ ============

    def set_box_shadow(self, shadow: str) -> "CSSBase":
        """Установить box-shadow: 0 2px 5px rgba(0,0,0,0.2)"""
        self.styles["box-shadow"] = shadow
        return self

    def set_text_shadow(self, shadow: str) -> "CSSBase":
        """Установить text-shadow: 1px 1px 2px #000"""
        self.styles["text-shadow"] = shadow
        return self

    # ============ ТЕКСТ ============

    def set_color(self, color: str) -> "CSSBase":
        """Установить color: #000, red, rgb(0,0,0), etc."""
        self.styles["color"] = color
        return self

    def set_font_family(self, font_family: str) -> "CSSBase":
        """Установить font-family: Arial, sans-serif, 'Times New Roman', etc."""
        self.styles["font-family"] = font_family
        return self

    def set_font_size(self, font_size: str) -> "CSSBase":
        """Установить font-size: 16px, 1rem, 100%, etc."""
        self.styles["font-size"] = font_size
        return self

    def set_font_weight(self, font_weight: str) -> "CSSBase":
        """Установить font-weight: normal, bold, 400, 700, etc."""
        self.styles["font-weight"] = font_weight
        return self

    def set_font_style(self, font_style: str) -> "CSSBase":
        """Установить font-style: normal, italic, oblique"""
        self.styles["font-style"] = font_style
        return self

    def set_font_variant(self, font_variant: str) -> "CSSBase":
        """Установить font-variant: normal, small-caps"""
        self.styles["font-variant"] = font_variant
        return self

    def set_line_height(self, line_height: str) -> "CSSBase":
        """Установить line-height: 1.5, 24px, normal"""
        self.styles["line-height"] = line_height
        return self

    def set_text_align(self, text_align: str) -> "CSSBase":
        """Установить text-align: left, right, center, justify"""
        self.styles["text-align"] = text_align
        return self

    def set_text_decoration(self, text_decoration: str) -> "CSSBase":
        """Установить text-decoration: none, underline, overline, line-through"""
        self.styles["text-decoration"] = text_decoration
        return self

    def set_text_transform(self, text_transform: str) -> "CSSBase":
        """Установить text-transform: none, capitalize, uppercase, lowercase"""
        self.styles["text-transform"] = text_transform
        return self

    def set_letter_spacing(self, letter_spacing: str) -> "CSSBase":
        """Установить letter-spacing: 1px, normal"""
        self.styles["letter-spacing"] = letter_spacing
        return self

    def set_word_spacing(self, word_spacing: str) -> "CSSBase":
        """Установить word-spacing: 1px, normal"""
        self.styles["word-spacing"] = word_spacing
        return self

    def set_white_space(self, white_space: str) -> "CSSBase":
        """Установить white-space: normal, nowrap, pre, pre-wrap, pre-line"""
        self.styles["white-space"] = white_space
        return self

    def set_word_break(self, word_break: str) -> "CSSBase":
        """Установить word-break: normal, break-all, keep-all"""
        self.styles["word-break"] = word_break
        return self

    def set_word_wrap(self, word_wrap: str) -> "CSSBase":
        """Установить word-wrap: normal, break-word"""
        self.styles["word-wrap"] = word_wrap
        return self

    def set_text_overflow(self, text_overflow: str) -> "CSSBase":
        """Установить text-overflow: clip, ellipsis"""
        self.styles["text-overflow"] = text_overflow
        return self

    def set_text_indent(self, text_indent: str) -> "CSSBase":
        """Установить text-indent: 20px, 2em"""
        self.styles["text-indent"] = text_indent
        return self

    def set_vertical_align(self, vertical_align: str) -> "CSSBase":
        """Установить vertical-align: baseline, top, middle, bottom, sub, super"""
        self.styles["vertical-align"] = vertical_align
        return self

    def set_direction(self, direction: str) -> "CSSBase":
        """Установить direction: ltr, rtl"""
        self.styles["direction"] = direction
        return self

    def set_unicode_bidi(self, unicode_bidi: str) -> "CSSBase":
        """Установить unicode-bidi: normal, embed, bidi-override"""
        self.styles["unicode-bidi"] = unicode_bidi
        return self

    # ============ СТИЛЬ КУРСОРА ============

    def set_cursor(self, cursor: str) -> "CSSBase":
        """Установить cursor: pointer, default, text, move, not-allowed, etc."""
        self.styles["cursor"] = cursor
        return self

    def set_pointer_events(self, pointer_events: str) -> "CSSBase":
        """Установить pointer-events: auto, none"""
        self.styles["pointer-events"] = pointer_events
        return self

    def set_user_select(self, user_select: str) -> "CSSBase":
        """Установить user-select: auto, none, text, all"""
        self.styles["user-select"] = user_select
        return self

    # ============ СПИСКИ ============

    def set_list_style_type(self, list_style_type: str) -> "CSSBase":
        """Установить list-style-type: disc, circle, square, decimal, none"""
        self.styles["list-style-type"] = list_style_type
        return self

    def set_list_style_position(self, list_style_position: str) -> "CSSBase":
        """Установить list-style-position: inside, outside"""
        self.styles["list-style-position"] = list_style_position
        return self

    def set_list_style_image(self, list_style_image: str) -> "CSSBase":
        """Установить list-style-image: url('bullet.png')"""
        self.styles["list-style-image"] = list_style_image
        return self

    def set_list_style(self, list_style: str) -> "CSSBase":
        """Установить list-style (сокращенная запись)"""
        self.styles["list-style"] = list_style
        return self

    # ============ ТАБЛИЦЫ ============

    def set_table_layout(self, table_layout: str) -> "CSSBase":
        """Установить table-layout: auto, fixed"""
        self.styles["table-layout"] = table_layout
        return self

    def set_caption_side(self, caption_side: str) -> "CSSBase":
        """Установить caption-side: top, bottom"""
        self.styles["caption-side"] = caption_side
        return self

    def set_empty_cells(self, empty_cells: str) -> "CSSBase":
        """Установить empty-cells: show, hide"""
        self.styles["empty-cells"] = empty_cells
        return self

    # ============ АНИМАЦИИ И ПЕРЕХОДЫ ============

    def set_transition(self, transition: str) -> "CSSBase":
        """Установить transition: property duration timing-function delay"""
        self.styles["transition"] = transition
        return self

    def set_transition_property(self, property: str) -> "CSSBase":
        """Установить transition-property: all, opacity, transform, etc."""
        self.styles["transition-property"] = property
        return self

    def set_transition_duration(self, duration: str) -> "CSSBase":
        """Установить transition-duration: 0.3s, 500ms"""
        self.styles["transition-duration"] = duration
        return self

    def set_transition_timing_function(self, timing: str) -> "CSSBase":
        """Установить transition-timing-function: ease, linear, ease-in, ease-out, cubic-bezier()"""
        self.styles["transition-timing-function"] = timing
        return self

    def set_transition_delay(self, delay: str) -> "CSSBase":
        """Установить transition-delay: 0s, 1s"""
        self.styles["transition-delay"] = delay
        return self

    def set_animation(self, animation: str) -> "CSSBase":
        """Установить animation: name duration timing-function delay iteration-count direction fill-mode"""
        self.styles["animation"] = animation
        return self

    def set_animation_name(self, name: str) -> "CSSBase":
        """Установить animation-name"""
        self.styles["animation-name"] = name
        return self

    def set_animation_duration(self, duration: str) -> "CSSBase":
        """Установить animation-duration"""
        self.styles["animation-duration"] = duration
        return self

    def set_animation_timing_function(self, timing: str) -> "CSSBase":
        """Установить animation-timing-function"""
        self.styles["animation-timing-function"] = timing
        return self

    def set_animation_delay(self, delay: str) -> "CSSBase":
        """Установить animation-delay"""
        self.styles["animation-delay"] = delay
        return self

    def set_animation_iteration_count(self, count: str) -> "CSSBase":
        """Установить animation-iteration-count: infinite, 1, 2, etc."""
        self.styles["animation-iteration-count"] = count
        return self

    def set_animation_direction(self, direction: str) -> "CSSBase":
        """Установить animation-direction: normal, reverse, alternate, alternate-reverse"""
        self.styles["animation-direction"] = direction
        return self

    def set_animation_fill_mode(self, fill_mode: str) -> "CSSBase":
        """Установить animation-fill-mode: none, forwards, backwards, both"""
        self.styles["animation-fill-mode"] = fill_mode
        return self

    def set_animation_play_state(self, play_state: str) -> "CSSBase":
        """Установить animation-play-state: running, paused"""
        self.styles["animation-play-state"] = play_state
        return self

    # ============ ТРАНСФОРМАЦИИ ============

    def set_transform(self, transform: str) -> "CSSBase":
        """Установить transform: translate(), rotate(), scale(), skew(), matrix()"""
        self.styles["transform"] = transform
        return self

    def set_transform_origin(self, origin: str) -> "CSSBase":
        """Установить transform-origin: center, top left, 50% 50%, etc."""
        self.styles["transform-origin"] = origin
        return self

    def set_transform_style(self, style: str) -> "CSSBase":
        """Установить transform-style: flat, preserve-3d"""
        self.styles["transform-style"] = style
        return self

    def set_perspective(self, perspective: str) -> "CSSBase":
        """Установить perspective: 100px, none"""
        self.styles["perspective"] = perspective
        return self

    def set_perspective_origin(self, origin: str) -> "CSSBase":
        """Установить perspective-origin"""
        self.styles["perspective-origin"] = origin
        return self

    def set_backface_visibility(self, visibility: str) -> "CSSBase":
        """Установить backface-visibility: visible, hidden"""
        self.styles["backface-visibility"] = visibility
        return self

    # ============ ПРОЧИЕ СВОЙСТВА ============

    def set_opacity(self, opacity: Union[float, str]) -> "CSSBase":
        """Установить opacity: 0.5, 1, 0"""
        self.styles["opacity"] = str(opacity)
        return self

    def set_filter(self, filter: str) -> "CSSBase":
        """Установить filter: blur(), brightness(), contrast(), grayscale(), etc."""
        self.styles["filter"] = filter
        return self

    def set_backdrop_filter(self, filter: str) -> "CSSBase":
        """Установить backdrop-filter"""
        self.styles["backdrop-filter"] = filter
        return self

    def set_mix_blend_mode(self, blend_mode: str) -> "CSSBase":
        """Установить mix-blend-mode: normal, multiply, screen, overlay, etc."""
        self.styles["mix-blend-mode"] = blend_mode
        return self

    def set_isolation(self, isolation: str) -> "CSSBase":
        """Установить isolation: auto, isolate"""
        self.styles["isolation"] = isolation
        return self

    def set_object_fit(self, object_fit: str) -> "CSSBase":
        """Установить object-fit: fill, contain, cover, none, scale-down"""
        self.styles["object-fit"] = object_fit
        return self

    def set_object_position(self, position: str) -> "CSSBase":
        """Установить object-position"""
        self.styles["object-position"] = position
        return self

    def set_resize(self, resize: str) -> "CSSBase":
        """Установить resize: none, both, horizontal, vertical"""
        self.styles["resize"] = resize
        return self

    def set_scroll_behavior(self, behavior: str) -> "CSSBase":
        """Установить scroll-behavior: auto, smooth"""
        self.styles["scroll-behavior"] = behavior
        return self

    def set_scrollbar_width(self, width: str) -> "CSSBase":
        """Установить scrollbar-width: auto, thin, none"""
        self.styles["scrollbar-width"] = width
        return self

    def set_scrollbar_color(self, color: str) -> "CSSBase":
        """Установить scrollbar-color: thumb-color track-color"""
        self.styles["scrollbar-color"] = color
        return self

    def set_writing_mode(self, mode: str) -> "CSSBase":
        """Установить writing-mode: horizontal-tb, vertical-rl, vertical-lr"""
        self.styles["writing-mode"] = mode
        return self

    def set_text_orientation(self, orientation: str) -> "CSSBase":
        """Установить text-orientation: mixed, upright, sideways"""
        self.styles["text-orientation"] = orientation
        return self

    # ============ CSS VARIABLES ============

    def set_css_variable(self, name: str, value: str) -> "CSSBase":
        """Установить CSS переменную: --main-color: #ff0000"""
        var_name = f"--{name.lstrip('-')}"
        self.styles[var_name] = value
        return self

    def get_css_variable(self, name: str) -> Optional[str]:
        """Получить значение CSS переменной"""
        var_name = f"--{name.lstrip('-')}"
        return self.styles.get(var_name)

    # ============ УТИЛИТНЫЕ МЕТОДЫ ============

    def add_styles_from_string(self, style):
        """
        Добавляет стили в словарь styles.

        Parameters
        ----------
        style : str
        """
        new_styles = self.parse_style_string(style)
        for style_name, style_value in new_styles.items():
            self.styles[style_name] = style_value

    def add_style(self, key: str, value: str) -> "CSSBase":
        """Установить произвольный стиль"""
        self.styles[key] = value
        return self

    def get_style(self, key: str) -> Optional[str]:
        """Получить значение стиля"""
        return self.styles.get(key)

    def remove_style(self, key: str) -> "CSSBase":
        """Удалить стиль"""
        if key in self.styles:
            del self.styles[key]
        return self

    def has_style(self, key: str) -> bool:
        """Проверить наличие стиля"""
        return key in self.styles

    def clear_styles(self) -> "CSSBase":
        """Очистить все стили"""
        self.styles.clear()
        return self

    def merge_styles(self, styles: Dict[str, str]) -> "CSSBase":
        """Объединить стили"""
        self.styles.update(styles)
        return self

    def get_styles_string(self, space=False) -> str:
        style_str_list = []

        for style_name, style_value in self.styles.items():
            if space:
                style_str_list.append(f"\t{style_name}:{style_value};\n")
            else:
                style_str_list.append(f"{style_name}:{style_value};")
        return " ".join(style_str_list)

    def copy_styles(self) -> Dict[str, str]:
        """Создать копию стилей"""
        return self.styles.copy()
