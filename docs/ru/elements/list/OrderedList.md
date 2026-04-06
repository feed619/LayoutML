# OrderedList

`OrderedList` - это специализированный класс для создания HTML нумерованных списков <ol>. Класс наследуется от [ListElement](ListElement.md) и предназначен для создания упорядоченных списков, где порядок элементов имеет значение (например, пошаговые инструкции, рейтинги, топ-списки).

---

## Импорт

```python
from layoutML.elements.list import OrderedList
```

## Наследование

- Родительский класс: ListElement
- Тип элемента: ol (упорядоченный список)
- Назначение: Создание нумерованных списков с автоматической нумерацией элементов

## Атрибуты класса

| Атрибут     | Тип  | Описание                                      | Значение по умолчанию |
| ----------- | ---- | --------------------------------------------- | --------------------- |
| items       | list | Список элементов (наследуется от ListElement) | []                    |
| object_type | str  | Тип объекта                                   | "OrderedListElement"  |

## Конструктор

### **init**(items=None, object_name=None, style=None, boolean_attributes=[], \*\*kwargs)

Создаёт новый нумерованный список с указанными параметрами.

Параметры:

- items (list): Начальные элементы списка. По умолчанию None
- object_name (опционально): Имя/идентификатор элемента
- style (опционально): CSS строка для inline стилей
- boolean_attributes (опционально): Список булевых атрибутов
- \*\*kwargs: Дополнительные HTML атрибуты (id, class\_, start, reversed, type и т.д.)

Автоматически устанавливаемые свойства:

- Тег: ol
- self_closing: False (не самозакрывающийся тег)
- object_type: "OrderedListElement"
- items: список элементов

Примеры:

```python
# Пустой список
ol = OrderedList()
# Список с элементами
ol = OrderedList(items=["Первый", "Второй", "Третий"])
# Список с атрибутами
ol = OrderedList(
    items=["Шаг 1", "Шаг 2", "Шаг 3"],
    class_="steps",
    start="1",
    type="A",
    id="instruction-list"
)
```

## Основные методы

### add_item(item)

Добавляет элемент в список. Наследуется от ListElement.

```python
ol = OrderedList()
ol.add_item("Первый пункт")
ol.add_item("Второй пункт")
ol.add_item(Anchor(href="/more", text="Подробнее..."))
```

## Специальные атрибуты HTML для OrderedList

| Атрибут  | Описание                   | Пример                                     |
| -------- | -------------------------- | ------------------------------------------ |
| start    | Номер первого элемента     | start="5" (начинает с 5)                   |
| reversed | Обратный порядок нумерации | reversed                                   |
| type     | Тип нумерации              | type="A" (буквы), type="I" (римские цифры) |

## Примеры использования

### Простой нумерованный список

```python
# Базовый список
steps = OrderedList(items=[
    "Подготовить ингредиенты",
    "Смешать компоненты",
    "Выпекать 30 минут",
    "Остудить и подать"
])
```

### Список с указанием стартового номера

```python
# Список, начинающийся с 5
top_five = OrderedList(
    items=[
        "Пятое место",
        "Четвёртое место",
        "Третье место",
        "Второе место",
        "Первое место"
    ],
    start="5",
    reversed=True  # Обратный порядок
)
```

### Различные типы нумерации

```python
# Буквенная нумерация (A, B, C...)
letter_list = OrderedList(
    items=["Пункт A", "Пункт B", "Пункт C"],
    type="A"
)
# Строчная буквенная нумерация (a, b, c...)
lower_letter_list = OrderedList(
    items=["Пункт a", "Пункт b", "Пункт c"],
    type="a"
)
# Римские цифры (I, II, III...)
roman_list = OrderedList(
    items=["Раздел I", "Раздел II", "Раздел III"],
    type="I"
)
# Строчные римские цифры (i, ii, iii...)
lower_roman_list = OrderedList(
    items=["Часть i", "Часть ii", "Часть iii"],
    type="i"
)
```

### Список со сложным содержимым

```python
from layoutml.elements import Anchor, Span, Image

recipe = OrderedList(class_="recipe-steps")

# Шаг 1: текст
recipe.add_item("Разогреть духовку до 180°C")

# Шаг 2: текст со ссылкой
step2 = Span()
step2.get_html(content="Добавить <a href='/ingredients/flour'>муку</a> и перемешать")
recipe.add_item(step2)

# Шаг 3: с изображением
step3_container = Span()
step3_container.get_html(content="Выложить тесто в форму: ")
step3_img = Image(src="pan.jpg", alt="Форма для выпечки", style="width: 50px; vertical-align: middle;")
step3_container.add_element(step3_img)
recipe.add_item(step3_container)

# Шаг 4: с подсказкой
step4 = Span()
step4.get_html(content="Выпекать 30 минут ")
tip = Span(text="(не открывайте духовку!)", class_="tip", style="color: #666; font-style: italic;")
step4.add_element(tip)
recipe.add_item(step4)
```

### Стилизованный нумерованный список

```python

ol = OrderedList(
    items=["Пункт 1", "Пункт 2", "Пункт 3"],
    object_name="styledOrderedList",
    class_="custom-list"
)

# Inline стили
ol.inline_styles.set_padding_left("30px")\
                .set_margin_bottom("20px")

# Стили для элементов списка
ol.selectors_styles.add_selector(".custom-list li")\
    .set_margin_bottom("10px")\
    .set_padding("8px 12px")\
    .set_background_color("#f8f9fa")\
    .set_border_radius("4px")

# Стили для номеров
ol.selectors_styles.add_selector(".custom-list li::marker")\
    .set_color("#007bff")\
    .set_font_weight("bold")\
    .set_font_size("1.2em")
```

