# CSSBase

`CSSBase` - это базовый класс для управления CSS-стилями HTML элементов. Класс предоставляет методы для установки, получения и управления всеми основными CSS свойствами в объектно-ориентированном стиле.

---

## Импорт

```python
from LayoutML.base.css import CSSBase
```

## Конструктор

### **init**(self, type="tag", style=None):

Параметры:

| Параметр | Тип | По умолчанию | Описание                                                          |
| -------- | --- | ------------ | ----------------------------------------------------------------- |
| type     | str | "tag"        | Тип элемента.                                                     |
| style    | str | None         | CSS-строка стилей для парсинга. Формат: "key:value; key2:value2". |

Пример:

```python
# С пустыми стилями
element = CSSBase()
# С начальными стилями
element = CSSBase(style="width: 100px; height: 200px; color: #333;")
```

## Методы CSS-свойств

### Блочная модель

| Метод                     | Описание                  | Пример                       |
| ------------------------- | ------------------------- | ---------------------------- |
| set_width(value)          | Установить ширину         | set_width("300px")           |
| set_height(value)         | Установить высоту         | set_height("200px")          |
| set_min_width(value)      | Минимальная ширина        | set_min_width("100px")       |
| set_min_height(value)     | Минимальная высота        | set_min_height("50px")       |
| set_max_width(value)      | Максимальная ширина       | set_max_width("500px")       |
| set_max_height(value)     | Максимальная высота       | set_max_height("400px")      |
| set_margin(value)         | Внешние отступы           | set_margin("10px 20px")      |
| set_margin_top(value)     | Верхний отступ            | set_margin_top("10px")       |
| set_margin_right(value)   | Правый отступ             | set_margin_right("15px")     |
| set_margin_bottom(value)  | Нижний отступ             | set_margin_bottom("10px")    |
| set_margin_left(value)    | Левый отступ              | set_margin_left("15px")      |
| set_padding(value)        | Внутренние отступы        | set_padding("20px")          |
| set_padding_top(value)    | Верхний внутренний отступ | set_padding_top("10px")      |
| set_padding_right(value)  | Правый внутренний отступ  | set_padding_right("15px")    |
| set_padding_bottom(value) | Нижний внутренний отступ  | set_padding_bottom("10px")   |
| set_padding_left(value)   | Левый внутренний отступ   | set_padding_left("15px")     |
| set_box_sizing(value)     | Модель бокса              | set_box_sizing("border-box") |
| set_display(value)        | Тип отображения           | set_display("flex")          |
| set_visibility(value)     | Видимость                 | set_visibility("hidden")     |
| set_overflow(value)       | Переполнение              | set_overflow("auto")         |

### Позиционирование

| Метод               | Описание             | Пример                   |
| ------------------- | -------------------- | ------------------------ |
| set_position(value) | Тип позиционирования | set_position("relative") |
| set_top(value)      | Отступ сверху        | set_top("10px")          |
| set_right(value)    | Отступ справа        | set_right("20px")        |
| set_bottom(value)   | Отступ снизу         | set_bottom("30px")       |
| set_left(value)     | Отступ слева         | set_left("40px")         |
| set_z_index(value)  | Z-индекс             | set_z_index(100)         |
| set_float(value)    | Обтекание            | set_float("left")        |
| set_clear(value)    | Очистка обтекания    | set_clear("both")        |

### Flexbox

| Метод                      | Описание                          | Пример                             |
| -------------------------- | --------------------------------- | ---------------------------------- |
| set_flex_direction(value)  | Направление flex                  | set_flex_direction("row")          |
| set_flex_wrap(value)       | Перенос flex-элементов            | set_flex_wrap("wrap")              |
| set_flex_flow(value)       | Сокращение направления и переноса | set_flex_flow("row wrap")          |
| set_justify_content(value) | Выравнивание по главной оси       | set_justify_content("center")      |
| set_align_items(value)     | Выравнивание по поперечной оси    | set_align_items("center")          |
| set_align_content(value)   | Выравнивание строк                | set_align_content("space-between") |
| set_align_self(value)      | Индивидуальное выравнивание       | set_align_self("flex-start")       |
| set_flex_grow(value)       | Коэффициент увеличения            | set_flex_grow(1)                   |
| set_flex_shrink(value)     | Коэффициент сжатия                | set_flex_shrink(0)                 |
| set_flex_basis(value)      | Базовый размер                    | set_flex_basis("auto")             |
| set_flex(value)            | Сокращенная запись                | set_flex("1 0 auto")               |
| set_order(value)           | Порядок элемента                  | set_order(2)                       |
| set_gap(value)             | Расстояние между элементами       | set_gap("10px")                    |

