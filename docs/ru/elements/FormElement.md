# FormElement

`FormElement` - является специализированным наследником базового класса HTMLElement, предназначенным для создания элементов HTML форм с поддержкой всех типов полей ввода, определенных в стандарте HTML5. Этот класс предоставляет удобный объектно-ориентированный интерфейс для работы с элементами форм, автоматически обрабатывая специфические атрибуты и особенности каждого типа.

---

## Импорт

```python
from LayoutML.elements import FormElement
# FormElement наследует от HTMLElement, поэтому доступны все его возможности
```

## Конструктор

### **init**(form_type: str = "text", boolean_attributes=[], \*\*kwargs)

Инициализирует новый элемент формы с указанными параметрами.

Параметры:

| Константа          | Тип       | По умолчанию | Описание                          | Пример                               |
| ------------------ | --------- | ------------ | --------------------------------- | ------------------------------------ |
| form_type          | str       | "text"       | Тип элемента формы                | "email", "password", "date"          |
| boolean_attributes | list[str] | []           | Список булевых HTML атрибутов     | ["required", "disabled", "readonly"] |
| object_name        | str       | None         | Уникальный идентификатор элемента | "form_element"                       |
| \*\*kwargs         | dict      | -            | Дополнительные атрибуты элемента  | id\_="email", name="user_email"      |

### Особенности конструктора:

- Автоматически устанавливает HTML тег как "input"
- Добавляет атрибут type с указанным значением form_type.Все возможные значения находятся в классе [FormTypes](../types/FormTypes.md)
- Наследует все возможности родительского класса HTMLElement (классы, стили, события, ARIA, data-атрибуты)

## Атрибуты класса

| Константа | Тип | По умолчанию                                                   |
| --------- | --- | -------------------------------------------------------------- |
| tag       | str | HTML тег элемента "input"                                      |
| form_type | str | Тип элемента формы (определяет поведение и внешний вид) "text" |

### Примечание: Класс также наследует все атрибуты от HTMLElement:

- class\_ - список CSS классов
- styles - словарь CSS стилей
- events - словарь обработчиков событий
- value_attributes - словарь стандартных HTML атрибутов
- custom_attributes - словарь пользовательских атрибутов
- boolean_attributes - список булевых атрибутов

## Методы

### get_attributes_string()

Генерирует полную строку атрибутов для HTML-тега, объединяя специфические атрибуты формы с наследуемыми от родительского класса.

Возвращает:

- str: Строка атрибутов, готовая для вставки в HTML-тег

Формат вывода:

```text
type="email" class="form-control" id_="emailInput" name="email" required placeholder="Введите email" aria-label="Электронная почта" data-validation="email"
```

### render()

Создает полный HTML код элемента формы, включая открывающий и закрывающий теги.
Возвращает:

- str: Полный HTML тег элемента с атрибутами

## Примеры инициализации:

```python
# Простое текстовое поле
text_field = FormElement(
    form_type="text",
    id_="username",
    name="username",
    placeholder="Введите имя"
)

# Поле email с валидацией
email_field = FormElement(
    form_type="email",
    id_="user_email",
    name="email",
    required=True,
    pattern="[a-z0-9._%+-]+@[a-z0-9.-]+\\.[a-z]{2,}$"
)

# Поле пароля с дополнительными атрибутами
password_field = FormElement(
    form_type="password",
    boolean_attributes=["required"],
    id_="user_password",
    name="password",
    minlength="8",
    autocomplete="new-password",
    aria_label="Пароль пользователя"
)

# Чекбокс с предварительным выбором
newsletter_checkbox = FormElement(
    form_type="checkbox",
    boolean_attributes=["checked"],
    id_="subscribe",
    name="newsletter",
    value="yes"
)

# Поле даты с ограничениями
birthday_field = FormElement(
    form_type="date",
    id_="birth_date",
    name="birthday",
    min="1900-01-01",
    max="2024-12-31",
    required=True
)

# Создание и рендеринг элементов
text_field = FormElement(
    form_type="text",
    id_="name",
    name="full_name",
    placeholder="Иван Иванов"
)

email_field = FormElement(
    form_type="email",
    id_="email",
    name="email",
    required=True
)

submit_button = FormElement(
    form_type="submit",
    value="Отправить",
    class_="btn btn-primary"
)

# Рендеринг
print(text_field.render())   # <input type="text" id_="name" name="full_name" placeholder="Иван Иванов">
print(email_field.render())  # <input type="email" id_="email" name="email" required>
print(submit_button.render()) # <input type="submit" value="Отправить" class="btn btn-primary">
```