### Пошаговая инструкция

```python
tutorial = OrderedList(
    class_="tutorial",
    type="1",
    start="1"
)

# Добавление шагов
steps = [
    "Установите Python с официального сайта",
    "Создайте виртуальное окружение: `python -m venv venv`",
    "Активируйте окружение",
    "Установите зависимости: `pip install -r requirements.txt`",
    "Запустите приложение: `python app.py`"
]

for step in steps:
    tutorial.add_item(step)

# Стилизация туториала
tutorial.object_styles.set_font_family("monospace")\
                      .set_background_color("#f4f4f4")\
                      .set_padding("20px")\
                      .set_border_radius("8px")

tutorial.selectors_styles.add_selector(".tutorial li")\
    .set_margin_bottom("15px")\
    .set_line_height("1.6")
```

### Вложенные нумерованные списки

```python
from layoutml.elements.list import OrderedList
# Основной список
main_list = OrderedList(class_="outline")

# Глава 1
chapter1 = "Глава 1: Введение"
subpoints1 = OrderedList(
    items=[
        "Что такое веб-разработка",
        "Основные технологии",
        "Инструменты разработчика"
    ],
    type="a"  # Строчные буквы для подпунктов
)
main_list.add_item(chapter1)
main_list.add_item(subpoints1)

# Глава 2
chapter2 = "Глава 2: HTML основы"
subpoints2 = OrderedList(
    items=[
        "Структура HTML документа",
        "Основные теги",
        "Атрибуты элементов"
    ],
    type="a"
)
main_list.add_item(chapter2)
main_list.add_item(subpoints2)

# Глава 3
chapter3 = "Глава 3: CSS стилизация"
subpoints3 = OrderedList(
    items=[
        "Селекторы",
        "Свойства",
        "Адаптивный дизайн"
    ],
    type="a"
)
main_list.add_item(chapter3)
main_list.add_item(subpoints3)
```

### Топ-список с описаниями

```python
top_list = OrderedList(
    class_="top-list",
    start="1",
    reversed=False
)

# Данные для топа
top_items = [
    {"title": "Python", "description": "Универсальный язык для начинающих"},
    {"title": "JavaScript", "description": "Язык для веб-разработки"},
    {"title": "Java", "description": "Популярный язык для корпоративных приложений"},
    {"title": "C++", "description": "Высокопроизводительный язык"},
    {"title": "Go", "description": "Современный язык от Google"}
]

for item in top_items:
    # Создаём элемент с заголовком и описанием
    item_container = BaseElement(tag="div")
    title = BaseElement(tag="strong")
    title.get_html(content=item["title"])
    description = BaseElement(tag="span")
    description.get_html(content=f" - {item['description']}")

    item_container.add_element(title)
    item_container.add_element(description)
    top_list.add_item(item_container)

# Стилизация
top_list.selectors_styles.add_selector(".top-list li")\
    .set_margin_bottom("15px")\
    .set_padding("10px")\
    .set_background_color("#f8f9fa")\
    .set_border_radius("5px")

top_list.selectors_styles.add_selector(".top-list li::marker")\
    .set_color("#dc3545")\
    .set_font_size("1.3em")\
    .set_font_weight("bold")
```

### Список с кастомной нумерацией (через CSS)

```python
custom_ol = OrderedList(
    items=[
        "Важное достижение",
        "Очень важное достижение",
        "Критически важное достижение"
    ],
    class_="achievements"
)

# CSS кастомная нумерация
custom_ol.selectors_styles.add_selector(".achievements")\
    .set_counter_reset("achievement-counter")

custom_ol.selectors_styles.add_selector(".achievements li")\
    .set_counter_increment("achievement-counter")\
    .set_list_style_type("none")\
    .set_position("relative")\
    .set_padding_left("30px")

custom_ol.selectors_styles.add_selector(".achievements li::before")\
    .set_content("'🏆 ' counter(achievement-counter) '. '")\
    .set_position("absolute")\
    .set_left("0")\
    .set_color("#ffc107")\
    .set_font_weight("bold")
```

### Список в боковой панели

```python
from layoutml.elements import Aside
sidebar = Aside(class_="sidebar")

# Заголовок
sidebar_title = BaseElement(tag="h3")
sidebar_title.get_html(content="Популярные статьи")

# Список
popular_articles = OrderedList(
    class_="popular-list",
    type="1"
)

articles = [
    ("10 лучших практик веб-разработки", "/articles/best-practices"),
    ("Как выучить Python за месяц", "/articles/learn-python"),
    ("Основы React для начинающих", "/articles/react-basics"),
    ("Современный CSS: Grid и Flexbox", "/articles/css-grid-flex")
]

for title, url in articles:
    link = Anchor(href=url, text=title, class_="article-link")
    popular_articles.add_item(link)

sidebar.add_element(sidebar_title)
sidebar.add_element(popular_articles)

# Стилизация
popular_articles.selectors_styles.add_selector(".popular-list li")\
    .set_margin_bottom("10px")

popular_articles.selectors_styles.add_selector(".popular-list a")\
    .set_color("#333")\
    .set_text_decoration("none")\
    .set_transition("color 0.3s")

popular_articles.selectors_styles.add_selector(".popular-list a:hover")\
    .set_color("#007bff")
```
