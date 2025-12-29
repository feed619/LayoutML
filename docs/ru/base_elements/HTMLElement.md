# HTMLElement

`HTMLElement` - базовый класс для создания HTML элементов с поддержкой глобальных атрибутов. Этот класс инкапсулирует стандартные HTML атрибуты, ARIA-атрибуты и обработчики событий, предоставляя удобный интерфейс для создания HTML элементов программным способом.

Класс предназначен для генерации корректной строки атрибутов HTML-тега и может использоваться в шаблонизаторах, HTML-генераторах или собственных UI-фреймворках.

---

## Конструктор
###  __init__(**kwargs)

Инициализирует HTML элемент с переданными атрибутами.

| Параметр        | Тип   | Описание                                   | Пример                                        |
| --------------- | ----- | ------------------------------------------ | --------------------------------------------- |
| id              | str   | Уникальный идентификатор элемента          | "main-container"                              |
| classname       | str   | CSS классы (строка, разделенная пробелами) | "btn btn-primary"                             |
| style           | str   | Встроенные стили CSS                       | "color: red; font-size: 14px;"                |
| title           | str   | Всплывающая подсказка                      | "Нажмите для продолжения"                     |
| data\*\*        | любое | Пользовательские data-атрибуты             | data_id="123" → data-id="123"                 |
| aria\*\*        | любое | ARIA-атрибуты                              | aria_label="Описание" → aria-label="Описание" |
| on\*            | str   | Обработчики событий                        | onclick="submit()"                            |
| hidden          | bool  | Скрыть элемент                             | True/False                                    |
| lang            | str   | Язык контента                              | "ru", "en"                                    |
| dir             | str   | Направление текста                         | "ltr", "rtl", "auto"                          |
| contenteditable | bool  | Разрешить редактирование                   | True/False                                    |
| spellcheck      | bool  | Включить проверку орфографии               | True/False                                    |
| draggable       | bool  | Разрешить перетаскивание                   | True/False                                    |
| accesskey       | str   | Клавиша быстрого доступа                   | "a", "Ctrl+S"                                 |
| tabindex        | int   | Порядок табуляции                          | 0, 1, -1                                      |

## Примеры использования

---

```python
# Простой элемент с основными атрибутами
simple_elem = HTMLElement(
    id="header",
    classname="header sticky",
    title="Основной заголовок"
)

# Элемент с data-атрибутами
data_elem = HTMLElement(
    data_user_id="42",
    data_action="delete",
    data_confirm="true"
)

# Доступный элемент с ARIA
accessible_elem = HTMLElement(
    aria_label="Кнопка закрытия",
    aria_hidden="false",
    role="button"
)

# Элемент с обработчиками событий
interactive_elem = HTMLElement(
    onclick="handleClick(event)",
    onmouseover="showTooltip()",
    onkeydown="handleKeyPress(event)"
)
```

---

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

### remove_class(classname)

Удаляет CSS класс из элемента.

Параметры:

- classname (str): Название CSS класса для удаления

Пример:

```python
element = HTMLElement(classname="container active highlight")
element.remove_class("active")  # Удаляет класс "active"
# Результат: class="container highlight"

```

### add_data(key, value)

Добавляет или обновляет data-\* атрибут.

Параметры:

- key (str): Имя атрибута без префикса 'data-'
- value (str): Значение атрибута

Пример:

```python
element = HTMLElement()
element.add_data("user_id", "12345")  # Добавляет data-user-id="12345"
element.add_data("action", "delete")  # Добавляет data-action="delete"
```

Примечание: В HTML атрибут будет преобразован в data-user-id (с дефисами), но в методе используется нижнее подчеркивание для удобства.

### add_aria(key, value)

Добавляет или обновляет aria-\* атрибут для улучшения доступности.

Параметры:

- key (str): Имя ARIA-атрибута без префикса 'aria-'
- value (str): Значение атрибута

Пример:

```python
element = HTMLElement()
element.add_aria("label", "Закрыть меню")  # Добавляет aria-label="Закрыть меню"
element.add_aria("expanded", "false")      # Добавляет aria-expanded="false"

```

Важно: ARIA-атрибуты критически важны для обеспечения доступности веб-контента для пользователей с ограниченными возможностями.

### add_event(event_name, handler)

Добавляет обработчик события к элементу.

Параметры:

- event_name (str): Имя события с префиксом 'on' (например, 'onclick', 'onmouseover')
- handler (str): JavaScript код для обработки события

Пример:

```python
element = HTMLElement()
element.add_event("onclick", "handleClick(event)")
element.add_event("onmouseover", "showTooltip()")

```

Предупреждение: Для безопасности рекомендуется использовать Event Listeners вместо inline-обработчиков при работе с пользовательскими данными.

### get_attributes_string()

