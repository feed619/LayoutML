# ListElement

`ListElement` - это базовый класс для создания HTML элементов списков. Класс наследуется от [BaseElement](../base/BaseElement.md) и предоставляет общую функциональность для работы с упорядоченными (<ol>) и неупорядоченными (<ul>) списками, включая управление элементами списка и их рендеринг.

---

## Импорт

```python
from layoutML.list. import ListElement
```

## Назначение

Класс предназначен для использования в качестве родительского для конкретных типов списков:

- UnorderedList (маркированный список <ul>)
- OrderedList (нумерованный список <ol>)

## Наследование

- Родительский класс: BaseElement
- Тип элемента: Зависит от переданного тега (ul или ol)
- Назначение: Создание и управление элементами списков

## Атрибуты класса

| Атрибут | Тип  | Описание         | Значение по умолчанию |
| ------- | ---- | ---------------- | --------------------- |
| items   | list | Список элементов | []                    |

## Конструктор

### **init**(tag, items=None, object_name=None, style=None, boolean_attributes=[], \*\*kwargs)

Создаёт новый элемент списка с указанными параметрами.

Параметры:

- tag (str): HTML тег списка (ul или ol). Обязательный параметр
- items (list): Начальные элементы списка. По умолчанию None
- object_name (опционально): Имя/идентификатор элемента
- style (опционально): CSS строка для inline стилей
- boolean_attributes (опционально): Список булевых атрибутов
- \*_kwargs: Дополнительные HTML атрибуты (id, class\_, aria-_ и т.д.)

Автоматически устанавливаемые свойства:

- self_closing: False (не самозакрывающийся тег)
- items: список элементов списка

Примеры:

```python
# Неупорядоченный список
ul = ListElement(tag="ul", items=["Пункт 1", "Пункт 2", "Пункт 3"])
# Упорядоченный список с начальными элементами
ol = ListElement(
    tag="ol",
    items=["Первый", "Второй", "Третий"],
    class_="numbered-list"
)
# Пустой список с последующим добавлением элементов
list_element = ListElement(tag="ul", object_name="myList")
```

## Основные методы

### add_item(item)

Добавляет элемент в список.

Параметры:

- item (str или BaseElement): Добавляемый элемент. Может быть строкой или объектом, наследуемым от BaseElement

```python
list_element = ListElement(tag="ul")
# Добавление строкового элемента
list_element.add_item("Простой текст")
# Добавление HTML элемента
from layoutml import Anchor
link_item = Anchor(href="/page", text="Ссылка")
list_element.add_item(link_item)
```

## Примеры использования

### Создание маркированного списка

```python
from layoutml import UnorderedList
# Через конструктор
ul = UnorderedList(items=["Яблоко", "Банан", "Апельсин"])
# С добавлением элементов
ul = UnorderedList()
ul.add_item("Первый пункт")
ul.add_item("Второй пункт")
ul.add_item("Третий пункт")
```

### Создание нумерованного списка

```python
from layoutml import OrderedList
# Через конструктор
ol = OrderedList(items=["Первый", "Второй", "Третий"])
# С настройками
ol = OrderedList(
    items=["Шаг 1", "Шаг 2", "Шаг 3"],
    class_="steps",
    start="1"
)
```

### Вложенные списки

```python
from layoutml import UnorderedList, ListElement
# Внешний список
main_list = UnorderedList()
# Первый пункт с вложенным списком
item1 = "Фрукты"
nested_list1 = UnorderedList(items=["Яблоко", "Груша", "Банан"])
main_list.add_item(item1)
main_list.add_item(nested_list1)  # Добавляем вложенный список как элемент
# Второй пункт с вложенным списком
item2 = "Овощи"
nested_list2 = UnorderedList(items=["Помидор", "Огурец", "Морковь"])
main_list.add_item(item2)
main_list.add_item(nested_list2)
html = main_list.get_html()
```

### Списки со сложным содержимым

```python
from layoutml import UnorderedList, Anchor, Span, Image
menu = UnorderedList(class_="nav-menu")
# Ссылка с иконкой
home = Anchor(href="/", text="🏠 Главная")
menu.add_item(home)
# Ссылка с описанием
about_container = Span()
about_link = Anchor(href="/about", text="О нас")
about_desc = Span(text=" (подробнее о компании)", class_="description")
about_container.get_html(content=f"{about_link.get_html()} {about_desc.get_html()}")
menu.add_item(about_container)

# Изображение-ссылка
logo_link = Anchor(href="/")
logo_img = Image(src="logo.png", alt="Логотип")
logo_link.get_html(content=logo_img.get_html())
menu.add_item(logo_link)
```

