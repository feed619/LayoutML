# Select

`Select` - это специализированный класс для создания HTML элемента выпадающего списка <select>. Класс наследуется от [BaseElement](../base/BaseElement.md) и предоставляет удобный интерфейс для создания списков с опциями, управления выбранным значением и генерации соответствующих HTML тегов <option>.

---

## Импорт

```python
from layoutML.elements import Select
```

## Наследование

- Родительский класс: BaseElement
- Тип элемента: select (не самозакрывающийся тег)
- Назначение: Создание выпадающих списков для форм

## Конструктор

### **init**(options=None, selected_value=None, name=None, id=None, object_name=None, style=None, boolean_attributes=[], \*\*kwargs)

Создаёт новый элемент выпадающего списка с указанными параметрами.

### Параметры:

- options (list): Список опций в формате словарей или кортежей. По умолчанию None
- selected_value (str): Значение выбранной по умолчанию опции. По умолчанию None
- name (str): Имя поля для отправки на сервер. По умолчанию None
- id (str): Уникальный идентификатор поля. По умолчанию None
- object_name (опционально): Имя/идентификатор элемента
- style (опционально): CSS строка для inline стилей
- boolean_attributes (опционально): Список булевых атрибутов (required, disabled, multiple)
- \*\*kwargs: Дополнительные HTML атрибуты

### Автоматически устанавливаемые свойства:

- Тег: select
- self_closing: False (не самозакрывающийся тег)
- object_type: "SelectElement"
- options: список опций
- selected_value: выбранное значение
- name: имя поля
- id: идентификатор поля

### Примеры:

```python
# Пустой список
select = Select()

# Список с опциями
select = Select(
    options=[
        {"value": "1", "text": "Опция 1"},
        {"value": "2", "text": "Опция 2"},
        {"value": "3", "text": "Опция 3"}
    ],
    name="choice",
    id="select-choice"
)

# Список с выбранным значением
select = Select(
    options=[
        {"value": "ru", "text": "Русский"},
        {"value": "en", "text": "Английский"},
        {"value": "es", "text": "Испанский"}
    ],
    selected_value="ru",
    name="language",
    required=True
)
```

## Основные методы

### add_option(value, text, selected=False)

Добавляет новую опцию в выпадающий список.

Параметры:

- value (str): Значение опции (отправляется на сервер)
- text (str): Текст опции (отображается пользователю)
- selected (bool): Является ли опция выбранной по умолчанию

```python
select = Select(name="country")
select.add_option("ru", "Россия")
select.add_option("us", "США")
select.add_option("cn", "Китай", selected=True)  # Китай выбран по умолчанию
```

## Примеры использования

### Простой выпадающий список

```python
# Список стран
country_select = Select(
    name="country",
    id="country",
    class_="form-select"
)

countries = [
    ("ru", "Россия"),
    ("us", "США"),
    ("gb", "Великобритания"),
    ("de", "Германия"),
    ("fr", "Франция")
]

for value, text in countries:
    country_select.add_option(value, text)
```

### Список с выбранным значением

```python
# Выбор языка с предустановленным русским
language_select = Select(
    name="language",
    selected_value="ru",
    required=True
)

languages = [
    {"value": "ru", "text": "Русский"},
    {"value": "en", "text": "Английский"},
    {"value": "es", "text": "Испанский"},
    {"value": "de", "text": "Немецкий"},
    {"value": "fr", "text": "Французский"}
]

for lang in languages:
    language_select.add_option(lang["value"], lang["text"])
```
