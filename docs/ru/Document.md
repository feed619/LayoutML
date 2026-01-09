# Document

`Document` - является специализированным наследником базового класса HTMLElement, предназначенным для создания HTML <body> элемента с управлением основным содержимым страницы. Этот класс предоставляет удобный объектно-ориентированный интерфейс для добавления элементов, скриптов и управления фоном веб-страницы.

---

## Импорт

```python
from LayoutML import Document
```

## Конструктор

### def **init**(self, doctype: str = "html", \*\*kwargs)

Инициализирует новый Body элемент с начальным содержимым и атрибутами.


Параметры:

- doctype (str) - тип документа. Все возможные значения находятся в классе [DocTypes](types/FormTypes.md).
- **kwargs - дополнительные аргументы, передаваемые в родительский класс HTMLElement

| Параметр      | Тип           | По умолчанию | Описание                      |
| ------------- | ------------- | ------------ | ----------------------------- |
| doctype       | str           | "html"       | Тип HTML документа            |
| head          | Head          | Head()       | Объект заголовка документа    |
| body          | Body          | Body()       | Объект тела документа         |
| custom_prefix | Optional[str] | None         | Пользовательский HTML префикс |
| custom_suffix | Optional[str] | None         | Пользовательский HTML суффикс |

Примеры инициализации:

```python
# Простой документ
doc = Document()

# Документ с кастомным doctype
doc = Document(doctype="xhtml")

# Документ с атрибутами
doc = Document(
    doctype="html5",
    class_="no-js",
    lang="ru",
    data_theme="dark"
)
```

## Методы

### set_head(head: Head) -> "Document"

Устанавливает заголовок документа.

```python
head = Head(title="Мой сайт")
doc.set_head(head)
```

### set_body(body: Body) -> "Document"

Устанавливает тело документа.

```python
body = Body()
body.add_element("<h1>Привет мир!</h1>")
doc.set_body(body)
```

### set_doctype(doctype: str) -> "Document"

Устанавливает тип документа (DOCTYPE).

```python
doc.set_doctype("html5")      # <!DOCTYPE html>
doc.set_doctype("xhtml")      # <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" ...>
doc.set_doctype("strict")     # <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" ...>
doc.set_doctype("transitional") # <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" ...>
```

### set_language(lang: str) -> "Document"

Устанавливает язык документа. Добавляет атрибут lang к тегу <html>.

```python
doc.set_language("ru")    # <html lang="ru">
doc.set_language("en")    # <html lang="en">
doc.set_language("de")    # <html lang="de">
```

### add_prefix(html: str) -> "Document"

Добавляет пользовательский HTML код перед документом (например, комментарии, условия для IE).

```python
doc.add_prefix("<!--[if IE]><![endif]-->")
doc.add_prefix("<!-- Built with LayoutML -->")
```

### add_suffix(html: str) -> "Document"

Добавляет пользовательский HTML код после документа.

```python
doc.add_suffix("<!-- Google Analytics -->")
doc.add_suffix("<script>console.log('Page loaded')</script>")
```

### render() -> str

Генерирует полный HTML документ в виде строки.

```python
html = doc.render()
```

Структура вывода:

- Пользовательский префикс (если есть)
- DOCTYPE
- Открывающий тег <html> с атрибутами
- Заголовок (<head>)
- Тело (<body>)
- Закрывающий тег </html>
- Пользовательский суффикс (если есть)

### get_html() -> str

Алиас для метода render().

```python
html = doc.get_html()
```

### save(filename: str, encoding: str = "utf-8") -> None

Сохраняет документ в файл.

```python
doc.save("index.html")                 # Сохраняет с кодировкой UTF-8
doc.save("page.html", encoding="cp1251") # Сохраняет с другой кодировкой
```