### Grid

| Метод                            | Описание                 | Пример                                                     |
| -------------------------------- | ------------------------ | ---------------------------------------------------------- |
| set_grid_template_columns(value) | Шаблон колонок           | set_grid_template_columns("1fr 2fr 1fr")                   |
| set_grid_template_rows(value)    | Шаблон строк             | set_grid_template_rows("100px auto")                       |
| set_grid_template_areas(value)   | Области шаблона          | set_grid_template_areas("header header" "sidebar content") |
| set_grid_template(value)         | Сокращенная запись       | set_grid_template("100px auto / 1fr 2fr")                  |
| set_grid_column_start(value)     | Начало колонки           | set_grid_column_start("2")                                 |
| set_grid_column_end(value)       | Конец колонки            | set_grid_column_end("4")                                   |
| set_grid_row_start(value)        | Начало строки            | set_grid_row_start("1")                                    |
| set_grid_row_end(value)          | Конец строки             | set_grid_row_end("3")                                      |
| set_grid_area(value)             | Область grid             | set_grid_area("header")                                    |
| set_justify_items(value)         | Выравнивание элементов   | set_justify_items("center")                                |
| set_place_items(value)           | Сокращенное выравнивание | set_place_items("center center")                           |

### Фон

| Метод                            | Описание                 | Пример                                                   |
| -------------------------------- | ------------------------ | -------------------------------------------------------- |
| set_background_color(value)      | Цвет фона                | set_background_color("#f0f0f0")                          |
| set_background_image(value)      | Фоновое изображение      | set_background_image("url('bg.jpg')")                    |
| set_background_repeat(value)     | Повторение фона          | set_background_repeat("no-repeat")                       |
| set_background_position(value)   | Позиция фона             | set_background_position("center")                        |
| set_background_size(value)       | Размер фона              | set_background_size("cover")                             |
| set_background_attachment(value) | Прикрепление фона        | set_background_attachment("fixed")                       |
| set_background(value)            | Сокращенная запись       | set_background("#f0f0f0 url('bg.jpg') no-repeat center") |
| set_background_clip(value)       | Область отображения фона | set_background_clip("content-box")                       |
| set_background_origin(value)     | Начало координат фона    | set_background_origin("padding-box")                     |

### Границы

| Метод                                 | Описание            | Пример                                |
| ------------------------------------- | ------------------- | ------------------------------------- |
| set_border(value)                     | Граница set_border  | ("1px solid #000")                    |
| set_border_width(value)               | Ширина границы      | set_border_width("2px")               |
| set_border_style(value)               | Стиль границы       | set_border_style("dashed")            |
| set_border_color(value)               | Цвет границы        | set_border_color("#ccc")              |
| set_border_top(value)                 | Верхняя граница     | set_border_top("2px solid red")       |
| set_border_right(value)               | Правая граница      | set_border_right("1px dotted #999")   |
| set_border_bottom(value)              | Нижняя граница      | set_border_bottom("3px double blue")  |
| set_border_left(value)                | Левая граница       | set_border_left("1px solid green")    |
| set_border_radius(value)              | Скругление углов    | set_border_radius("10px")             |
| set_border_top_left_radius(value)     | Левый верхний угол  | set_border_top_left_radius("5px")     |
| set_border_top_right_radius(value)    | Правый верхний угол | set_border_top_right_radius("5px")    |
| set_border_bottom_left_radius(value)  | Левый нижний угол   | set_border_bottom_left_radius("5px")  |
| set_border_bottom_right_radius(value) | Правый нижний угол  | set_border_bottom_right_radius("5px") |
| set_outline(value)                    | Контур set_outline  | ("2px dashed red")                    |

### Текст

