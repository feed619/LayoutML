# Body

`Body` - это специализированный класс для создания HTML <body> элемента является наследником базового класса [HTMLElement](base/HTMLElement.md). Класс предоставляет удобный интерфейс для управления основным содержимым веб-страницы, включая добавление HTML элементов, текстового содержимого и скриптов, которые должны выполняться после загрузки DOM.

---

## Импорт

```python
from layoutml import Body
```

## Наследование

- Родительский класс: BaseElement
- Тип элемента: body
- Назначение: Контейнер для основного содержимого страницы

## Атрибуты класса

| Атрибут        | Тип               | Описание                                   | Значение по умолчанию |
| -------------- | ----------------- | ------------------------------------------ | --------------------- |
| content        | str               | Текстовое содержимое body                  | Пустая строка         |
| elements       | List[BaseElement] | Список HTML элементов                      | Пустой список         |
| scripts_footer | List[Dict]        | Список script тегов для конца body         | Пустой список         |
| object_type    | str               | Тип объекта (всегда "Body")                | "Body"                |
| links          | dict              | Зарезервировано для будущего использования | Пустой словарь        |

## Конструктор

### **init**(content: str = "", \*\*kwargs)

Инициализирует новый Body элемент с начальным содержимым и атрибутами.

Параметры:

| Параметр    | Тип  | По умолчанию | Описание                                |
| ----------- | ---- | ------------ | --------------------------------------- |
| content     | str  | ""           | Начальное текстовое содержимое body     |
| object_name | str  | None         | Уникальный идентификатор элемента       |
| \*\*kwargs  | dict | -            | Дополнительные атрибуты для тега <body> |

Примеры инициализации:

```python
# Пустой body с базовыми атрибутами
body = Body()
# Body с начальным содержимым
body = Body(content="Добро пожаловать на наш сайт!")
# Body с атрибутами класса
body = Body(
    content="Содержимое страницы",
    class_="main-body dark-theme",
    id="pageBody",
    data_page="home"
)
# Body с обработчиками событий
body = Body(
    onload="initPage()",
    onscroll="handleScroll()",
    onresize="handleResize()"
)
```

## Методы

### add_content(content: str) -> "Body"

Добавляет текстовое содержимое к body.

Параметры:

- content (str): Текст для добавления

Возвращает:

- self: Позволяет использовать цепочки вызовов

Примеры:

```python
# Простое добавление текста
body = Body()
body.add_content("Добро пожаловать на наш сайт!")
# Цепочка вызовов
body.add_content("Основной контент").add_content("Дополнительный текст")
# Добавление форматированного текста
body.add_content("<h1>Заголовок</h1>")
body.add_content("<p>Абзац текста с <strong>выделением</strong>.</p>")
# Многострочный контент
body.add_content("""
    <div class="intro">
        <h2>Введение</h2>
        <p>Это первая страница нашего сайта.</p>
    </div>
""")
```

### add_element(element: Any) -> "Body"

Добавляет HTML элемент в body.

Поддерживаемые типы элементов:

- Объекты BaseElement и его наследники
- Объекты Layout, HorizontalLayout, VerticalLayout
- Объекты Form
- Любые другие объекты с методом get_html()
- Строки (сырой HTML)

```python
body = Body()
# Добавление различных типов элементов
body.add_element(BaseElement(tag="div", object_name="container"))
body.add_element(Form(form_type="text", object_name="search"))
body.add_element(Layout(object_name="mainLayout"))
```

### add_html(html: str) -> "Body"

Добавляет сырой HTML код в body.

```python
body = Body()
body.add_html("<div class='custom'>Свой HTML</div>")
body.add_html("<!-- Комментарий -->")
```

### add_script(src: Optional[str] = None, content: Optional[str] = None, \*\*attributes) -> "Body"

Добавляет script тег в конец body (перед закрывающим тегом </body>).

Параметры:

- src (опционально): URL внешнего скрипта
- content (опционально): Inline JavaScript код
- \*\*attributes: Дополнительные атрибуты

```python
body = Body()
# Внешний скрипт
body.add_script(src="app.js", defer=True)
body.add_script(src="analytics.js", async=True)
# Inline скрипт
body.add_script(content="console.log('DOM загружен');")
# Скрипт с кастомными атрибутами
body.add_script(
    src="https://cdn.example.com/library.js",
    integrity="sha256-abc123",
    crossorigin="anonymous"
)
# Скрипт с type="module"
body.add_script(src="module.js", type="module")
```

### get_html() -> str

Генерирует полный HTML код секции <body>.

```python
body = Body()
body.add_content("<h1>Заголовок</h1>")
html = body.get_html()  # <body>...</body>
```

### get_styles() -> dict

Собирает CSS стили из всех элементов body.

```python
body = Body()
div = BaseElement(tag="div", object_name="test")
div.object_styles.set_width("100px")

body.add_element(div)
styles = body.get_styles()  # Словарь со стилями
```

## Специальные методы Python

### **str**() -> str

Возвращает HTML представление body.

```python
body = Body(content="Hello")
print(str(body))  # Выводит HTML
```

### **repr**() -> str

Возвращает строковое представление для отладки.

```python
body = Body()
body.add_element(BaseElement(tag="div"))
print(repr(body))  # Body(elements=1, content_length=0)
```

### **iadd**(other: Any) -> "Body"

Перегрузка оператора += для удобного добавления элементов.

```python
body = Body()
body += BaseElement(tag="div", object_name="box1")
body += "<span>Текст</span>"
# Эквивалентно body.add_element(...)
```
