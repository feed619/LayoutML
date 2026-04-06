# Textarea

`Textarea` - это специализированный класс для создания HTML элемента многострочного текстового поля <textarea>. Класс наследуется от [BaseElement](../base/BaseElement.md) и предоставляет удобный интерфейс для создания текстовых областей с настраиваемым размером, текстом-подсказкой и другими атрибутами.

---

## Импорт

```python
from layoutML.elements import Textarea
```

## Наследование

- Родительский класс: BaseElement
- Тип элемента: textarea (не самозакрывающийся тег)
- Назначение: Создание многострочных текстовых полей для ввода больших объёмов текста

## Конструктор

### **init**(placeholder="", value="", rows=4, cols=50, name=None, id=None, object_name=None, style=None, boolean_attributes=[], \*\*kwargs)

Создаёт новое многострочное текстовое поле с указанными параметрами.

Параметры:

- placeholder (str): Текст-подсказка внутри поля. По умолчанию пустая строка
- value (str): Предустановленный текст в поле. По умолчанию пустая строка
- rows (int): Количество видимых строк. По умолчанию 4
- cols (int): Количество видимых столбцов. По умолчанию 50
- name (str): Имя поля для отправки на сервер. По умолчанию None
- id (str): Уникальный идентификатор поля. По умолчанию None
- object_name (опционально): Имя/идентификатор элемента
- style (опционально): CSS строка для inline стилей
- boolean_attributes (опционально): Список булевых атрибутов (required, disabled, readonly)
- \*\*kwargs: Дополнительные HTML атрибуты

Автоматически устанавливаемые свойства:

- Тег: textarea
- self_closing: False (не самозакрывающийся тег)
- object_type: "TextareaElement"
- placeholder: текст-подсказка
- value: предустановленный текст
- rows: количество строк
- cols: количество столбцов
- name: имя поля
- id: идентификатор поля

Пример :

```python
# Простое текстовое поле
textarea = Textarea()
# Текстовое поле с настройками
textarea = Textarea(
    placeholder="Введите ваш отзыв...",
    rows=6,
    cols=60,
    name="review",
    id="review-field"
)
# Текстовое поле с предустановленным текстом
textarea = Textarea(
    value="Это предустановленный текст.\nОн может занимать несколько строк.",
    rows=5,
    class_="form-textarea",
    required=True
)
```

## Примеры использования

### Базовая текстовая область

```python
# Простое поле для комментариев
comment = Textarea(
    placeholder="Оставьте ваш комментарий...",
    rows=5,
    cols=60,
    name="comment"
)
# Поле с предустановленным текстом
feedback = Textarea(
    value="Отличная работа! Спасибо.",
    rows=4,
    name="feedback"
)
```

### Форма обратной связи

```python
from layoutml import Form, Input, Button, Label
form = Form(action="/submit", method="post")
# Имя
form.add_element(Label(for_id="name", text="Имя:"))
form.add_element(Input(id="name", name="name", required=True))
# Email
form.add_element(Label(for_id="email", text="Email:"))
form.add_element(Input(type="email", id="email", name="email", required=True))
# Сообщение
form.add_element(Label(for_id="message", text="Сообщение:"))
message_field = Textarea(
    id="message",
    name="message",
    placeholder="Введите ваше сообщение...",
    rows=6,
    required=True
)
form.add_element(message_field)
# Кнопка отправки
form.add_element(Button(text="Отправить", type="submit"))
```

### Стилизованная текстовая область

```python
textarea = Textarea(
    object_name="styledTextarea",
    placeholder="Ваш отзыв...",
    rows=5
)
# Inline стили
textarea.inline_styles.set_width("100%")\
                      .set_padding("12px")\
                      .set_border("2px solid #ddd")\
                      .set_border_radius("8px")\
                      .set_font_size("16px")\
                      .set_font_family("Arial, sans-serif")\
                      .set_resize("vertical")
# Стили при фокусе
textarea.selectors_styles.add_selector("styledTextarea:focus")\
    .set_border_color("#007bff")\
    .set_outline("none")\
    .set_box_shadow("0 0 0 3px rgba(0,123,255,0.25)")
# Стили для placeholder
textarea.selectors_styles.add_selector("styledTextarea::placeholder")\
    .set_color("#999")\
    .set_font_style("italic")
```

### Текстовая область с ограничениями

```python
# Поле с ограничением длины
bio = Textarea(
    placeholder="Расскажите о себе...",
    rows=4,
    name="bio",
    maxlength="500",
    data_maxlength="500"
)
# Добавление счётчика символов через JavaScript
bio.add_event("oninput", "updateCounter(this)")
# JavaScript для счётчика
counter_script = """
function updateCounter(textarea) {
    const max = textarea.getAttribute('maxlength');
    const current = textarea.value.length;
    const counter = document.getElementById('charCounter');
    if (counter) {
        counter.textContent = current + ' / ' + max;
    }
}
"""
```

