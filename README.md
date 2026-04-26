<p align="center">
  <img src="ico\full_logo.png" alt="LayoutML"></a>
</p>
<p align="center">
    <em>LayoutML(layout markup library) — это библиотека которая позволяет описывать структуру веб-страниц напрямую через код, превращая Python в язык разметки для web-интерфейсов.</em>
</p>
<p align="center">
<a href="https://pypi.org/project/layoutml">
    <img src="https://img.shields.io/pypi/v/fastapi?color=%2334D058&label=pypi%20package" alt="Package version">
</a>
<a href="https://pypi.org/project/fastapi">
    <img src="https://img.shields.io/pypi/pyversions/fastapi.svg?color=%2334D058" alt="Supported Python versions">
</a>
</p>

## ✨ Основные возможности

- Создание HTML-элементов через Python-классы
- Описание CSS-стилей программным способом
- Компонентный подход (переиспользуемые layout-блоки)
- Читаемый и декларативный синтаксис
- Генерация чистого HTML/CSS без лишнего кода
- Лёгкая интеграция с FastAPI, Flask, Django
- Минимальный вес и отсутствие внешних зависимостей

## Для кого

- Python-разработчиков, которые не хотят писать HTML вручную
- Backend-разработчиков (FastAPI / Django / Flask)
- Учебных проектов
- Генерации HTML-отчётов и интерфейсов
- Создания собственных web-фреймворков поверх LayoutML

## Содержание

### Основные классы

- [CSSBase](docs\ru\base\css\CSSBase.md) - Базовый класс для работы с CSS стилями
- [CSSInline](docs\ru\base\css\CSSInline.md) - Класс для работы с inline стилями
- [CSSSelectors](docs\ru\base\css\CSSSelectors.md) - Класс для управления CSS селекторами

### Базовые элементы

- [BaseElement](docs\ru\base\BaseElement.md) - Базовый класс всех HTML элементов
- [HTMLElement](docs\ru\base\HTMLElement.md) - Класс для работы с HTML атрибутами

### Семантические элементы

- [Header](docs\ru\elements\Header.md) - Семантический элемент шапки `<header>`
- [Main](docs\ru\elements\Main.md) - Семантический элемент основного содержимого `<main>`
- [Footer](docs\ru\elements\Footer.md) - Семантический элемент подвала `<footer>`
- [Nav](docs\ru\elements\Nav.md) - Семантический элемент навигации `<nav>`
- [Section](docs\ru\elements\Section.md) - Семантический элемент секции `<section>`
- [Article](docs\ru\elements\Article.md) - Семантический элемент статьи `<article>`
- [Aside](docs\ru\elements\Aside.md) - Семантический элемент боковой панели `<aside>`

### Текстовые элементы

- [Paragraph](docs\ru\elements\Paragraph.md) - Элемент параграфа `<p>`
- [Span](docs\ru\elements\Span.md) - Строчный контейнер `<span>`
- [Anchor](docs\ru\elements\Anchor.md) - Элемент ссылки `<a>`
- [Heading](docs\ru\elements\Heading.md) - Элементы заголовков `<h1>-<h6>`
- [ListElement](docs\ru\elements\list\ListElement.md) - Базовый класс для списков
- [UnorderedList](docs\ru\elements\list\UnorderedList.md) - Маркированный список `<ul>`
- [OrderedList](docs\ru\elements\list\OrderedList.md) - Нумерованный список `<ol>`

### Медиа элементы

- [Image](docs\ru\elements\Image.md) - Элемент изображения `<img>`

### Элементы форм

- [Form](docs\ru\elements\Form.md) - Базовый класс для элементов форм
- [FormElement](docs\ru\elements\FormElement.md) - Элемент формы `<input>`
- [Input](docs\ru\elements\Input.md) - Специализированный элемент ввода
- [Label](docs\ru\elements\Label.md) - Элемент метки `<label>`
- [Button](docs\ru\elements\Button.md) - Элемент кнопки `<button>`
- [Select](docs\ru\elements\Select.md) - Элемент выпадающего списка `<select>`
- [Textarea](docs\ru\elements\Textarea.md) - Многострочное текстовое поле `<textarea>`

### Компоновка (Layout)

- [Layout](docs\ru\layout\Layout.md) - Базовый класс для layout'ов (Flexbox)
- [HorizontalLayout](docs\ru\layout\HorizontalLayout.md) - Горизонтальный layout
- [VerticalLayout](docs\ru\layout\VerticalLayout.md) - Вертикальный layout

### Структура документа

