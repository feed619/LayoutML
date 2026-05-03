<p align="center">
    <img src="ico/full_logo.png" alt="LayoutML">
</p>
<p align="center">
<a href="https://pypi.org/project/layoutml">
    <img src="https://img.shields.io/badge/pypi-v1.05-blue" alt="Package version">
</a>
</p>
<p align="center">
    <em>LayoutML(layout markup library) — это библиотека которая позволяет описывать структуру веб-страниц напрямую через код, превращая Python в язык разметки для web-интерфейсов.</em>
</p>

[English version](README_EN.md)

## Основные возможности

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

- [CSSBase](docs/ru/base/css/CSSBase.md) - Базовый класс для работы с CSS стилями
- [CSSInline](docs/ru/base/css/CSSInline.md) - Класс для работы с inline стилями
- [CSSSelectors](docs/ru/base/css/CSSSelectors.md) - Класс для управления CSS селекторами

### Базовые элементы

- [BaseElement](docs/ru/base/BaseElement.md) - Базовый класс всех HTML элементов
- [HTMLElement](docs/ru/base/HTMLElement.md) - Класс для работы с HTML атрибутами

### Семантические элементы

- [Header](docs/ru/elements/Header.md) - Семантический элемент шапки `<header>`
- [Main](docs/ru/elements/Main.md) - Семантический элемент основного содержимого `<main>`
- [Footer](docs/ru/elements/Footer.md) - Семантический элемент подвала `<footer>`
- [Nav](docs/ru/elements/Nav.md) - Семантический элемент навигации `<nav>`
- [Section](docs/ru/elements/Section.md) - Семантический элемент секции `<section>`
- [Article](docs/ru/elements/Article.md) - Семантический элемент статьи `<article>`
- [Aside](docs/ru/elements/Aside.md) - Семантический элемент боковой панели `<aside>`

### Текстовые элементы

- [Paragraph](docs/ru/elements/Paragraph.md) - Элемент параграфа `<p>`
- [Span](docs/ru/elements/Span.md) - Строчный контейнер `<span>`
- [Anchor](docs/ru/elements/Anchor.md) - Элемент ссылки `<a>`
- [Heading](docs/ru/elements/Heading.md) - Элементы заголовков `<h1>-<h6>`
- [ListElement](docs/ru/elements/list/ListElement.md) - Базовый класс для списков
- [UnorderedList](docs/ru/elements/list/UnorderedList.md) - Маркированный список `<ul>`
- [OrderedList](docs/ru/elements/list/OrderedList.md) - Нумерованный список `<ol>`

### Медиа элементы

- [Image](docs/ru/elements/Image.md) - Элемент изображения `<img>`

### Элементы форм

- [Form](docs/ru/elements/Form.md) - Базовый класс для элементов форм
- [FormElement](docs/ru/elements/FormElement.md) - Элемент формы `<input>`
- [Input](docs/ru/elements/Input.md) - Специализированный элемент ввода
- [Label](docs/ru/elements/Label.md) - Элемент метки `<label>`
- [Button](docs/ru/elements/Button.md) - Элемент кнопки `<button>`
- [Select](docs/ru/elements/Select.md) - Элемент выпадающего списка `<select>`
- [Textarea](docs/ru/elements/Textarea.md) - Многострочное текстовое поле `<textarea>`

### Компоновка (Layout)

- [Layout](docs/ru/layout/Layout.md) - Базовый класс для layout'ов (Flexbox)
- [HorizontalLayout](docs/ru/layout/HorizontalLayout.md) - Горизонтальный layout
- [VerticalLayout](docs/ru/layout/VerticalLayout.md) - Вертикальный layout

### Структура документа

- [Head](docs/ru/Head.md) - Элемент заголовка страницы `<head>`
- [Body](docs/ru/Body.md) - Элемент тела страницы `<body>`
- [Page](docs/ru/Page.md) - Полный HTML документ

### Маршрутизация

- [Router](docs/ru/router/Router.md) - Класс для маршрутизации URL

### Приложение

- [LayoutML](docs/ru/LayoutML.md) - Главный класс приложения

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
from layoutml.elements import Button, Label
from layoutml.layout import VerticalLayout

