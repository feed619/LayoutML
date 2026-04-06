# Span

`Span` - это специализированный класс для создания HTML элемента <span>. Класс наследуется от [BaseElement](../base/BaseElement.md) и предназначен для создания строчных (inline) контейнеров для группировки и стилизации текста или других элементов без добавления семантического значения.

---

## Импорт

```python
from layoutML.elements import Span
```

## Наследование

- Родительский класс: BaseElement
- Тип элемента: span (не самозакрывающийся тег)
- Назначение: Создание строчных контейнеров для стилизации и группировки контента

## Конструктор

### **init**(text="", object_name=None, style=None, boolean_attributes=[], \*\*kwargs)

Создаёт новый строчный элемент span с указанными параметрами.

Параметры:

- text (str): Текст внутри элемента. По умолчанию пустая строка
- object_name (опционально): Имя/идентификатор элемента
- style (опционально): CSS строка для inline стилей
- boolean_attributes (опционально): Список булевых атрибутов
- \*_kwargs: Дополнительные HTML атрибуты (id, class\_, aria-_ и т.д.)

Автоматически устанавливаемые свойства:

- Тег: span
- self_closing: False (не самозакрывающийся тег)
- object_type: "SpanElement"
- text: текст элемента

Примеры:

```python
# Пустой span
span = Span()
# Span с текстом
span = Span(text="Выделенный текст")
# Span с текстом и атрибутами
span = Span(
    text="Важное слово",
    object_name="highlight",
    class_="important-text",
    style="color: red; font-weight: bold;"
)
```

## Примеры использования

### Выделение текста

```python
# Цветовое выделение
highlight = Span(
    text="важный текст",
    class_="highlight",
    style="background-color: yellow; font-weight: bold;"
)
# Форматирование внутри параграфа
paragraph = Paragraph()
paragraph.get_html(content=f'''
    Это обычный текст, а это {highlight.get_html()}, на который стоит обратить внимание.
''')
```

### Иконки и символы

```python
# Иконка через span
icon_span = Span(
    text="🔍",
    class_="icon",
    style="font-size: 20px; margin-right: 5px;"
)
# Иконка с текстом
search_span = Span(
    text="Поиск",
    class_="search-label"
)
search_container = Span()
search_container.get_html(content=f"{icon_span.get_html()} {search_span.get_html()}")
```

### Стилизованные фрагменты

```python
# Разные стили в одном тексте
name_span = Span(
    text="Иван Петров",
    class_="name",
    style="font-weight: bold; color: #007bff;"
)
role_span = Span(
    text="(Разработчик)",
    class_="role",
    style="color: #666; font-size: 0.9em;"
)
user_info = Span()
user_info.get_html(content=f"{name_span.get_html()} {role_span.get_html()}")
```

### Интерактивные элементы

```python
# Кликабельный span
clickable_span = Span(
    text="Нажми меня",
    class_="clickable",
    style="cursor: pointer; color: blue; text-decoration: underline;"
)
# Добавление события
clickable_span.add_event("onclick", "alert('Span clicked!')")
```

### Хлебные крошки

```python
# Разделители в хлебных крошках
separator = Span(
    text="/",
    class_="separator",
    style="margin: 0 8px; color: #999;"
)
breadcrumb = Span()
breadcrumb.get_html(content=f'''
    <a href="/">Главная</a>
    {separator.get_html()}
    <a href="/catalog">Каталог</a>
    {separator.get_html()}
    <span>Товары</span>
''')
```
