# OrderedList

`OrderedList` - это специализированный класс для создания HTML маркированных (ненумерованных) списков <ul>. Класс наследуется от [ListElement](ListElement.md) и предназначен для создания списков, где порядок элементов не имеет значения (например, списки товаров, меню, категории, характеристики).

---

## Импорт

```python
from layoutML.elements.list import OrderedList
```

## Наследование

- Родительский класс: ListElement
- Тип элемента: ul (ненумерованный список)
- Назначение: Создание маркированных списков с маркерами (точки, кружки, квадраты)

## Атрибуты класса

| Атрибут     | Тип  | Описание                                      | Значение по умолчанию  |
| ----------- | ---- | --------------------------------------------- | ---------------------- |
| items       | list | Список элементов (наследуется от ListElement) | []                     |
| object_type | str  | Тип объекта                                   | "UnorderedListElement" |

## Конструктор

### **init**(items=None, object_name=None, style=None, boolean_attributes=[], \*\*kwargs)

Создаёт новый маркированный список с указанными параметрами.

Параметры:

- items (list): Начальные элементы списка. По умолчанию None
- object_name (опционально): Имя/идентификатор элемента
- style (опционально): CSS строка для inline стилей
- boolean_attributes (опционально): Список булевых атрибутов
- \*_kwargs: Дополнительные HTML атрибуты (id, class\_, aria-_ и т.д.)

Автоматически устанавливаемые свойства:

- Тег: ul
- self_closing: False (не самозакрывающийся тег)
- object_type: "UnorderedListElement"
- items: список элементов

Примеры:

```python
# Пустой список
ul = UnorderedList()

# Список с элементами
ul = UnorderedList(items=["Яблоко", "Банан", "Апельсин"])

# Список с атрибутами
ul = UnorderedList(
items=["Главная", "О нас", "Контакты"],
class\_="nav-menu",
id="main-menu",
aria_label="Основное меню"
)
```

## Основные методы

### add_item(item)

Добавляет элемент в список. Наследуется от ListElement.

```python
ul = UnorderedList()
ul.add_item("Первый пункт")
ul.add_item("Второй пункт")
ul.add_item(Anchor(href="/more", text="Подробнее..."))
```

## Примеры использования

### Простой маркированный список

```python
# Базовый список
fruits = UnorderedList(items=["Яблоко", "Банан", "Апельсин", "Груша"])
# Список с классом
features = UnorderedList(
    items=[
        "Бесплатная доставка",
        "Гарантия качества",
        "Поддержка 24/7"
    ],
    class_="features-list"
)
```

### Навигационное меню

```python
from layoutml.elements import Anchor
nav_menu = UnorderedList(class_="main-nav")

# Добавление пунктов меню
menu_items = [
    ("Главная", "/"),
    ("О компании", "/about"),
    ("Услуги", "/services"),
    ("Блог", "/blog"),
    ("Контакты", "/contact")
]

for text, url in menu_items:
    link = Anchor(href=url, text=text, class_="nav-link")
    nav_menu.add_item(link)

# Стилизация меню
nav_menu.object_styles.set_display("flex")\
                      .set_list_style_type("none")\
                      .set_padding("0")\
                      .set_margin("0")\
                      .set_gap("20px")
```

### Список с иконками

```python
icon_list = UnorderedList(class_="icon-list")
items_with_icons = [
    ("✓", "Высокое качество"),
    ("🚀", "Быстрая доставка"),
    ("💎", "Лучшая цена"),
    ("🛡️", "Гарантия возврата")
]

for icon, text in items_with_icons:
    item_content = BaseElement(tag="span")
    item_content.get_html(content=f"{icon} {text}")
    icon_list.add_item(item_content)
# Стилизация
icon_list.selectors_styles.add_selector(".icon-list")\
    .set_list_style_type("none")\
    .set_padding_left("0")

icon_list.selectors_styles.add_selector(".icon-list li")\
    .set_padding("8px 0")\
    .set_font_size("16px")
```

### Стилизованный список с кастомными маркерами

```python
styled_ul = UnorderedList(
    items=[
        "Изучить основы Python",
        "Практиковаться ежедневно",
        "Создать портфолио",
        "Найти первую работу"
    ],
    class_="todo-list"
)
# Кастомные маркеры через CSS
styled_ul.selectors_styles.add_selector(".todo-list")\
    .set_list_style_type("none")\
    .set_padding_left("0")

styled_ul.selectors_styles.add_selector(".todo-list li")\
    .set_padding("8px 0 8px 30px")\
    .set_position("relative")

styled_ul.selectors_styles.add_selector(".todo-list li::before")\
    .set_content("'✓ '")\
    .set_position("absolute")\
    .set_left("0")\
    .set_color("#28a745")\
    .set_font_weight("bold")
```

### Вложенные списки

```python
# Главный список
main_list = UnorderedList(class_="categories")
# Категория "Фрукты" с подкатегориями
main_list.add_item("Фрукты")
fruits_sublist = UnorderedList(
    items=["Яблоки", "Бананы", "Апельсины", "Груши"],
    class_="sub-list"
)
main_list.add_item(fruits_sublist)
# Категория "Овощи" с подкатегориями
main_list.add_item("Овощи")
vegetables_sublist = UnorderedList(
    items=["Помидоры", "Огурцы", "Морковь", "Лук"],
    class_="sub-list"
)
main_list.add_item(vegetables_sublist)
# Стилизация вложенных списков
main_list.selectors_styles.add_selector(".sub-list")\
    .set_margin_top("5px")\
    .set_margin_left("20px")\
    .set_list_style_type("circle")
```