### Текстовая область с предварительным просмотром

```python
preview_textarea = Textarea(
    placeholder="Введите текст для предпросмотра...",
    rows=6,
    id="editor",
    name="content"
)
# Кнопка предпросмотра
preview_btn = Button(text="Предпросмотр", onclick="showPreview()")
# Контейнер для предпросмотра
preview_container = BaseElement(tag="div", id="preview", class_="preview")
# JavaScript для предпросмотра
preview_script = """
function showPreview() {
    const content = document.getElementById('editor').value;
    const preview = document.getElementById('preview');
    preview.innerHTML = '<h3>Предпросмотр:</h3><div class="preview-content">' +
                        content.replace(/\\n/g, '<br>') + '</div>';
}
"""
```

### Адаптивная текстовая область

```python
responsive_textarea = Textarea(
    object_name="responsiveTextarea",
    placeholder="Адаптивная текстовая область...",
    rows=4
)
# Базовые стили
responsive_textarea.object_styles.set_width("100%")\
                                  .set_box_sizing("border-box")
# Стили для разных размеров экрана
desktop_media = responsive_textarea.selectors_styles.add_selector(
    "@media (min-width: 768px)",
    selector_type="media"
)
desktop_media.set_font_size("16px")
mobile_media = responsive_textarea.selectors_styles.add_selector(
    "@media (max-width: 480px)",
    selector_type="media"
)
mobile_media.set_font_size("14px")\
           .set_padding("8px")
```

### Текстовая область с булевыми атрибутами

```python
# Обязательное поле
required_textarea = Textarea(
    placeholder="Обязательное поле",
    boolean_attributes=["required"],
    name="required_field"
)
# Только для чтения
readonly_textarea = Textarea(
    value="Этот текст нельзя изменить",
    boolean_attributes=["readonly"],
    name="readonly_field"
)
# Отключённое поле
disabled_textarea = Textarea(
    placeholder="Поле недоступно",
    boolean_attributes=["disabled"],
    name="disabled_field"
)
```

### Текстовая область в модальном окне

```python
from layoutml import VerticalLayout
modal_content = VerticalLayout(object_name="modalContent")
# Заголовок
title = BaseElement(tag="h3")
title.get_html(content="Редактировать описание")
# Текстовая область
description = Textarea(
    value="Текущее описание товара...",
    rows=8,
    name="description",
    id="edit-description"
)
# Кнопки действий
buttons = BaseElement(tag="div")
buttons.get_html(content="""
    <button onclick="saveChanges()">Сохранить</button>
    <button onclick="closeModal()">Отмена</button>
""")
modal_content.add_elements(title, description, buttons)
```

### Текстовая область с подсветкой синтаксиса (CSS классы)

```python
code_area = Textarea(
    placeholder="Введите код...",
    rows=10,
    name="code",
    class_="code-editor",
    data_language="python"
)
# Стили для редактора кода
code_area.object_styles.set_font_family("'Courier New', monospace")\
                       .set_font_size("14px")\
                       .set_background_color("#1e1e1e")\
                       .set_color("#d4d4d4")\
                       .set_border("none")\
                       .set_border_radius("8px")\
                       .set_padding("15px")
# Подсветка строк
code_area.selectors_styles.add_selector(".code-editor:focus")\
    .set_outline("2px solid #007acc")
```

## Лучшие практики

### Установка размера

```python
# Хорошо: используйте rows и cols для базового размера
good_textarea = Textarea(rows=5, cols=60)
# Лучше: используйте CSS для более гибкого управления
better_textarea = Textarea(rows=5)
better_textarea.object_styles.set_width("100%").set_height("150px")
# Плохо: слишком маленькое поле
bad_textarea = Textarea(rows=1, cols=10)
```

### Placeholder для подсказки

```python
# Хорошо: информативный placeholder
good_textarea = Textarea(
    placeholder="Напишите ваш отзыв о товаре...",
    rows=5
)
# Плохо: placeholder не даёт информации
bad_textarea = Textarea(placeholder="Текст", rows=5)
```

### Управление размером

```python
# Разрешить пользователю изменять размер
resizable_textarea = Textarea(rows=4)
resizable_textarea.object_styles.set_resize("vertical")  # Только по вертикали
# или
resizable_textarea.object_styles.set_resize("both")  # По горизонтали и вертикали
# Запретить изменение размера
fixed_textarea = Textarea(rows=4)
fixed_textarea.object_styles.set_resize("none")
```

### Доступность

```python
# Добавление ARIA атрибутов
accessible_textarea = Textarea(
    placeholder="Комментарий",
    aria_label="Поле для ввода комментария",
    aria_describedby="comment-help",
    aria_required="true"
)
# Пояснительный текст
help_text = BaseElement(tag="small", id="comment-help")
help_text.get_html(content="Максимум 500 символов")
# Связывание через aria-describedby
accessible_textarea.value_attributes["aria-describedby"] = "comment-help"
```
