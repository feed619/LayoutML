# Head

`Head` - является специализированным наследником базового класса [BaseElement](base/BaseElement.md), предназначенным для создания HTML <head> элемента с полным набором мета-тегов, стилей, скриптов и других ресурсов, необходимых для веб-страницы. Этот класс предоставляет удобный объектно-ориентированный интерфейс для управления мета-информацией и ресурсами страницы.

---

## Импорт

```python
from layoutml import Head
```

## Наследование

- Родительский класс: BaseElement
- Тип элемента: head
- Назначение: Управление метаданными и ресурсами HTML страницы

## Конструктор

### **init**(title: str = "", \*\*kwargs)

Инициализирует новый Head элемент с базовой конфигурацией.

Параметры:

| Параметр    | Тип  | По умолчанию | Описание                                              |
| ----------- | ---- | ------------ | ----------------------------------------------------- |
| title       | str  | ""           | Заголовок страницы (отображается во вкладке браузера) |
| object_name | str  | None         | Уникальный идентификатор элемента                     |
| \*\*kwargs  | dict | -            | Дополнительные атрибуты для тега <head>               |

Автоматически устанавливаемые свойства:

- Тег: head
- Кодировка: UTF-8 (<meta charset="UTF-8">)
- Viewport: адаптивный (<meta name="viewport" content="width=device-width, initial-scale=1.0">)

Примеры:

```python
# Простой head
head = Head()
# Head с заголовком
head = Head(title="Мой сайт")
# Head с дополнительными атрибутами
head = Head(
    title="Документация",
    object_name="pageHead",
    lang="ru"
)
```

## Атрибуты класса

| Атрибут     | Тип           | Описание                                 | Значение по умолчанию       |
| ----------- | ------------- | ---------------------------------------- | --------------------------- |
| title       | str           | Заголовок страницы (тег <title>)         | Пустая строка               |
| meta_tags   | List[Dict]    | Список мета-тегов                        | Содержит charset и viewport |
| links       | List[Dict]    | Список link тегов (стили, иконки и т.д.) | Пустой список               |
| scripts     | List[Dict]    | Список script тегов                      | Пустой список               |
| styles_css  | List[str]     | Список inline CSS стилей                 | Пустой список               |
| base_url    | Optional[str] | Базовый URL для относительных путей      | None                        |
| object_type | str           | Тип объекта (всегда "Head")              | "Head"                      |

## Методы

### set_title(title: str) -> "Head"

Устанавливает или изменяет заголовок страницы.

Параметры:

- title (str): Новый заголовок страницы
  Возвращает:

Примеры:

```python
# Установка заголовка при создании
head = Head(title="Исходный заголовок")
# Изменение заголовка
head.set_title("Новый заголовок страницы")
# Цепочка вызовов
head.set_title("Продукты").add_meta(name="description", content="Каталог продукции")
```

### add_meta(\*\*attributes) -> "Head"

Добавляет мета-тег с указанными атрибутами.

Параметры:

- \*\*attributes: Пары ключ-значение для атрибутов мета-тега

Возвращает:

- self: Позволяет использовать цепочки вызовов

Типичные мета-теги:

```python
# Кодировка (уже добавлена по умолчанию)
head.add_meta(charset="UTF-8")
# Viewport для мобильных устройств (уже добавлен по умолчанию)
head.add_meta(name="viewport", content="width=device-width, initial-scale=1.0")
# Описание страницы для SEO
head.add_meta(
    name="description",
    content="Интернет-магазин электроники с доставкой по всей России"
)
# Ключевые слова для SEO
head.add_meta(
    name="keywords",
    content="электроника, смартфоны, ноутбуки, доставка, интернет-магазин"
)
```

### add_link(rel: str, href: str, \*\*attributes) -> "Head"

Добавляет link тег для подключения внешних ресурсов.

Параметры:

- rel: Отношение ресурса (stylesheet, icon, canonical и т.д.)
- href: URL ресурса
- \*\*attributes: Дополнительные атрибуты

Примеры:

```python

head = Head()

# CSS стили
head.add_link(rel="stylesheet", href="style.css")
head.add_link(rel="stylesheet", href="mobile.css", media="(max-width: 768px)")

# Иконки
head.add_link(rel="icon", href="favicon.ico", type="image/x-icon")
head.add_link(rel="apple-touch-icon", href="apple-touch-icon.png")

# Канонический URL
head.add_link(rel="canonical", href="https://example.com/page")

# Предзагрузка шрифтов
head.add_link(rel="preload", href="font.woff2", as_="font", type="font/woff2", crossorigin=True)

# RSS feed
head.add_link(rel="alternate", href="rss.xml", type="application/rss+xml", title="RSS")
```

### add_stylesheet(href: str, media: str = "all") -> "Head"

Упрощенный метод для добавления CSS файлов.

```python
head = Head()
head.add_stylesheet("style.css")
head.add_stylesheet("print.css", media="print")
```

### add_icon(href: str, type: str = "image/x-icon") -> "Head"

Упрощенный метод для добавления фавиконки.

```python
head = Head()
head.add_icon("favicon.ico")
head.add_icon("icon.png", type="image/png")
```

### add_script(src: Optional[str] = None, content: Optional[str] = None, \*\*attributes) -> "Head"

Добавляет тег <script> с указанными параметрами.

Параметры:

- src (Optional[str]): URL внешнего скрипта
- content (Optional[str]): Встроенный JavaScript код
- \*\*attributes: Дополнительные атрибуты

Возвращает:

- self: Позволяет использовать цепочки вызовов

Примеры:

```python
# Внешний скрипт с defer
head.add_script(src="/js/main.js", defer=True)
# Внешний скрипт с async
head.add_script(src="/js/analytics.js", async=True)
# Внешний модуль
head.add_script(src="/js/app.js", type="module")
# Встроенный скрипт
head.add_script(
    content="""
        console.log('Страница загружается');
        window.APP_CONFIG = {
            apiUrl: 'https://api.example.com',
            debug: false
        };
    """,
    type="application/javascript"
)

```

### get_css_text() -> str

Генерирует текст inline CSS стилей из selectors_styles.

```python
head = Head()
head.object_styles.set_background_color("red")
css_text = head.get_css_text()  # Генерирует <style>...</style>
```

### get_html() -> str

Генерирует полный HTML код секции <head>.

```python
head = Head(title="Страница")
html = head.get_html()  # <head>...</head>
```

## Примеры

### Пример 1: Базовая страница

```python
head = Head(title="Добро пожаловать на мой сайт")
# Мета-теги
head.add_meta(name="description", content="Личный блог о программировании и технологиях")
head.add_meta(name="keywords", content="программирование, python, блог, технологии")
head.add_meta(name="author", content="Иван Петров")
# Стили
head.add_stylesheet("css/main.css")
head.add_stylesheet("css/mobile.css", media="(max-width: 768px)")
# Иконки
head.add_icon("favicon.ico")
head.add_link(rel="apple-touch-icon", href="apple-touch-icon.png")
# Скрипты
head.add_script(src="js/app.js", defer=True)
print(head.get_html())
```