### Стилизованные списки

```python
from layoutml import UnorderedList
styled_list = UnorderedList(
    items=["Пункт 1", "Пункт 2", "Пункт 3"],
    object_name="styledList"
)
# Inline стили
styled_list.inline_styles.set_list_style_type("none")\
                         .set_padding_left("0")

# Стили для элементов списка
styled_list.selectors_styles.add_selector("styledList li")\
    .set_padding("8px 12px")\
    .set_margin_bottom("5px")\
    .set_background_color("#f8f9fa")\
    .set_border_radius("4px")

# Стили для маркеров (замена стандартных)
styled_list.selectors_styles.add_selector("styledList li::before")\
    .set_content("'✓ '")\
    .set_color("#28a745")\
    .set_font_weight("bold")
```

### Горизонтальное меню

```python
from layoutml import UnorderedList
horizontal_menu = UnorderedList(
    items=[
        Anchor(href="/", text="Главная"),
        Anchor(href="/about", text="О нас"),
        Anchor(href="/services", text="Услуги"),
        Anchor(href="/contact", text="Контакты")
    ],
    class_="horizontal-nav"
)
# Стили для горизонтального меню
horizontal_menu.object_styles.set_display("flex")\
                             .set_list_style_type("none")\
                             .set_padding("0")\
                             .set_margin("0")\
                             .set_gap("20px")
horizontal_menu.selectors_styles.add_selector(".horizontal-nav li")\
    .set_display("inline-block")
horizontal_menu.selectors_styles.add_selector(".horizontal-nav a")\
    .set_text_decoration("none")\
    .set_color("#333")\
    .set_padding("10px 15px")\
    .set_border_radius("4px")\
    .set_transition("background-color 0.3s")
horizontal_menu.selectors_styles.add_selector(".horizontal-nav a:hover")\
    .set_background_color("#007bff")\
    .set_color("white")
```

### Список с кастомными маркерами

```python
from layoutml import UnorderedList
custom_list = UnorderedList(
    items=[
        "Задача 1: Создать проект",
        "Задача 2: Написать код",
        "Задача 3: Протестировать",
        "Задача 4: Задеплоить"
    ],
    class_="task-list"
)
# Кастомные маркеры через CSS
custom_list.selectors_styles.add_selector(".task-list")\
    .set_list_style_type("none")\
    .set_padding_left("0")
custom_list.selectors_styles.add_selector(".task-list li")\
    .set_padding("8px 0 8px 30px")\
    .set_position("relative")
custom_list.selectors_styles.add_selector(".task-list li::before")\
    .set_content("'☐ '")\
    .set_position("absolute")\
    .set_left("0")\
    .set_color("#007bff")\
    .set_font_size("18px")
```

### Список определений (через отдельные классы)

```python
from layoutml import BaseElement
# Для списков определений (<dl>) нужно использовать отдельный подход
dl = BaseElement(tag="dl", class_="definition-list")
terms_and_defs = [
    ("HTML", "Язык разметки гипертекста"),
    ("CSS", "Каскадные таблицы стилей"),
    ("Python", "Язык программирования")
]
for term, definition in terms_and_defs:
    dt = BaseElement(tag="dt")
    dt.get_html(content=term)
    dd = BaseElement(tag="dd")
    dd.get_html(content=definition)

    dl.add_element(dt)
    dl.add_element(dd)
```

### Динамическое создание списка из данных

```python
from layoutml import UnorderedList, Anchor
def create_nav_list(items):
    """Создаёт навигационный список из данных"""
    nav = UnorderedList(class_="dynamic-nav")

    for item in items:
        if isinstance(item, dict):
            link = Anchor(
                href=item.get("url", "#"),
                text=item.get("title", "Ссылка")
            )
            nav.add_item(link)
        else:
            nav.add_item(str(item))

    return nav

# Данные для меню
menu_items = [
    {"title": "Главная", "url": "/"},
    {"title": "Продукты", "url": "/products"},
    {"title": "О компании", "url": "/about"},
    {"title": "Контакты", "url": "/contact"}
]
# Создание меню
main_menu = create_nav_list(menu_items)
```
