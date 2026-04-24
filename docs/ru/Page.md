# Page

`Page` - является специализированным наследником базового класса [BaseElement](base/BaseElement.md), для создания полных HTML документов. Класс объединяет компоненты Head и Body в единую структуру и предоставляет методы для рендеринга, сохранения и управления всем HTML документом.

---

## Импорт

```python
from layoutml import Page
```

## Наследование

- Родительский класс: BaseElement
- Тип элемента: html (корневой элемент документа)
- Назначение: Создание полных HTML страниц со всей необходимой структурой

## Атрибуты класса

| Атрибут     | Тип  | Описание                    | Значение по умолчанию             |
| ----------- | ---- | --------------------------- | --------------------------------- |
| doctype     | str  | Тип HTML документа          | "html"                            |
| head        | Head | Объект секции head          | Создаётся с заголовком "LayoutML" |
| body        | Body | Объект секции body          | Пустой объект Body                |
| object_type | str  | Тип объекта (всегда "Page") | "Page"                            |

## Конструктор

### **init**(doctype: str = "html", title: str = "LayoutML", lang="ru", object_name=None, \*\*kwargs)

Создаёт новую HTML страницу с базовыми настройками.

Параметры:

- doctype (str): Тип документа. По умолчанию "html" (HTML5). Поддерживаемые значения можно получить из файла [DocTypes](types/DocTypes.md)
- title (str): Заголовок страницы. По умолчанию "LayoutML"
- lang (str): Язык документа. По умолчанию "ru"
- object_name (опционально): Имя/идентификатор страницы
- \*\*kwargs: Дополнительные атрибуты HTML элемента

Автоматически создаваемые компоненты:

- Объект Head с указанным заголовком
- Объект Body для основного содержимого
- Устанавливается тег html с указанным языком

Примеры:

```python
# Простая страница
page = Page()
# Страница с кастомизацией
page = Page(
    title="Мой сайт",
    lang="ru",
    doctype="html5",
    object_name="homePage"
)
# Страница с дополнительными атрибутами
page = Page(
    title="Документация",
    class_="documentation",
    data_theme="dark"
)
```

## Методы

### set_head(head: Head) -> "Page"

Заменяет объект head страницы на пользовательский.

```python
custom_head = Head(title="Кастомный заголовок")
page = Page()
page.set_head(custom_head)
```

### set_body(body: Body) -> "Page"

Заменяет объект body страницы на пользовательский.

```python
custom_body = Body()
custom_body.add_content("<h1>Привет!</h1>")
page = Page()
page.set_body(custom_body)
```

### set_doctype(doctype: str) -> "Page"

Устанавливает тип документа.

```python
page = Page()
page.set_doctype("html5")      # HTML5
page.set_doctype("xhtml")      # XHTML 1.0 Transitional
page.set_doctype("strict")     # HTML 4.01 Strict
page.set_doctype("transitional")  # HTML 4.01 Transitional
```

### set_language(lang: str) -> "Page"

Устанавливает язык документа (атрибут lang тега <html>).

```python
page = Page()
page.set_language("en")    # Английский
page.set_language("ru")    # Русский
page.set_language("es")    # Испанский
```

### add_element(element)

Добавляет элемент в body документа.

Параметры:

- element (BaseElement): HTML элемент для добавления

Примечание: Этот метод предназначен для совместимости со старым кодом и работает с атрибутом document, который должен быть установлен.

```python
from layoutml import Paragraph

app = LayoutML()
app.add_element(Paragraph(text="Привет, мир!"))
```

### add_script(src: Optional[str] = None, content: Optional[str] = None, \*\*attributes) -> "Page"

Добавляет script тег в секцию head.

Параметры:

- src (опционально): URL внешнего скрипта
- content (опционально): Inline JavaScript код
- \*\*attributes: Дополнительные атрибуты (defer, async, type и т.д.)

```python
page = Page()
# Внешний скрипт
page.add_script(src="app.js", defer=True)
# Inline скрипт
page.add_script(content="console.log('Page loaded');")
# Скрипт с кастомными атрибутами
page.add_script(
    src="https://cdn.example.com/library.js",
    integrity="sha256-abc123",
    crossorigin="anonymous"
)
```

### get_html() -> str

Генерирует полный HTML код документа.

```python
page = Page(title="Тестовая страница")
html = page.get_html()  # Полный HTML документ
```

### render() -> str

Рендерит полный HTML документ с автоматическим созданием CSS файла.

Особенности:

- Собирает CSS стили из всех компонентов
- Создает CSS файл в папке styles/
- Добавляет ссылку на созданный CSS файл в head
- Возвращает полный HTML документ

```python
page = Page()
page.body.add_element(BaseElement(tag="div", object_name="test"))
html = page.render()  # Создает CSS файл и возвращает HTML
```

### get_css_text() -> str

Генерирует текст CSS стилей из всех компонентов страницы.

```python
page = Page()
css_text = page.get_css_text()  # Все CSS стили в одной строке
```

### get_styles() -> dict

Собирает CSS стили из всех компонентов страницы в словарь.

```python
page = Page()
styles = page.get_styles()  # Словарь {селектор: стили}
```

### save(filename: str, encoding: str = "utf-8") -> None

Сохраняет HTML документ в файл.

```python
page = Page(title="Моя страница")
page.save("index.html")               # Сохраняет в index.html
page.save("page.html", encoding="utf-8-sig")  # С указанной кодировкой
```

## Примеры использования

### Пример 1: Простая HTML страница

```python
# Создание базовой страницы
page = Page(
    title="Добро пожаловать на мой сайт",
    lang="ru",
    doctype="html5"
)

# Настройка head
page.head.add_meta(
    name="description",
    content="Личный сайт о программировании и технологиях"
)
page.head.add_stylesheet("css/style.css")
page.head.add_script(src="js/app.js", defer=True)

# Добавление содержимого в body
page.body.add_content("""
    <header>
        <h1>Привет, мир!</h1>
    </header>

    <main>
        <p>Это моя первая страница, созданная с помощью LayoutML.</p>
    </main>

    <footer>
        <p>&copy; 2024 Мой сайт</p>
    </footer>
""")

# Сохранение в файл
page.save("index.html")

# Или получение HTML кода
html_code = page.get_html()
print(html_code)
```
