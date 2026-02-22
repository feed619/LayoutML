# Label

`Label` - это специализированный класс для создания HTML элемента метки <label>. Класс наследуется от [BaseElement](../base/BaseElement.md) и предназначен для создания текстовых меток, связанных с элементами форм, что улучшает доступность и удобство использования веб-форм.

---

## Импорт

```python
from layoutML.elements import Label
```

## Наследование

- Родительский класс: BaseElement
- Тип элемента: label (не самозакрывающийся тег)
- Назначение: Создание меток для элементов форм

## Конструктор

### **init**(for_id=None, text="", object_name=None, style=None, boolean_attributes=[], \*\*kwargs)

Создаёт новый элемент метки с указанными параметрами.

### Параметры:

- for_id (str): Идентификатор элемента формы, с которым связана метка. По умолчанию None
- text (str): Текст метки. По умолчанию пустая строка
- object_name (опционально): Имя/идентификатор элемента
- style (опционально): CSS строка для inline стилей
- boolean_attributes (опционально): Список булевых атрибутов
- \*_kwargs: Дополнительные HTML атрибуты (class\_, aria-_ и т.д.)

### Автоматически устанавливаемые свойства:

- Тег: label
- self_closing: False (не самозакрывающийся тег)
- object_type: "LabelElement"
- text: текст метки
- for_id: идентификатор связанного элемента формы

### Примеры:

```python
# Простая метка
label = Label(text="Имя пользователя")

# Метка, связанная с полем ввода
label = Label(
    for_id="username-field",
    text="Имя пользователя",
    class_="form-label"
)

# Метка с inline стилями
label = Label(
    text="Email адрес",
    style="font-weight: bold; color: #333;",
    aria_label="Поле для ввода email"
)
```

## Примеры использования

### Простые метки

```python
# Базовая метка
label1 = Label(text="Имя пользователя")

# Метка с классом
label2 = Label(
    text="Email",
    class_="form-label required"
)

# Метка с идентификатором
label3 = Label(
    text="Пароль",
    id="password-label",
    for_id="password-field"
)
```

### Метки для разных типов полей

```python
from layoutml import Input

# Метка для текстового поля
text_label = Label(
    for_id="username",
    text="Имя пользователя:",
    class_="field-label"
)
text_input = Input(id="username", placeholder="Введите имя")

# Метка для email
email_label = Label(
    for_id="user-email",
    text="Email адрес:",
    class_="field-label required"
)
email_input = Input(
    input_type="email",
    id="user-email",
    placeholder="user@example.com"
)

# Метка для чекбокса
checkbox_label = Label(
    for_id="agree-terms",
    text="Я согласен с условиями"
)
checkbox_input = Input(
    input_type="checkbox",
    id="agree-terms",
    value="yes"
)
```