- [Head](docs\ru\Head.md) - Элемент заголовка страницы `<head>`
- [Body](docs\ru\Body.md) - Элемент тела страницы `<body>`
- [Page](docs\ru\Page.md) - Полный HTML документ

### Маршрутизация

- [Router](docs\ru\base\router\Router.md) - Класс для маршрутизации URL

### Приложение

- [LayoutML](docs\ru\LayoutML.md) - Главный класс приложения

## Быстрый старт

### Установка

```bash
pip install layoutml
```

## Пример использования

В этом разделе представлены примеры создания веб-приложений с использованием библиотеки LayoutML. Вы узнаете, как создавать страницы, добавлять элементы и запускать сервер.

### Обычный запуск

Самый простой способ запустить приложение LayoutML:

```python
from layoutml import LayoutML, Page
from layoutml.elements import Header, Paragraph, Button

class BasePage(Page):
    def __init__(self, doctype="html", title="LayoutML", lang="ru", object_name=None, **kwargs):
        super().__init__(doctype, title, lang, object_name, **kwargs)
        self.head.set_icon("ico/logo.ico")


# Создание приложения
app = LayoutML()

# Определение маршрута
@app._router.route("/")
def home():
    page = BasePage(title="Главная")

    # Создание элементов
    header = Header()
    header.get_html(content="<h1>Добро пожаловать!</h1>")

    paragraph = Paragraph(text="Это пример использования LayoutML")

    button = Button(text="Нажми меня", onclick="alert('Hello!')")

    # Добавление элементов на страницу
    page.body.add_element(header)
    page.body.add_element(paragraph)
    page.body.add_element(button)

    return page

# Запуск приложения
if __name__ == "main":
    app.start(host="localhost", port=3700)
```

После запуска сервер будет доступен по адресу http://localhost:3700

### Запуск через Uvicorn из командной строки

Вы можете запустить приложение с помощью Uvicorn из терминала:

```bash
uvicorn test:app --host localhost --port 3700 --reload
```

Где `test` - имя вашего Python файла, `app` - имя экземпляра приложения LayoutML.

### Запуск через Uvicorn из Python кода

Вы также можете запустить Uvicorn непосредственно из Python скрипта:

```python
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

### Создание нескольких маршрутов

Пример приложения с несколькими страницами:

```python
from layoutml import LayoutML, Page
from layoutml.elements import Header, Paragraph, Button, Anchor

app = LayoutML()

@app.route("/")
def home():
    page = Page(title="Главная")

    header = Header()
    header.get_html(content="<h1>Главная страница</h1>")

    paragraph = Paragraph(text="Добро пожаловать на наш сайт!")

    link = Anchor(href="/about", text="О нас")

    page.body.add_element(header)
    page.body.add_element(paragraph)
    page.body.add_element(link)

    return page

@app.route("/about")
def about():
    page = Page(title="О нас")

    header = Header()
    header.get_html(content="<h1>О нашей компании</h1>")

    paragraph = Paragraph(text="Мы создаём веб-приложения с помощью LayoutML")

    back_link = Anchor(href="/", text="На главную")

    page.body.add_element(header)
    page.body.add_element(paragraph)
    page.body.add_element(back_link)

    return page

if __name__ == "__main__":
    app.start()
```

### Использование параметров маршрута

Вы можете создавать динамические страницы с параметрами в URL:

```python
from layoutml import LayoutML, Page
from layoutml.elements import Header, Paragraph

app = LayoutML()

@app._router.route("/user/<username>")
def user_profile(username: str):
    page = Page(title=f"Профиль {username}")

    header = Header()
    header.get_html(content=f"<h1>Профиль пользователя: {username}</h1>")

    paragraph = Paragraph(text=f"Добро пожаловать, {username}!")

    page.body.add_element(header)
    page.body.add_element(paragraph)

    return page

if __name__ == "__main__":
    app.start()
```

### Добавление CSS стилей

Пример страницы с кастомными стилями:

```python
from layoutml import LayoutML, Page
from layoutml.elements import Header, Paragraph, Button

app = LayoutML()

