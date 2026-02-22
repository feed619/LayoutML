# Input

`Input` - это специализированный класс для создания HTML элементов ввода <input>. Класс наследуется от [Form](Form.md) и предоставляет удобный интерфейс для создания полей ввода с часто используемыми атрибутами, такими как placeholder, value, name и id.

---

## Импорт

```python
from layoutML.elements import Input
```

Наследование

    Родительский класс: Form (который наследуется от BaseElement)

    Тип элемента: input (самозакрывающийся тег)

    Назначение: Создание полей ввода для форм

## Конструктор

### **init**(input_type="text", placeholder="", value="", name=None, id=None, object_name=None, style=None, boolean_attributes=[], \*\*kwargs)

Создаёт новый элемент ввода с указанными параметрами.

### Параметры:

- input_type (str): Тип поля ввода. По умолчанию "text"
- placeholder (str): Текст-подсказка внутри поля. По умолчанию пустая строка
- value (str): Значение поля. По умолчанию пустая строка
- name (str): Имя поля для отправки на сервер. По умолчанию None
- id (str): Уникальный идентификатор поля. По умолчанию None
- object_name (опционально): Имя/идентификатор элемента
- style (опционально): CSS строка для inline стилей
- boolean_attributes (опционально): Список булевых атрибутов (disabled, readonly, required и т.д.)
- \*\*kwargs: Дополнительные HTML атрибуты

### Автоматически устанавливаемые свойства:

- Тег: input
- self_closing: True (самозакрывающийся тег)
- object_type: "InputElement"
- form_type: значение параметра input_type (передаётся в родительский класс)
- placeholder: текст-подсказка
- value: значение поля
- name: имя поля
- id: идентификатор поля

### Примеры:

```python
# Простое текстовое поле
input_text = Input(placeholder="Введите имя")

# Поле с полным набором атрибутов
input_email = Input(
    input_type="email",
    placeholder="Ваш email",
    value="user@example.com",
    name="user_email",
    id="email-field",
    class_="form-input",
    required=True
)

# Поле с inline стилями
input_search = Input(
    input_type="search",
    placeholder="Поиск...",
    style="padding: 10px; border-radius: 5px;",
    aria_label="Поле поиска"
)
```

## Поддерживаемые типы полей ввода

Класс Input поддерживает все стандартные HTML5 типы полей ввода через параметр input_type:

| Тип        | Описание                                   |
| ---------- | ------------------------------------------ |
| "text"     | Однострочное текстовое поле (по умолчанию) |
| "password" | Поле для пароля (символы скрываются)       |
| "email"    | Поле для email адреса                      |
| "number"   | Поле для чисел                             |
| "tel"      | Поле для телефонного номера                |
| "url"      | Поле для URL адреса                        |
| "search"   | Поле для поиска                            |
| "date"     | Поле для даты                              |
| "time"     | Поле для времени                           |
| "datetime- | local" Поле для локальной даты и времени   |
| "month"    | Поле для месяца                            |
| "week"     | Поле для недели                            |
| "color"    | Поле для выбора цвета                      |
| "range"    | Ползунок                                   |
| "file"     | Поле для загрузки файлов                   |
| "checkbox" | Флажок                                     |
| "radio"    | Переключатель                              |
| "hidden"   | Скрытое поле                               |

## Примеры

### Разные типы полей

```python
# Дата
date_field = Input(
    input_type="date",
    name="birth_date",
    min="1900-01-01",
    max="2026-12-31"
)

# Цвет
color_field = Input(
    input_type="color",
    name="theme_color",
    value="#007bff"
)

# Диапазон
range_field = Input(
    input_type="range",
    name="volume",
    min="0",
    max="100",
    value="50",
    step="5"
)

# Файл
file_field = Input(
    input_type="file",
    name="document",
    accept=".pdf,.doc,.docx",
    multiple=True
)
```

## Поля с валидацией

```python
# Email с валидацией
email_field = Input(
    input_type="email",
    placeholder="user@example.com",
    name="email",
    required=True,
    pattern="[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$",
    title="Введите корректный email адрес"
)

# Число с ограничениями
quantity_field = Input(
    input_type="number",
    placeholder="Количество",
    name="quantity",
    min="1",
    max="100",
    step="1",
    required=True
)

# URL с валидацией
url_field = Input(
    input_type="url",
    placeholder="https://example.com",
    name="website",
    pattern="https?://.+"
)
```
