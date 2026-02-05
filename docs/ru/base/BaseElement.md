# BaseElement

`BaseElement` - это расширенный класс для создания HTML элементов с поддержкой CSS стилей через объекты CSSBase и CSSSelectors. Класс наследуется от [HTMLElement](HTMLElement.md) и добавляет возможности для управления внешними CSS стилями, автоматической генерации классов и гибкого рендеринга HTML.

## Наследование

- Родительский класс: [HTMLElement](HTMLElement.md)
- Добавляет: Управление CSS стилями через объекты, автоматическое связывание классов со стилями

## Атрибуты класса

| Атрибут          | Тип          | Описание                                      | Наследование   |
| ---------------- | ------------ | --------------------------------------------- | -------------- |
| object\*styles   | CSSBase      | Объект для управления CSS стилями элемента    | Новый          |
| selectors_styles | CSSSelectors | Контейнер для CSS селекторов и их стилей      | Новый          |
| tag              | str          | HTML тег элемента (div, span, button и т.д.)  | Новый          |
| self_closing     | bool         | Флаг самозакрывающегося тега (img, br, input) | Новый          |
| inline_styles    | CSSInline    | Inline стили элемента (наследуется)           | Из HTMLElement |
| class\*          | list[str]    | Список CSS классов (наследуется)              | Из HTMLElement |
| object_name      | str          | Имя объекта (наследуется)                     | Из HTMLElement |
| object_type      | str          | Тип объекта (наследуется)                     | Из HTMLElement |

## Конструктор

### **init**(tag="", self_closing: bool = False, object_name=None, style=None, boolean_attributes=[], \*\*kwargs)

Создаёт новый базовый HTML элемент с поддержкой CSS стилей.

Параметры:

- tag (str): HTML тег элемента (например, "div", "span", "button"). По умолчанию пустая строка
- self_closing (bool): Если True, элемент будет самозакрывающимся. По умолчанию False
- object_name (опционально): Имя/идентификатор элемента
- style (опционально): CSS строка для inline стилей
- boolean_attributes (опционально): Список булевых атрибутов
- \*\*kwargs: Дополнительные HTML атрибуты

Примеры:

```python
# Простой div элемент
div_element = BaseElement(tag="div")
# Самозакрывающийся элемент (img)
img_element = BaseElement(
    tag="img",
    self_closing=True,
    src="image.jpg",
    alt="Description"
)
# Элемент со стилями и атрибутами
button = BaseElement(
    tag="button",
    object_name="submitBtn",
    style="padding: 10px;",
    class_="btn-primary",
    onclick="submitForm()",
    disabled=True
)
```

## Основные методы

### get_html(content: str = "", tab: int = 0) -> str

Генерирует HTML строку элемента.

Параметры:

- content (str): Внутреннее содержимое элемента. По умолчанию пустая строка
- tab (int): Уровень отступа для форматирования. По умолчанию 0

Примеры:

```python
# Простой элемент
element = BaseElement(tag="div", object_name="container")
html = element.get_html()
# Результат: <div class="container" ></div>

# Элемент с содержимым
element = BaseElement(tag="p", object_name="description")
html = element.get_html(content="Hello World")
# Результат: <p class="description" >Hello World</p>

# Самозакрывающийся элемент
element = BaseElement(tag="img", self_closing=True, src="photo.jpg")
html = element.get_html()
# Результат: <img src="photo.jpg" >

# С форматированием отступов
element = BaseElement(tag="div", object_name="wrapper")
html = element.get_html(content="\n    <p>Content</p>\n", tab=1)
# Результат: <div class="wrapper" >
#     <p>Content</p>
#     </div>
```

### get_styles(space: bool = True) -> dict

Генерирует словарь CSS стилей для элемента и связывает их с классами.

Параметры:

- space (bool): Если True, форматирует CSS с пробелами и переносами

Возвращает:

- Словарь CSS стилей в формате {селектор: css_стили}

Примеры:

```python
element = BaseElement(tag="div", object_name="myElement")
# Добавление стилей через CSSBase
element.object_styles.set_width("100px")\
 .set_height("100px")\
 .set_background_color("red")
# Получение стилей
styles = element.get_styles()
# Результат: {'.myElement': 'width:100px;height:100px;background-color:red;'}
# С форматированием
formatted_styles = element.get_styles(space=True)
# Результат: {'.myElement': ' width: 100px;\n height: 100px;\n background-color: red;'}
```

## Примеры использования

### Пример 1: Модальное окно с анимацией

```python
modal = BaseElement(
    tag="div",
    object_name="modalOverlay",
    role="dialog",
    aria_modal="true",
    aria_labelledby="modalTitle",
    aria_hidden="true"
)

# Стили оверлея
modal.object_styles.set_position("fixed")\
                   .set_top("0")\
                   .set_left("0")\
                   .set_width("100%")\
                   .set_height("100%")\
                   .set_background_color("rgba(0,0,0,0.5)")\
                   .set_display("flex")\
                   .set_justify_content("center")\
                   .set_align_items("center")\
                   .set_z_index("1000")\
                   .set_opacity("0")\
                   .set_visibility("hidden")\
                   .set_transition("opacity 0.3s, visibility 0.3s")

# Анимация показа
show_styles = CSSBase()
show_styles.set_opacity("1").set_visibility("visible")
modal.selectors_styles.add_selector("modalOverlay.show").merge_styles(show_styles.styles)

# Контент модального окна
modal_content = BaseElement(
    tag="div",
    object_name="modalContent",
    role="document"
)

modal_content.object_styles.set_background_color("white")\
                           .set_padding("30px")\
                           .set_border_radius("8px")\
                           .set_max_width("500px")\
                           .set_width("90%")\
                           .set_transform("scale(0.9)")\
                           .set_transition("transform 0.3s")

# Анимация контента
content_show_styles = CSSBase()
content_show_styles.set_transform("scale(1)")
modal_content.selectors_styles.add_selector("modalContent.show").merge_styles(content_show_styles.styles)
```

### Пример 2: Навигационное меню

```python
nav = BaseElement(
    tag="nav",
    object_name="mainNav",
    role="navigation",
    aria_label="Main navigation"
)

# Стили навигации
nav.object_styles.set_background_color("#333")\
                 .set_padding("15px 0")\
                 .set_display("flex")\
                 .set_justify_content("center")\
                 .set_gap("30px")

# Создание элементов меню
menu_items = ["Home", "Products", "About", "Contact"]
menu_content = ""

for item in menu_items:
    menu_item = BaseElement(
        tag="a",
        object_name=f"nav{item}",
        href=f"/{item.lower()}",
        aria_current="page" if item == "Home" else None
    )

    # Стили пункта меню
    menu_item.object_styles.set_color("white")\
                           .set_text_decoration("none")\
                           .set_padding("10px")\
                           .set_border_radius("4px")\
                           .set_transition("background-color 0.3s")

    # Hover эффект
    menu_item.selectors_styles.add_selector(f"nav{item}:hover").set_background_color("#555")

    menu_content += menu_item.get_html(content=item) + "\n"

# Генерация меню
nav_html = nav.get_html(content=menu_content, tab=1)
```