@app.route("/")
def styled_page():
    page = Page(title="Стилизованная страница")

    # Создание элемента с CSS классами
    header = Header(class_="main-header")
    header.get_html(content="<h1>Стилизованная страница</h1>")

    paragraph = Paragraph(
        text="Этот текст стилизован с помощью CSS",
        class_="highlight-text"
    )

    button = Button(
        text="Стильная кнопка",
        class_="custom-button",
        style="padding: 10px 20px; background: #007bff; color: white; border: none; border-radius: 5px;"
    )

    # Добавление CSS стилей через объект head
    page.head.selectors_styles.add_selector(".main-header")\
        .set_background_color("#f8f9fa")\
        .set_padding("20px")\
        .set_text_align("center")

    page.head.selectors_styles.add_selector(".highlight-text")\
        .set_color("#007bff")\
        .set_font_size("18px")\
        .set_font_weight("bold")

    page.head.selectors_styles.add_selector(".custom-button:hover")\
        .set_background_color("#0056b3")\
        .set_transform("scale(1.05)")

    page.body.add_element(header)
    page.body.add_element(paragraph)
    page.body.add_element(button)

    return page

if __name__ == "__main__":
    app.start()
```

### Использование макетов (Layouts)

Создание страницы с помощью горизонтальных и вертикальных макетов:

```python
from layoutml import LayoutML, Page
from layoutml.elements import Header, Paragraph, Button
from layoutml.layout import HorizontalLayout, VerticalLayout

app = LayoutML()

@app.route("/")
def layout_example():
    page = Page(title="Пример макетов")

    # Вертикальный макет для всей страницы
    main_layout = VerticalLayout(object_name="mainLayout")
    main_layout.object_styles.set_gap("20px").set_padding("20px")

    # Горизонтальный макет для навигации
    nav_layout = HorizontalLayout(object_name="navLayout")
    nav_layout.object_styles.set_justify_content("space-between")

    nav_layout.add_element(Button(text="Главная"))
    nav_layout.add_element(Button(text="О нас"))
    nav_layout.add_element(Button(text="Контакты"))

    # Горизонтальный макет для карточек
    cards_layout = HorizontalLayout(object_name="cardsLayout")
    cards_layout.object_styles.set_gap("20px").set_justify_content("center")

    for i in range(3):
        card = VerticalLayout(object_name=f"card{i}")
        card.object_styles.set_border("1px solid #ddd")\
                          .set_padding("15px")\
                          .set_border_radius("8px")\
                          .set_width("200px")

        card.add_element(Paragraph(text=f"Карточка {i+1}"))
        card.add_element(Button(text="Подробнее"))
        cards_layout.add_element(card)

    main_layout.add_elements(nav_layout, cards_layout)
    page.body.add_element(main_layout)

    return page

if __name__ == "__main__":
    app.start()
```

### Обработка форм

Пример создания страницы с формой и обработкой данных:

```python
from layoutml import LayoutML, Page
from layoutml.elements import Input, Button, Label, Paragraph

app = LayoutML()

@app.route("/contact", methods=["GET", "POST"])
def contact_page():
    page = Page(title="Контакты")

    page.body.add_element(Paragraph(text="Свяжитесь с нами"))

    # Создание формы
    form = BaseElement(tag="form", method="post", action="/submit")

    # Поле имени
    form.add_element(Label(for_id="name", text="Имя:"))
    form.add_element(Input(id="name", name="name", required=True))

    # Поле email
    form.add_element(Label(for_id="email", text="Email:"))
    form.add_element(Input(type="email", id="email", name="email", required=True))

    # Кнопка отправки
    form.add_element(Button(text="Отправить", type="submit"))

    page.body.add_element(form)

    return page

if __name__ == "__main__":
    app.start()
```

## Советы по разработке

1. Режим разработки: Используйте флаг --reload при запуске через Uvicorn для автоматической перезагрузки при изменениях кода.
2. Отладка: Вы можете выводить информацию о маршрутах с помощью метода print_routes():

```python
app.print_routes()
```

3. Структурирование кода: Для больших приложений рекомендуется разделять маршруты по модулям:

```python
# routes.py
from layoutml import LayoutML
app = LayoutML()
# Импорт маршрутов из других модулей

from .home_routes import home_router
from .api_routes import api_router

app.include_router(home_router)
app.include_router(api_router, prefix="/api")
```

4. Асинхронные обработчики: LayoutML поддерживает асинхронные функции для обработки маршрутов:

```python
@app.route("/async-data")
async def async_data():
  data = await fetch_data_from_db()
  page = Page(title="Данные")
  page.body.add_element(Paragraph(text=str(data)))
  return page
```

## Статус проекта

LayoutML находится в активной разработке.

## 📄 Лицензия

[MIT License](LICENSE)

## Обратная связь:

Я всегда рад вашим отзывам и предложениям по улучшению LayoutML. Пожалуйста, оставляйте свои комментарии.
Электронная почта

- [Email](mailto:feed619pro@gmail.com)