class BasePage(Page):
    def __init__(self, object_name=None, doctype="html", title="LayoutML", lang="ru", **kwargs):
        super().__init__(object_name=object_name, doctype=doctype, title=title, lang=lang, **kwargs)
        self.head.set_icon("ico/logo.ico")

# Создание приложения
app = LayoutML()

# Создание страницы
main_page = BasePage(title="Главная")
# Создание элементов
label = Label(text="Hello World!")
button = Button(text="Нажми меня", onclick="alert('Hello!')")
# Создания layout
v_layout = VerticalLayout(object_name="v_layout")
v_layout.add_element(label)
v_layout.add_element(button)
# Добавление элементов на страницу
main_page.body.add_element(v_layout)
# Регистрация страницы
app.include_page(main_page)

# Определение маршрута
@app.route("/")
def home():
    page = main_page.copy()
    return page

# Запуск приложения
if __name__ == "__main__":
    app.start(host="localhost", port=3700)
```

После запуска сервер будет доступен по адресу http://localhost:3700

### Запуск через Uvicorn из командной строки

Вы можете запустить приложение с помощью Uvicorn из терминала:

```bash
pip install uvicorn
uvicorn main:app --host localhost --port 3700 --reload
```

Где `main` - имя вашего Python файла, `app` - имя экземпляра приложения LayoutML.

### Запуск через Uvicorn из Python кода

Вы также можете запустить Uvicorn непосредственно из Python скрипта:

```python
if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=3700)

```

### Создание нескольких маршрутов

Пример приложения с несколькими страницами:

```python
from layoutml import LayoutML, Page
from layoutml.elements import Anchor, Button, Label, Paragraph
from layoutml.layout import VerticalLayout

class BasePage(Page):
    def __init__(self, object_name=None, doctype="html", title="LayoutML", lang="ru", **kwargs):
        super().__init__(object_name=object_name, doctype=doctype, title=title, lang=lang, **kwargs)
        self.head.set_icon("ico/logo.ico")

def get_main_page() -> Page:
    # Создание страницы
    main_page = BasePage(title="Главная")
    # Создание элементов
    label = Label(text="Hello World!")
    button = Button(text="Нажми меня", onclick="alert('Hello!')")
    # Создания layout
    v_layout = VerticalLayout(object_name="v_layout")
    v_layout.add_element(label)
    v_layout.add_element(button)
    # Добавление элементов на страницу
    main_page.add_element(v_layout)

    return main_page

def get_about_page() -> Page:
    # Создание страницы
    page = BasePage(title="О нас")
    # Создание элементов
    paragraph = Paragraph(text="Мы создаём веб-приложения с помощью LayoutML")
    back_link = Anchor(href="/", text="На главную")
    # Добавление элементов на страницу
    page.add_element(paragraph)
    page.add_element(back_link)

    return page

# Создание приложения
app = LayoutML()

# Регистрация страницы
main_page = get_main_page()
about_page = get_about_page()
app.include_page(main_page)
app.include_page(about_page)

# Определение маршрута
@app.route("/")
def home():
    page = main_page.copy()
    return page

@app.route("/about")
def about():
    page = about_page.copy()
    return page

# Запуск приложения
if __name__ == "__main__":
    app.start(host="localhost", port=3700)
```

### Использование параметров маршрута

Вы можете создавать динамические страницы с параметрами в URL:

```python
from layoutml import LayoutML, Page
from layoutml.elements import Button, Label
from layoutml.layout import VerticalLayout

def get_echo_page() -> Page:
    # Создание страницы
    main_page = Page(title="Главная")
    # Создание элементов
    label = Label(text="Hello World!")
    button = Button(object_name="button", text="Нажми меня", onclick="alert('Hello!')")
    # Создания layout
    v_layout = VerticalLayout(object_name="v_layout")
    v_layout.add_element(label)
    v_layout.add_element(button)
    main_page.add_element(v_layout)

    return main_page

# Создание приложения
app = LayoutML()
# Регистрация страницы
username_page = get_echo_page()
app.include_page(username_page)
# Определение маршрута

@app.route("/echo")
def echo(username: str):
    page = username_page.copy()
    button: Button = page.get_element("v_layout").get_element("button")
    button.text += f" {username}"
    return page