Генерирует строку атрибутов для использования в HTML-теге.

Возвращает:

- str: Строка атрибутов, готовая для вставки в HTML-тег

Пример:

```python
# Создание элемента
element = HTMLElement(
    id="submitBtn",
    classname="btn primary",
    onclick="submitForm()"
)

# Получение строки атрибутов
attributes = element.get_attributes_string()
# Результат: 'id="submitBtn" class="btn primary" onclick="submitForm()"'

# Использование в HTML
html = f'<button {attributes}>Нажми меня</button>'

```

Подробный пример:

```python
complex_element = HTMLElement(
    id="userCard",
    classname="card user-card",
    data_user_id="42",
    aria_role="region",
    aria_label="Карточка пользователя",
    style="width: 300px; padding: 20px;",
    tabindex=0,
    contenteditable=False,
    draggable=True
)

result = complex_element.get_attributes_string()
print(result)
# Вывод: id="userCard" class="card user-card" style="width: 300px; padding: 20px;" data-user_id="42" aria-role="region" aria-label="Карточка пользователя" tabindex="0" draggable="true"
```

---

## Атрибуты класса

| Атрибут           | Тип  | Значение по умолчанию             | Описание                              |
| ----------------- | ---- | --------------------------------- | ------------------------------------- |
| id                | str  | Уникальный идентификатор элемента | "main-container"                      |
| \_id              | str  | None                              | Уникальный идентификатор элемента     |
| \_class           | list | []                                | Список CSS классов                    |
| \_style           | str  | ""                                | Встроенные CSS стили                  |
| \_title           | str  | None                              | Всплывающая подсказка                 |
| \_data_attrs      | dict | {}                                | Пользовательские data-\* атрибуты     |
| \_hidden          | bool | False                             | Скрыт ли элемент                      |
| \_lang            | str  | "en                               | " Язык элемента                       |
| \_dir             | str  | "ltr                              | " Направление текста                  |
| \_contenteditable | bool | False                             | Разрешает редактирование содержимого  |
| \_spellcheck      | bool | False                             | Включает проверку орфографии          |
| \_draggable       | bool | False                             | Определяет возможность перетаскивания |
| \_accesskey       | str  | None                              | Клавиша быстрого доступа              |
| \_tabindex        | int  | None                              | Порядок перехода по Tab               |
| \_aria_attrs      | dict | {}                                | ARIA-атрибуты для доступности         |
| \_events          | dict | {}                                | Обработчики событий                   |

## Практические примеры

### Пример 1: Создание кнопки

```python
# Создание доступной кнопки
button = HTMLElement(
    id="submit-button",
    classname="btn btn-primary btn-lg",
    type="button",
    aria_label="Отправить форму",
    data_action="submit",
    data_form_id="user-form",
    onclick="validateAndSubmit()",
    tabindex=1,
    title="Нажмите для отправки формы"
)

button_html = f'<button {button.get_attributes_string()}>Отправить</button>'
```

### Пример 2: Карточка пользователя

```python
# Создание карточки пользователя
user_card = HTMLElement(
    id=f"user-{user_id}",
    classname="card user-card",
    data_user_id=user_id,
    data_role=user_role,
    aria_label=f"Карточка пользователя {username}",
    aria_labelledby=f"username-{user_id}",
    style="border: 1px solid #ddd; border-radius: 8px;"
)

# Динамическое добавление классов
if user.is_active:
    user_card.add_classname("active")
if user.is_premium:
    user_card.add_classname("premium")

card_html = f'<div {user_card.get_attributes_string()}>...</div>'
```

### Пример 3: Форма с валидацией

```python
# Создание поля ввода с валидацией
input_field = HTMLElement(
    id="email-input",
    classname="form-control",
    type="email",
    name="email",
    required=True,
    aria_required="true",
    aria_invalid="false",
    aria_describedby="email-help",
    onchange="validateEmail(this)",
    onblur="checkEmailAvailability(this)",
    data_validate="email",
    data_async="true",
    placeholder="Введите ваш email"
)

input_html = f'<input {input_field.get_attributes_string()} />'
```

## Особенности работы

### Преобразование имен атрибутов

Класс автоматически преобразует имена атрибутов:

- data_user_id → data-user-id
- aria_labelledby → aria-labelledby
- classname → class

### Булевы атрибуты

Булевы атрибуты выводятся только при значении True:

```
python
elem = HTMLElement(hidden=True, draggable=False, contenteditable=True)
# Результат: hidden contenteditable="true"
```

## Порядок атрибутов

Атрибуты выводятся в следующем порядке:

1. Основные атрибуты (id, class, style)
2. Стандартные HTML атрибуты
3. Data-атрибуты
4. ARIA-атрибуты
5. Обработчики событий

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