| Метод                      | Описание              | Пример                               |
| -------------------------- | --------------------- | ------------------------------------ |
| set_color(value)           | Цвет текста           | set_color("#333")                    |
| set_font_family(value)     | Шрифт                 | set_font_family("Arial, sans-serif") |
| set_font_size(value)       | Размер шрифта         | set_font_size("16px")                |
| set_font_weight(value)     | Насыщенность шрифта   | set_font_weight("bold")              |
| set_font_style(value)      | Стиль шрифта          | set_font_style("italic")             |
| set_line_height(value)     | Межстрочный интервал  | set_line_height("1.5")               |
| set_text_align(value)      | Выравнивание текста   | set_text_align("center")             |
| set_text_decoration(value) | Декорация текста      | set_text_decoration("underline")     |
| set_text_transform(value)  | Трансформация текста  | set_text_transform("uppercase")      |
| set_letter_spacing(value)  | Межбуквенный интервал | set_letter_spacing("1px")            |
| set_word_spacing(value)    | Межсловный интервал   | set_word_spacing("2px")              |

### Анимации и переходы

| Метод                                 | Описание                 | Пример                                        |
| ------------------------------------- | ------------------------ | --------------------------------------------- |
| set_transition(value)                 | Переход                  | set_transition("all 0.3s ease")               |
| set_transition_property(value)        | Свойство перехода        | set_transition_property("opacity")            |
| set_transition_duration(value)        | Длительность перехода    | set_transition_duration("0.5s")               |
| set_transition_timing_function(value) | Функция времени          | set_transition_timing_function("ease-in-out") |
| set_transition_delay(value)           | Задержка перехода        | set_transition_delay("0.1s")                  |
| set_animation(value)                  | Анимация                 | set_animation("slide 2s infinite")            |
| set_animation_name(value)             | Имя анимации             | set_animation_name("fadeIn")                  |
| set_animation_duration(value)         | Длительность анимации    | set_animation_duration("1s")                  |
| set_animation_timing_function(value)  | Функция времени анимации | set_animation_timing_function("linear")       |
| set_animation_delay(value)            | Задержка анимации        | set_animation_delay("0.5s")                   |

### Трансформации

| Метод                          | Описание                   | Пример                             |
| ------------------------------ | -------------------------- | ---------------------------------- |
| set_transform(value)           | Трансформация              | set_transform("rotate(45deg)")     |
| set_transform_origin(value)    | Начало трансформации       | set_transform_origin("center")     |
| set_transform_style(value)     | Стиль трансформации        | set_transform_style("preserve-3d") |
| set_perspective(value)         | Перспектива                | set_perspective("500px")           |
| set_backface_visibility(value) | Видимость обратной стороны | set_backface_visibility("hidden")  |

### Прочие свойства

| Метод                  | Описание         | Пример                                      |
| ---------------------- | ---------------- | ------------------------------------------- |
| set_opacity(value)     | Прозрачность     | set_opacity(0.5)                            |
| set_filter(value)      | Фильтры          | set_filter("blur(5px)")                     |
| set_box_shadow(value)  | Тень блока       | set_box_shadow("0 2px 5px rgba(0,0,0,0.2)") |
| set_text_shadow(value) | Тень текста      | set_text_shadow("1px 1px 2px #000")         |
| set_cursor(value)      | Курсор           | set_cursor("pointer")                       |
| set_user_select(value) | Выделение текста | set_user_select("none")                     |

### Утилитные методы

Управление стилями

```python
# Добавление стилей из строки
element.add_styles_from_string("width: 100px; height: 200px; color: red;")
# Установка произвольного стиля
element.add_style("custom-property", "value")
# Получение значения стиля
width = element.get_style("width")
# Проверка наличия стиля
has_width = element.has_style("width")
# Удаление стиля
element.remove_style("width")
# Очистка всех стилей
element.clear_styles()
# Объединение стилей из словаря
element.merge_styles({"margin": "10px", "padding": "20px"})
# Копирование стилей
styles_copy = element.copy_styles()
```

### Работа со строками стилей

```python
# Получение строки стилей (компактный формат)
style_string = element.get_styles_string()
# width:300px;height:200px;color:#333;
# Получение строки стилей (с отступами)
formatted_style = element.get_styles_string(space=True)
#   width:300px;
#   height:200px;
#   color:#333;
```

### CSS переменные

```python
# Установка CSS переменной
element.set_css_variable("main-color", "#ff0000")
element.set_css_variable("padding-size", "20px")
# Получение CSS переменной
color = element.get_css_variable("main-color")  # "#ff0000"
```
