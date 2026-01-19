# HTMLElement

`HTMLElement` - базовый класс для создания HTML элементов в системе LayoutML. Он инкапсулирует все основные атрибуты HTML элементов, включая классы, стили, события и стандартные HTML атрибуты, предоставляя удобный объектно-ориентированный интерфейс для работы с HTML.

Класс предназначен для генерации корректной строки атрибутов HTML-тега и может использоваться в шаблонизаторах, HTML-генераторах или собственных UI-фреймворках.

---

## Импорт

```python
from LayoutML.base_elements.HTMLElement import HTMLElement
from LayoutML.html_core.HTMLAttributes import ValueAttributes
from LayoutML.html_core.HTMLEvents import MouseEvents, KeyboardEvents, FormEvents, etc.
```

## Конструктор

### **init**(boolean_attributes=[], \*\*kwargs)

Инициализирует новый HTML элемент с указанными атрибутами.

Параметры:

| Параметр           | Тип | По умолчанию | Описание                                   | Пример             |
| ------------------ | --- | ------------ | ------------------------------------------ | ------------------ |
| object_name        | str | None         | Уникальный идентификатор элемента          | "container         |
| boolean_attributes | str | []           | Булевые атрибуты                           | "main-container"   |
| inline_styles      | str | []           | Встроенные CSS стили (строка в формате     | "property: value;" |
| \*\*kwargs         | str | -            | CSS классы (строка, разделенная пробелами) | "btn btn-primary"  |

### Особые параметры \*\*kwargs:

    - class_ - CSS классы (строка, разделенная пробелами)
    - Любые другие атрибуты, определенные в классе ValueAttributes из [HTMLAttributes](HTMLAttributes.md)

### Примеры:

```python
# Простой элемент с классами и стилями
element1 = HTMLElement(
    object_name="element1",
    class_="container primary",
    style="color: red; font-size: 14px;",
    id="main",
    title="Основной элемент"
)

# Элемент с булевыми атрибутами
element2 = HTMLElement(
    object_name="element2",
    boolean_attributes=["disabled", "readonly", "required"],
    id="inputField",
    name="username",
    placeholder="Введите имя"
)

# Элемент с произвольными атрибутами
element3 = HTMLElement(
    object_name="element3",
    data_id="123",
    aria_label="Описание",
    custom_attribute="значение"
)
```

## Атрибуты класса

| Атрибут            | Тип       | Описание                                                 |
| ------------------ | --------- | -------------------------------------------------------- |
| object_name        | str       | Уникальный идентификатор элемента                        |
| object_type        | str       | Название типа объекта                                    |
| class\_            | list[str] | Список CSS классов элемента                              |
| inline_styles      | CSSInline | Класс [CSSInline](../css/CSSInline.md)                   |
| events             | dict      | Словарь обработчиков событий (event_name → handler)      |
| aria_attrs         | dict      | Словарь атрибут для улучшения доступности веб-контента   |
| data_attrs         | dict      | Словарь атрибут для хранения пользовательских данных     |
| value_attributes   | dict      | Словарь стандартных HTML атрибутов со значениями         |
| custom_attributes  | dict      | Словарь пользовательских атрибутов (data-, aria-, и др.) |
| boolean_attributes | list[str] | Список булевых HTML атрибутов                            |

---

## Поддерживаемые атрибуты

### Значения из HTMLAttributes.ValueAttributes

Класс поддерживает все атрибуты, определенные в классе [HTMLAttributes](../html_core/HTMLAttributes.md): - Базовые атрибуты: id, name, title, lang, dir, translate - Стили и классы: class, style - Ссылки и пути: href, src, srcset, sizes, poster, action, formaction - Размеры: width, height, size - Формы и ввод: value, placeholder, pattern, min, max, step, maxlength, minlength - Мета-атрибуты: charset, content, http_equiv, property - Таблицы: colspan, rowspan, headers, scope - И многие другие...

Полный список смотрите в документации [HTMLAttributes.py](../html_core/HTMLAttributes.md).

### Булевые атрибуты

Булевые атрибуты передаются через параметр boolean_attributes:

- Видимость: hidden, inert
- Формы: required, disabled, readonly, checked, selected, multiple, autofocus, formnovalidate
- Медиа: controls, autoplay, loop, muted, playsinline
- Другие: contenteditable, draggable, spellcheck, async, defer, open

Полный список смотрите в документации [HTMLAttributes.py](../html_core/HTMLAttributes.md) (класс BooleanAttributes).

### События из HTMLEvents

Метод add_event() поддерживает все события, определенные в файле HTMLEvents.py:

- MouseEvents: onclick, ondblclick, onmousedown, onmouseup, onmousemove, onmouseover, onmouseout, и др.
- KeyboardEvents: onkeydown, onkeyup, onkeypress, oninput, onbeforeinput
- FormEvents: onsubmit, onreset, onchange, onselect, oninvalid, onfocus, onblur
- MediaEvents: onabort, oncanplay, onended, onerror, onloadeddata, onpause, onplay
- И многие другие...

Полный список смотрите в документации [HTMLEvents.py](../html_core/HTMLEvents.md).

## Методы

### add_classname(classname)

Добавляет CSS класс к элементу.

Параметры:

- classname (str): Название CSS класса для добавления

Пример:

```python
element = HTMLElement(classname="container")
element.add_classname("active")      # Добавляет класс "active"
element.add_classname("highlight")   # Добавляет класс "highlight"
# Результат: class="container active highlight"
```

### del_class(classname)

Удаляет CSS класс из элемента.

Параметры:

- classname (str): Название CSS класса для удаления

Пример:

```python
element = HTMLElement(classname="container active highlight")
element.del_class("active")  # Удаляет класс "active"
# Результат: class="container highlight"

```

### add_event(event_name, handler)

Добавляет обработчик события к элементу.

Параметры:

- event_name (str): Имя события с префиксом 'on' (например, 'onclick', 'onmouseover')
- handler (str): JavaScript код для обработки события

Пример:

```python
from LayoutML.html_core.HTMLEvents import MouseEvents, KeyboardEvents

element = HTMLElement()

# Использование констант из HTMLEvents
element.add_event(MouseEvents.onclick, "handleClick(event)")
element.add_event(KeyboardEvents.onkeydown, "handleKeyPress(event)")
element.add_event(FormEvents.onfocus, "highlightField()")

# Или напрямую строкой
element.add_event("onmouseover", "showTooltip()")
element.add_event("onsubmit", "return validateForm()")
```

### del_event(event_name)

Удаляет обработчик события из элемента.

Параметры:

-event_name (str): Имя события для удаления

Пример:

```python
element = HTMLElement()
element.add_event("onclick", "handleClick()")
element.del_event("onclick")
```

### add_aria(key, value)

Добавляет или обновляет ARIA (Accessible Rich Internet Applications) атрибут для улучшения доступности веб-контента.

Параметры:

| Параметр | Тип | Обязательный | Описание                               |
| -------- | --- | ------------ | -------------------------------------- |
| key      | str | Да           | Имя ARIA-атрибута без префикса 'aria-' |
| value    | str | Да           | Значение атрибута                      |

Примеры использования:

```python
# Создание элемента
element = HTMLElement(id="menuButton")

# Добавление базовых ARIA атрибутов
element.add_aria("label", "Главное меню")
element.add_aria("expanded", "false")
element.add_aria("haspopup", "true")
```

Важно: ARIA-атрибуты критически важны для обеспечения доступности веб-контента для пользователей с ограниченными возможностями.

### del_aria(key)

Удаляет ARIA атрибут из элемента.

Параметры:

| Параметр | Тип | Обязательный | Описание                               |
| -------- | --- | ------------ | -------------------------------------- |
| key      | str | Да           | Имя ARIA-атрибута без префикса 'aria-' |

Примеры использования:

```python
# Создание элемента с ARIA атрибутами
element = HTMLElement()
element.add_aria("label", "Старая метка")
element.add_aria("expanded", "true")
element.add_aria("role", "button")

# Удаление атрибутов
element.del_aria("label")  # Удаляет aria-label
element.del_aria("expanded")  # Удаляет aria-expanded
```

### add_data(key, value)

Добавляет или обновляет data-\* атрибут для хранения пользовательских данных.

Параметры:

| Параметр | Тип | Обязательный | Описание                          |
| -------- | --- | ------------ | --------------------------------- |
| key      | str | Да           | Имя атрибута без префикса 'data-' |
| value    | str | Да           | Значение атрибута                 |

Примеры использования:

```python
# Создание элемента
element = HTMLElement(id="userCard")

# Добавление data атрибутов
element.add_data("user_id", "12345")
element.add_data("role", "admin")
element.add_data("registration_date", "2024-01-15")
element.add_data("premium", "true")

```

### del_data(key)

Удаляет data-\* атрибут из элемента.

Параметры:

| Параметр | Тип | Обязательный | Описание                          |
| -------- | --- | ------------ | --------------------------------- |
| key      | str | Да           | Имя атрибута без префикса 'data-' |

Примеры использования:

```python
# Создание элемента с data атрибутами
element = HTMLElement()
element.add_data("user_id", "12345")
element.add_data("role", "admin")
element.add_data("status", "active")
element.add_data("temporary", "true")

# Удаление атрибутов
element.del_data("temporary")  # Удаляет data-temporary
element.del_data("status")  # Удаляет data-status

```

### add_attributes(boolean_attributes=[], \*\*kwargs)

Добавляет несколько атрибутов одновременно.

```python
element.add_attributes(
    boolean_attributes=["required"],
    id="email",
    name="email",
    placeholder="Введите email"
)
```

### del_attributes(\*args)

Удаляет несколько атрибутов.

```python
element.del_attributes("id", "name", "required")
```

### get_attributes_string()

Генерирует строку атрибутов для использования в HTML-теге.

Возвращает:

- str: Строка атрибутов, готовая для вставки в HTML-тег

Формат вывода:

```
class="class1 class2" style="property:value; property2:value2;"
onclick="handler()" disabled readonly id="elementId" name="fieldName"
```

## Примеры использования

### Пример 1: Базовый элемент с атрибутами

```python
# Создание элемента с различными типами атрибутов
element = HTMLElement(
    boolean_attributes=["required", "autofocus"],
    class_="form-control input-lg",
    style="border: 2px solid #007bff; border-radius: 5px;",
    id="usernameInput",
    name="username",
    placeholder="Введите имя пользователя",
    maxlength="50",
    minlength="3",
    data_validation="alphanumeric",
    aria_label="Поле для ввода имени пользователя",
    aria_required="true"
)

# Добавление событий
from LayoutML.html_core.HTMLEvents import MouseEvents, KeyboardEvents, FormEvents

element.add_event(MouseEvents.onclick, "handleInputClick()")
element.add_event(KeyboardEvents.onkeyup, "validateUsername(event)")
element.add_event(FormEvents.onfocus, "highlightField(this)")
element.add_event(FormEvents.onblur, "validateField(this)")

# Генерация HTML
html_attrs = element.get_attributes_string()
print(f'<input {html_attrs} />')
```

### Пример 2: Интерактивная кнопка

```python
from LayoutML.html_core.HTMLEvents import MouseEvents, KeyboardEvents

# Создание доступной кнопки
button = HTMLElement(
    boolean_attributes=["disabled"],
    class_="btn btn-primary",
    id="submitButton",
    type="button",
    role="button",
    tabindex="0",
    aria_label="Отправить форму",
    aria_disabled="true",
    data_action="submit",
    data_form_id="userForm"
)

# Добавление событий для мыши и клавиатуры
button.add_event(MouseEvents.onclick, "submitForm()")
button.add_event(MouseEvents.onmouseover, "showTooltip('Нажмите для отправки')")
button.add_event(MouseEvents.onmouseout, "hideTooltip()")
button.add_event(KeyboardEvents.onkeydown, "if(event.key === 'Enter' || event.key === ' ') submitForm()")

# Включение кнопки при определенных условиях
button.boolean_attributes.remove("disabled")
button.value_attributes["aria_disabled"] = "false"

# Генерация HTML
button_attrs = button.get_attributes_string()
print(f'<button {button_attrs}>Отправить</button>')
```

## Порядок атрибутов

Атрибуты выводятся в следующем порядке:

1. CSS классы
2. Встроенные стили
3. Обработчики событий
4. Булевые атрибуты
5. Data атрибуты
6. Aria атрибуты
7. Стандартные HTML атрибуты со значениями

## Безопасность

- Избегайте использования inline JavaScript с пользовательскими данными
- Используйте add_event для безопасного добавления обработчиков
- Валидируйте все пользовательские данные перед добавлением в атрибуты

## Производительность

- Для часто изменяемых элементов кэшируйте строку атрибутов
- Используйте add_classname/remove_class вместо полной перестройки классов
- Для статических элементов создавайте атрибуты один раз в конструкторе

## Доступность

- Всегда добавляйте ARIA-атрибуты для интерактивных элементов
- Используйте tabindex для управления фокусом
- Добавляйте aria-label для элементов без видимого текст

## Ограничения

- Нет поддержки вложенных элементов - класс управляет только атрибутами
- Нет валидации значений - ответственность за корректность данных лежит на разработчике
- Inline стили - для сложных стилей рекомендуется использовать CSS классы
- Inline JavaScript - для сложной логики рекомендуется использовать внешние обработчики

## Совместимость

Класс генерирует стандартные HTML5 атрибуты, совместимые со всеми современными браузерами. Все сгенерированные атрибуты соответствуют спецификации W3C HTML5.