# Запуск приложения
if __name__ == "__main__":
    app.start(host="localhost", port=3700)
```

### Добавление CSS стилей

Пример страницы с кастомными стилями:

```python
from layoutml import LayoutML, Page
from layoutml.elements import Paragraph, Button


def get_page() -> Page:
    page = Page(object_name="main_page", title="Стилизованная страница")
    paragraph = Paragraph(text="Этот текст стилизован с помощью CSS", class_="highlight-text")
    button = Button(
        text="Стильная кнопка",
        class_="custom-button",
        style="padding: 10px 20px; background: #007bff; color: white; border: none; border-radius: 5px;",
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

    page.body.add_element(paragraph)
    page.body.add_element(button)

    return page

app = LayoutML()
main_page = get_page()
app.include_page(main_page)

@app.route("/")
def styled_page():
    page = main_page.copy()
    return page

if __name__ == "__main__":
    app.start()
```

### Использование макетов (Layouts)

Создание страницы с помощью горизонтальных и вертикальных макетов:

```python
from layoutml import LayoutML, Page
from layoutml.elements import  Paragraph, Button
from layoutml.layout import HorizontalLayout, VerticalLayout

def get_page() -> Page:
    page = Page(object_name="main_page", title="Пример макетов")
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
        card.object_styles.set_border("1px solid #ddd").set_padding("15px").set_border_radius("8px").set_width("200px")
        card.add_element(Paragraph(text=f"Карточка {i+1}"))
        card.add_element(Button(text="Подробнее"))
        cards_layout.add_element(card)
    main_layout.add_elements(nav_layout, cards_layout)
    page.body.add_element(main_layout)

    return page

app = LayoutML()
main_page = get_page()
app.include_page(main_page)

@app.route("/")
def layout_example():
    page = main_page.copy()
    return page

if __name__ == "__main__":
    app.start()
```

### Обработка форм

Пример создания страницы с формой и обработкой данных:

```python
from layoutml import LayoutML, Page
from layoutml.elements import Input, Button, Label, Paragraph
from layoutml.layout import VerticalLayout, HorizontalLayout


def get_form_page():
    page = Page(object_name="form_page", title="Контакты")
    page.body.add_element(Paragraph(text="Свяжитесь с нами"))
    # Создание формы
    h_layout_name = HorizontalLayout(object_name="h_layout_name")
    h_layout_email = HorizontalLayout(object_name="h_layout_email")
    # Поле имени
    h_layout_name.add_element(Label(for_id="name", text="Имя:"))
    h_layout_name.add_element(Input(id="name", name="name", required=True))
    # Поле email
    h_layout_email.add_element(Label(for_id="email_label", text="Email:"))
    h_layout_email.add_element(Input(type="email", id="email", name="email", required=True))
    # Кнопка отправки
    button = Button(text="Отправить", type="submit")
    v_layout = VerticalLayout(object_name="v_layout")
    v_layout.add_elements(h_layout_name, h_layout_email, button)
    page.body.add_element(v_layout)
    # Отключении автоматического рендеринга файла страница
    page.render_css_file = False
    page.add_stylesheet(href="styles/form_page_styles.css")
    return page


app = LayoutML()
form_page = get_form_page()
app.include_page(form_page)


@app.route("/")
def contact_page():
    page = form_page.copy()
    return page


if __name__ == "__main__":
    app.start()
```

```css
/* form_page_styles.css */

@import url("https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap");

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body.Body {
  font-family: "Inter", sans-serif;
  background: #f8fafc;
  color: #1e293b;
  min-height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 20px;
}

.v_layout {
  background: #ffffff;
  width: 100%;
  max-width: 480px;
  padding: 40px;
  border-radius: 20px;
  box-shadow: 0 10px 40px rgba(15, 23, 42, 0.08);
  display: flex;
  flex-direction: column;
  gap: 24px;
  border: 1px solid rgba(226, 232, 240, 0.8);
}

.ParagraphElement {
  position: absolute;
  top: 80px;
  font-size: 2rem;
  font-weight: 600;
  color: #0f172a;
  letter-spacing: -0.5px;
}

.h_layout_name,
.h_layout_email {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.LabelElement {
  font-size: 0.95rem;
  font-weight: 500;
  color: #475569;
}

.InputElement {
  width: 100%;
  padding: 14px 16px;
  border: 1.5px solid #e2e8f0;
  border-radius: 14px;
  font-size: 1rem;
  background: #f8fafc;
  transition: all 0.25s ease;
  outline: none;
}

.InputElement:focus {
  border-color: #6366f1;
  background: #ffffff;
  box-shadow: 0 0 0 4px rgba(99, 102, 241, 0.12);
}

.ButtonElement {
  margin-top: 10px;
  padding: 15px;
  border: none;
  border-radius: 14px;
  background: #6366f1;
  color: white;
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.25s ease;
}

.ButtonElement:hover {
  background: #4f46e5;
  transform: translateY(-2px);
  box-shadow: 0 8px 20px rgba(99, 102, 241, 0.25);
}

.ButtonElement:active {
  transform: translateY(0);
}

@media (max-width: 600px) {
  .v_layout {
    padding: 28px;
  }

  .ParagraphElement {
    font-size: 1.6rem;
    top: 40px;
  }
}
```

### Полный пример использования

```python
from layoutml import LayoutML, Page, Request, Response, JSONResponse

# Создание приложения
app = LayoutML(styles_dirname="assets/css")

# Создание базовой страницы
class BasePage(Page):
    def __init__(self, object_name: str, title="LayoutML", **kwargs):
        super().__init__(object_name=object_name, title=title, **kwargs)
        self.head.set_icon("static/logo.ico")  # Установка иконки

# Создание и регистрация страницы
main_page = BasePage(object_name="main_page", title="Главная")
main_page.body.add_content("<h1>Добро пожаловать!</h1>")
app.include_page(main_page)

# HTML маршрут
@app.route("/")
async def home(request: Request, response: Response):
    page = main_page.copy()
    page.body.add_content("<p>Это главная страница</p>")
    return page

# API маршрут с JSON ответом
@app.route("/api/data")
async def get_data(request: Request, response: Response):
    return JSONResponse(content={"status": "ok", "data": [1, 2, 3]})

# Маршрут с параметрами
@app.route("/user")
async def user_profile(
    request: Request,
    response: Response,
    user_id: int,
    name: str = "Guest",
):
    page = main_page.copy()
    page.title = f"Профиль {name}"
    page.body.add_content(f"<h1>Пользователь: {name} (ID: {user_id})</h1>")
    return page

# Кастомная страница 404
custom_404 = BasePage(object_name="error_page", title="Страница не найдена")
custom_404.body.add_content("""
    <div style="text-align: center; padding: 50px;">
        <h1>404</h1>
        <p>Страница не найдена</p>
        <a href="/">Вернуться на главную</a>
    </div>
""")
app.set_error_page(custom_404)

if __name__ == "__main__":
    app.print_routes()  # Просмотр маршрутов
    app.start(host="localhost", port=3700)
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

## Лучшие практики

### 1. Используйте копирование страниц

```python
# Всегда копируйте страницу в обработчике
@app.route("/profile")
def profile_handler(request: Request, response: Response):
    page = base_page.copy()  # ✅
    return page
```

### 2. Регистрируйте все страницы

```python
# Регистрация всех используемых страниц
app.include_page(home_page)
app.include_page(about_page)
app.include_page(contact_page)
```

### 3. Используйте базовый класс для страниц установления иконки для всех страниц

```python
class AppPage(Page):
    def __init__(self, title="App", **kwargs):
        super().__init__(title=title, **kwargs)
        self.head.set_icon("/static/favicon.ico")
        self.head.add_stylesheet("/static/app.css")
```

### 4. Обрабатывайте ошибки

```python
@app.route("/protected")
async def protected(request: Request, response: Response):
    if not request.headers.get("Authorization"):
        raise HTTPException(status_code=401, detail="Unauthorized")
    return page.copy()
```

## Статус проекта

LayoutML находится в активной разработке.

## 📄 Лицензия

[MIT License](LICENSE)

## Обратная связь:

Я всегда рад вашим отзывам и предложениям по улучшению LayoutML. Пожалуйста, оставляйте свои комментарии.
Электронная почта

- [Email](mailto:feed619pro@gmail.com)
