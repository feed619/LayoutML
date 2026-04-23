<p align="center">
  <img src="ico\logo.png" style="width: 50%; max-width: 300px;" />
</p>
<h2><p align="center">LayoutML — Layout Markup Library</p></h2>

---

## LayoutML — это простой и расширяемый Python-фреймворк для декларативного создания HTML и CSS с использованием классов и объектов Python.

Библиотека позволяет описывать структуру веб-страниц, стили и компоненты без шаблонизаторов, напрямую через код, превращая Python в язык разметки для web-интерфейсов.

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

- [Image](docs\ru\elements\Image.md) - Элемент изображения <img>

### Элементы форм

- [Form](docs\ru\elements\Form.md) - Базовый класс для элементов форм
- [FormElement](docs\ru\elements\FormElement.md) - Элемент формы <input>
- [Input](docs\ru\elements\Input.md) - Специализированный элемент ввода
- [Label](docs\ru\elements\Label.md) - Элемент метки <label>
- [Button](docs\ru\elements\Button.md) - Элемент кнопки <button>
- [Select](docs\ru\elements\Select.md) - Элемент выпадающего списка <select>
- [Textarea](docs\ru\elements\Textarea.md) - Многострочное текстовое поле <textarea>

### Компоновка (Layout)

- [Layout](docs\ru\layout\Layout.md) - Базовый класс для layout'ов (Flexbox)
- [HorizontalLayout](docs\ru\layout\HorizontalLayout.md) - Горизонтальный layout
- [VerticalLayout](docs\ru\layout\VerticalLayout.md) - Вертикальный layout

### Структура документа

- [Head](docs\ru\Head.md) - Элемент заголовка страницы <head>
- [Body](docs\ru\Body.md) - Элемент тела страницы <body>
- [Page](docs\ru\Page.md) - Полный HTML документ

### Маршрутизация

- [Router](docs\ru\base\router\Router.md) - Класс для маршрутизации URL

### Приложение

[- LayoutML](docs\ru\LayoutML.md) - Главный класс приложения

## Быстрый старт

### Установка

```bash
pip install layoutml
```

## Пример использования

```python
from layoutml import LayoutML, Page
from layoutml.elements import Header, Paragraph, Button
# Создание приложения
app = LayoutML()
# Определение маршрута
@app._router.route("/")
def home():
    page = Page(title="Главная")

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
app.start()
```

```python
import uvicorn
from layoutml import LayoutML, Page
from layoutml.elements import Header, Paragraph, Button

# Создание приложения
app = LayoutML()
# Определение маршрута
@app._router.route("/")
def home():
    page = Page(title="Главная")

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

if __name__ == "__main__":
  uvicorn.run(app, host="0.0.0.0", port=8000)
```

## Статус проекта

LayoutML находится в активной разработке.

## 📄 Лицензия

MIT License

# Запуск приложение в решиби разработки

uvicorn main:app --reload --port 5005
