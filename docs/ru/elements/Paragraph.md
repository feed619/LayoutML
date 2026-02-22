# Paragraph

`Paragraph` - это специализированный класс для создания HTML элемента параграфа <p>. Класс наследуется от [BaseElement](../base/BaseElement.md) и предоставляет удобный интерфейс для создания текстовых абзацев с возможностью установки текста через конструктор или при генерации HTML.

---

## Импорт

```python
from layoutML.elements import Paragraph
```

## Наследование

- Родительский класс: BaseElement
- Тип элемента: p (не самозакрывающийся тег)
- Назначение: Создание текстовых параграфов для структурирования контента

## Конструктор

### **init**(text="", object_name=None, style=None, boolean_attributes=[], \*\*kwargs)

Создаёт новый элемент параграфа с указанными параметрами.

### Параметры:

- text (str): Текст параграфа. По умолчанию пустая строка
- object_name (опционально): Имя/идентификатор элемента
- style (опционально): CSS строка для inline стилей
- boolean_attributes (опционально): Список булевых атрибутов
- \*_kwargs: Дополнительные HTML атрибуты (id, class\_, aria-_ и т.д.)

### Автоматически устанавливаемые свойства:

- Тег: p
- self_closing: False (не самозакрывающийся тег)
- object_type: "ParagraphElement"
- text: текст параграфа

### Примеры:

```python
# Пустой параграф
p = Paragraph()

# Параграф с текстом
p = Paragraph(text="Это текст параграфа.")

# Параграф с текстом и атрибутами
p = Paragraph(
    text="Добро пожаловать на наш сайт!",
    object_name="welcomeMessage",
    class_="intro-text",
    style="font-size: 16px; line-height: 1.5;"
)
```

## Примеры

### Простые параграфы

```python
# Базовый параграф
p1 = Paragraph(text="Это обычный текст в параграфе.")

# Параграф с классом
p2 = Paragraph(
    text="Это важный текст.",
    class_="important"
)

# Параграф с идентификатором
p3 = Paragraph(
    text="Уникальный параграф",
    id="unique-paragraph"
)
```

### Стилизованные параграфы

```python
p = Paragraph(
    text="Стилизованный параграф с красивым оформлением.",
    object_name="styledParagraph"
)

# Inline стили
p.inline_styles.set_font_family("Georgia, serif")\
               .set_font_size("18px")\
               .set_line_height("1.8")\
               .set_color("#333")\
               .set_margin_bottom("20px")

# CSS стили через object_styles
p.object_styles.set_text_indent("20px")\
               .set_letter_spacing("0.5px")

# Псевдо-элементы
p.selectors_styles.add_selector("styledParagraph::first-letter")\
    .set_font_size("24px")\
    .set_font_weight("bold")\
    .set_color("#007bff")

p.selectors_styles.add_selector("styledParagraph::first-line")\
    .set_font_weight("bold")
```