### Список характеристик товара

```python
product_features = UnorderedList(class_="product-specs")
specs = [
    ("Процессор", "Intel Core i7-12700K"),
    ("Оперативная память", "32 GB DDR5"),
    ("Видеокарта", "NVIDIA RTX 4080"),
    ("Накопитель", "1 TB NVMe SSD"),
    ("Операционная система", "Windows 11 Pro")
]
for spec_name, spec_value in specs:
    spec_item = BaseElement(tag="span")
    spec_item.get_html(content=f"<strong>{spec_name}:</strong> {spec_value}")
    product_features.add_item(spec_item)
# Стилизация
product_features.selectors_styles.add_selector(".product-specs li")\
    .set_margin_bottom("8px")\
    .set_padding("5px")\
    .set_border_bottom("1px solid #eee")
```

### Список с ссылками и описаниями

```python
from layoutml import Anchor, Span
resource_list = UnorderedList(class_="resources")
resources = [
    {"title": "Документация Python", "url": "https://docs.python.org", "desc": "Официальная документация"},
    {"title": "Stack Overflow", "url": "https://stackoverflow.com", "desc": "Q&A для разработчиков"},
    {"title": "GitHub", "url": "https://github.com", "desc": "Платформа для хостинга кода"},
    {"title": "MDN Web Docs", "url": "https://developer.mozilla.org", "desc": "Документация по веб-технологиям"}
]
for resource in resources:
    # Создаём контейнер для ссылки и описания
    item_container = BaseElement(tag="div")
    # Ссылка
    link = Anchor(href=resource["url"], text=resource["title"], target="_blank")
    # Описание
    desc = Span(text=f" - {resource['desc']}", class_="description")
    item_container.add_element(link)
    item_container.add_element(desc)
    resource_list.add_item(item_container)

# Стилизация
resource_list.selectors_styles.add_selector(".resources li")\
    .set_margin_bottom("12px")

resource_list.selectors_styles.add_selector(".resources .description")\
    .set_color("#666")\
    .set_font_size("0.9em")
```

### Горизонтальное меню

```python
horizontal_menu = UnorderedList(
    items=[
        Anchor(href="/", text="Главная"),
        Anchor(href="/catalog", text="Каталог"),
        Anchor(href="/about", text="О нас"),
        Anchor(href="/contact", text="Контакты")
    ],
    class_="horizontal-nav"
)
# Стилизация горизонтального меню
horizontal_menu.object_styles.set_display("flex")\
                             .set_list_style_type("none")\
                             .set_padding("0")\
                             .set_margin("0")\
                             .set_gap("30px")
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

### Список с бейджами

```python
notification_list = UnorderedList(class_="notifications")
notifications = [
    {"text": "Новое сообщение от Ивана", "badge": "2", "color": "#dc3545"},
    {"text": "Системное обновление готово", "badge": "1", "color": "#28a745"},
    {"text": "Завершено резервное копирование", "badge": "✓", "color": "#17a2b8"}
]
for notif in notifications:
    item_container = BaseElement(tag="div", class_="notification-item")
    # Текст уведомления
    text = Span(text=notif["text"])
    # Бейдж
    badge = Span(
        text=str(notif["badge"]),
        class_="badge",
        style=f"background-color: {notif['color']}; color: white; padding: 2px 8px; border-radius: 12px; margin-left: 10px; font-size: 12px;"
    )
    item_container.add_element(text)
    item_container.add_element(badge)
    notification_list.add_item(item_container)
# Стилизация
notification_list.selectors_styles.add_selector(".notifications li")\
    .set_padding("10px")\
    .set_border_bottom("1px solid #eee")
notification_list.selectors_styles.add_selector(".notifications li:hover")\
    .set_background_color("#f8f9fa")
```

### Список в боковой панели

```python
from layoutml.elements import Aside
sidebar = Aside(class_="sidebar")
# Заголовок
sidebar_title = BaseElement(tag="h3")
sidebar_title.get_html(content="Категории")
# Список категорий
categories = UnorderedList(class_="categories-list")
category_links = [
    ("Электроника", "/category/electronics", 25),
    ("Одежда", "/category/clothing", 18),
    ("Книги", "/category/books", 12),
    ("Спорт", "/category/sports", 8),
    ("Игрушки", "/category/toys", 15)
]
for cat_name, cat_url, count in category_links:
    link_container = BaseElement(tag="span")

    link = Anchor(href=cat_url, text=cat_name)
    count_span = Span(text=f" ({count})", class_="count", style="color: #666; font-size: 0.9em;")

    link_container.add_element(link)
    link_container.add_element(count_span)
    categories.add_item(link_container)

sidebar.add_element(sidebar_title)
sidebar.add_element(categories)
# Стилизация
categories.selectors_styles.add_selector(".categories-list")\
    .set_list_style_type("none")\
    .set_padding_left("0")

categories.selectors_styles.add_selector(".categories-list li")\
    .set_margin_bottom("10px")

categories.selectors_styles.add_selector(".categories-list a")\
    .set_color("#333")\
    .set_text_decoration("none")\
    .set_display("block")\
    .set_padding("5px")\
    .set_border_radius("4px")

categories.selectors_styles.add_selector(".categories-list a:hover")\
    .set_background_color("#007bff")\
    .set_color("white")
```
