# Класс FormElement

## Обзор

`FormElement` - это специализированный класс для создания элементов HTML форм, наследующий от базового класса `HTMLElement`. Класс предоставляет удобный интерфейс для работы со всеми стандартными атрибутами элементов ввода HTML5.

**Наследование:** `FormElement` → `HTMLElement`

## Быстрый старт

```python
# Создание текстового поля
text_field = FormElement(
    type="text",
    name="username",
    placeholder="Введите имя пользователя",
    required=True,
    maxlength=50
)

# Создание поля email
email_field = FormElement(
    type="email",
    name="email",
    required=True,
    pattern="[a-z0-9._%+-]+@[a-z0-9.-]+\\.[a-z]{2,}$"
)

# Использование в HTML
input_html = f'<input type="text" {text_field.get_attributes_string()} />'
```

## Конструктор

### **init**(\*\*kwargs)

Создает новый элемент формы с указанными атрибутами.

#### Параметры формы

| Параметр     | Тип  | По умолчанию | Описание              |
| ------------ | ---- | ------------ | --------------------- |
| type         | str  | 'text'       | Тип элемента формы    |
| name         | str  | None         | Имя элемента          |
| value        | any  | None         | Значение по умолчанию |
| placeholder  | str  | None         | Подсказка в поле      |
| required     | bool | False        | Обязательное поле     |
| readonly     | bool | False        | Только чтение         |
| disabled     | bool | False        | Отключенное поле      |
| maxlength    | int  | None         | Макс. длина текста    |
| minlength    | int  | None         | Мин. длина текста     |
| max          | any  | None         | Максимальное значение |
| min          | any  | None         | Минимальное значение  |
| step         | any  | None         | Шаг изменения         |
| pattern      | str  | None         | Регулярное выражение  |
| autofocus    | bool | False        | Автофокус             |
| multiple     | bool | False        | Множественный выбор   |
| checked      | bool | False        | Выбрано               |
| autocomplete | str  | 'on'         | Автозаполнение        |

#### Дополнительные параметры

| Параметр       | Тип  | По умолчанию | Описание                    |
| -------------- | ---- | ------------ | --------------------------- |
| size           | int  | None         | Видимая ширина поля         |
| accept         | str  | None         | Типы файлов                 |
| capture        | str  | None         | Способ захвата медиа        |
| dirname        | str  | None         | Поле для направления текста |
| form           | str  | None         | ID связанной формы          |
| formaction     | str  | None         | URL отправки                |
| formenctype    | str  | None         | Кодирование данных          |
| formmethod     | str  | None         | HTTP метод                  |
| formnovalidate | bool | False        | Отключить валидацию         |
| formtarget     | str  | None         | Целевое окно                |
| height         | int  | None         | Высота изображения          |
| width          | int  | None         | Ширина изображения          |
| list           | str  | None         | ID datalist                 |
| alt            | str  | None         | Альтернативный текст        |
| src            | str  | None         | URL изображения             |
| rows           | int  | None         | Количество строк            |
| cols           | int  | None         | Количество колонок          |
| wrap           | str  | 'soft'       | Перенос текста              |
| options        | list | []           | Список опций                |
| selected       | any  | None         | Выбранное значение          |
| text           | str  | ''           | Текст в textarea            |

## Примеры создания элементов

```python
# Поле пароля
password_field = FormElement(
    type="password",
    name="password",
    placeholder="Введите пароль",
    required=True,
    minlength=8,
    autocomplete="off"
)

# Числовое поле
number_field = FormElement(
    type="number",
    name="age",
    min=18,
    max=99,
    step=1,
    value=25
)

# Флажок
checkbox = FormElement(
    type="checkbox",
    name="subscribe",
    value="yes",
    checked=True
)

# Поле даты
date_field = FormElement(
    type="date",
    name="birthday",
    min="1900-01-01",
    max="2024-12-31"
)
```

## Методы

### get_form_attributes()

Возвращает список строковых представлений специфических атрибутов формы.

Возвращает:

- list[str]: Список HTML-атрибутов формы

Пример:

```python
field = FormElement(
    name="email",
    type="email",
    required=True,
    placeholder="user@example.com"
)

attrs = field.get_form_attributes()
# Результат: ['name="email"', 'type="email"', 'required', 'placeholder="user@example.com"']
```

### Примечание:

Этот метод возвращает только атрибуты, специфичные для форм. Для получения всех атрибутов (включая унаследованные от HTMLElement) используйте метод get_attributes_string() родительского класса.

## Наследуемые методы

Класс FormElement наследует все методы от HTMLElement:

- add_classname(classname) - добавляет CSS класс
- remove_class(classname) - удаляет CSS класс
- add_data(key, value) - добавляет data-атрибут
- add_aria(key, value) - добавляет aria-атрибут
- add_event(event_name, handler) - добавляет обработчик события
- get_attributes_string() - возвращает все атрибуты элемента

## Атрибуты класса

Специфичные атрибуты формы

| Атрибут          | Тип           | Значение по умолчанию | Описание                         |
| ---------------- | ------------- | --------------------- | -------------------------------- |
| \_type           | str           | 'text'                | Тип элемента формы               |
| \_name           | str, optional | None                  | Имя элемента формы               |
| \_value          | any, optional | None                  | Значение элемента                |
| \_placeholder    | str, optional | None                  | Текст-подсказка в поле           |
| \_required       | bool          | False                 | Обязательное поле                |
| \_readonly       | bool          | False                 | Только для чтения                |
| \_disabled       | bool          | False                 | Отключенный элемент              |
| \_maxlength      | int, optional | None                  | Максимальная длина текста        |
| \_minlength      | int, optional | None                  | Минимальная длина текста         |
| \_max            | any, optional | None                  | Максимальное значение            |
| \_min            | any, optional | None                  | Минимальное значение             |
| \_step           | any, optional | None                  | Шаг изменения значения           |
| \_pattern        | str, optional | None                  | Регулярное выражение             |
| \_autofocus      | bool          | False                 | Автофокус при загрузке           |
| \_multiple       | bool          | False                 | Множественный выбор              |
| \_checked        | bool          | False                 | Выбранный элемент                |
| \_autocomplete   | str           | 'on'                  | Автозаполнение                   |
| \_size           | int, optional | None                  | Видимая ширина поля              |
| \_accept         | str, optional | None                  | Типы файлов для загрузки         |
| \_capture        | str, optional | None                  | Способ захвата медиа             |
| \_dirname        | str, optional | None                  | Поле направления текста          |
| \_form           | str, optional | None                  | ID связанной формы               |
| \_formaction     | str, optional | None                  | URL для отправки                 |
| \_formenctype    | str, optional | None                  | Способ кодирования данных        |
| \_formmethod     | str, optional | None                  | HTTP метод отправки              |
| \_formnovalidate | bool          | False                 | Отключение валидации             |
| \_formtarget     | str, optional | None                  | Целевое окно для результата      |
| \_height         | int, optional | None                  | Высота изображения               |
| \_width          | int, optional | None                  | Ширина изображения               |
| \_list           | str, optional | None                  | ID datalist для автозаполнения   |
| \_alt            | str, optional | None                  | Альтернативный текст             |
| \_src            | str, optional | None                  | URL источника изображения        |
| \_rows           | int, optional | None                  | Количество строк textarea        |
| \_cols           | int, optional | None                  | Количество колонок textarea      |
| \_wrap           | str           | 'soft'                | Перенос текста в textarea        |
| \_options        | list          | []                    | Список опций для select/datalist |
| \_selected       | any, optional | None                  | Выбранное значение               |
| \_text           | str           | ''                    | Текст внутри textarea            |

## Унаследованные атрибуты (от HTMLElement)

Все стандартные HTML атрибуты: \_id, \_class, \_style, \_title, \_data_attrs, \_aria_attrs, \_events, и другие.

## Практические примеры

### Пример 1: Форма регистрации

```python
# Поля формы регистрации
username_field = FormElement(
    type="text",
    name="username",
    placeholder="Имя пользователя",
    required=True,
    minlength=3,
    maxlength=30,
    pattern="[A-Za-z0-9_]+"
)

email_field = FormElement(
    type="email",
    name="email",
    placeholder="Электронная почта",
    required=True
)

password_field = FormElement(
    type="password",
    name="password",
    placeholder="Пароль",
    required=True,
    minlength=8,
    autocomplete="new-password"
)

# Генерация HTML
username_html = f'<input {username_field.get_attributes_string()} />'
email_html = f'<input {email_field.get_attributes_string()} />'
password_html = f'<input {password_field.get_attributes_string()} />'
```

### Пример 2: Форма поиска с фильтрами

```python
# Поле поиска
search_field = FormElement(
    type="search",
    name="query",
    placeholder="Поиск...",
    autocomplete="off",
    aria_label="Поиск по сайту"
)

# Выпадающий список
category_field = FormElement(
    name="category",
    required=True,
    value="all"
)

# Диапазон цен
price_min = FormElement(
    type="number",
    name="price_min",
    placeholder="От",
    min=0,
    step=100
)

price_max = FormElement(
    type="number",
    name="price_max",
    placeholder="До",
    min=0,
    step=100
)
```

### Пример 3: Интерактивная форма с событиями

```python
# Поле с динамической валидацией
dynamic_field = FormElement(
    type="text",
    name="dynamic",
    id="dynamic-field",
    classname="form-control",
    placeholder="Введите текст",
    required=True,
    data_validate="dynamic",
    oninput="validateField(this)",
    onblur="showValidationMessage(this)",
    aria_describedby="field-help"
)

# Добавление дополнительных атрибутов
dynamic_field.add_data("async", "true")
dynamic_field.add_aria("live", "polite")
dynamic_field.add_event("onfocus", "highlightField(this)")
```

## Поддерживаемые типы элементов для атрибута 'type'

Типы можно указывать через FormType, класс можно вызвать по пути:

```python
from LayoutML.types import FormTypes
```

### Текстовые поля:

- text: Обычное текстовое поле
- password: Поле для пароля
- email: Поле для email адреса
- number: Числовое поле
- tel: Поле для телефона
- url: Поле для URL
- search: Поле поиска

```
class TextField(str, Enum):
    TEXT = "text"
    PASSWORD = "password"
    EMAIL = "email"
    NUMBER = "number"
    TEL = "tel"
    URL = "url"
    SEARCH = "search"
```

#### Примеры использования:

### 1. text - Текстовое поле

```python
from LayoutML.types.FormTypes import TextField
# Простое текстовое поле для ввода любого текста
username_field = FormElement(
    type=TextField.TEXT, # или можно указать как "text"
    name="username",
    placeholder="Введите ваше имя",
    maxlength=50
)
# HTML: <input type="text" name="username" placeholder="Введите ваше имя" maxlength="50">
```

Использование: логины, имена, названия, любые текстовые данные

### 2. password - Поле пароля

```python
from LayoutML.types.FormTypes import TextField
# Поле пароля (символы скрываются точками)
password_field = FormElement(
    type=TextField.PASSWORD, # или можно указать как "password"
    name="password",
    placeholder="Пароль",
    minlength=8,
    autocomplete="new-password"
)
# HTML: <input type="password" name="password" placeholder="Пароль" minlength="8" autocomplete="new-password">
```

Использование: пароли, секретные данные

### 3. email - Электронная почта

```python
from LayoutML.types.FormTypes import TextField
# Поле для email с автоматической проверкой формата
email_field = FormElement(
    type=TextField.EMAIL, # или можно указать как "email"
    name="email",
    placeholder="user@example.com",
    required=True,
    pattern="[a-z0-9._%+-]+@[a-z0-9.-]+\\.[a-z]{2,}$"
)
# HTML: <input type="email" name="email" placeholder="user@example.com" required pattern="[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$">
```

Использование: email адреса, на мобильных устройствах показывает специальную клавиатуру с @

### 4. number - Числовое поле

```python
from LayoutML.types.FormTypes import TextField
# Поле для чисел с ограничениями
age_field = FormElement(
    type=TextField.NUMBER, # или можно указать как "number",
    name="age",
    placeholder="Ваш возраст",
    min=18,
    max=99,
    step=1,
    value=25
)
# HTML: <input type="number" name="age" placeholder="Ваш возраст" min="18" max="99" step="1" value="25">
```

Использование: возраст, количество, цена, любые числовые значения

### 5. tel - Телефон

```python
from LayoutML.types.FormTypes import TextField
# Поле для номера телефона
phone_field = FormElement(
    type=TextField.TEL, # или можно указать как "tel"
    name="phone",
    placeholder="+7 (999) 999-99-99",
    pattern="\\+7\\s?\\(?\\d{3}\\)?\\s?\\d{3}-?\\d{2}-?\\d{2}"
)
# HTML: <input type="tel" name="phone" placeholder="+7 (999) 999-99-99" pattern="\+7\s?\(?\d{3}\)?\s?\d{3}-?\d{2}-?\d{2}">
```

Использование: номера телефонов, на мобильных показывает цифровую клавиатуру

### 6. url - URL адрес

```python
from LayoutML.types.FormTypes import TextField
# Поле для веб-адресов
website_field = FormElement(
    type=TextField.URL, # или можно указать как "url"
    name="website",
    placeholder="https://example.com",
    pattern="https?://.+"
)
# HTML: <input type="url" name="website" placeholder="https://example.com" pattern="https?://.+">
```

Использование: ссылки на сайты, автоматически проверяет формат URL

### 7. search - Поиск

```python
from LayoutML.types.FormTypes import TextField
# Поле для поисковых запросов
search_field = FormElement(
    type=TextField.SEARCH, # или можно указать как "search"
    name="query",
    placeholder="Поиск по сайту...",
    autocomplete="off"
)
# HTML: <input type="search" name="query" placeholder="Поиск по сайту..." autocomplete="off">
```

Использование: поисковые поля, часто имеет специальное оформление в браузере

---

### Элементы выбора:

- checkbox: Флажок
- radio: Радиокнопка
- select: Выпадающий список (требует options)
- datalist: Список подсказок

```
class SelectionElements(str, Enum):
    CHECKBOX = "checkbox"
    RADIO = "radio"
    SELECT = "select"
    DATALIST = "datalist"
```

#### Примеры использования:

### 1. checkbox - Флажок

```python
from LayoutML.types.FormTypes import SelectionElements
# Чекбокс (можно выбрать несколько)
agree_terms = FormElement(
    type=SelectionElements.CHECKBOX, # или можно указать как "checkbox"
    name="agree_terms",
    value="yes",
    checked=True  # По умолчанию отмечен
)
# HTML: <input type="checkbox" name="agree_terms" value="yes" checked>
newsletter = FormElement(
    type=SelectionElements.CHECKBOX, # или можно указать как "checkbox"
    name="subscribe",
    value="newsletter"
)
# HTML: <input type="checkbox" name="subscribe" value="newsletter">
```

Использование: множественный выбор, согласия, опции

### 2. radio - Переключатель

```python
from LayoutML.types.FormTypes import SelectionElements
# Радиокнопки (только один выбор из группы)
gender_male = FormElement(
    type=SelectionElements.RADIO, # или можно указать как "radio"
    name="gender",  # Одинаковое name для группы!
    value="male",
    id="male"
)
# HTML: <input type="radio" name="gender" value="male" id="male">

gender_female = FormElement(
    type=SelectionElements.RADIO, # или можно указать как "radio"
    name="gender",  # Такое же name!
    value="female",
    id="female",
    checked=True
)
# HTML: <input type="radio" name="gender" value="female" id="female" checked>
```

Использование: выбор одного варианта из нескольких

### 3. select - Выпадающий список

```python
from LayoutML.types.FormTypes import SelectionElements

# Пример 1: Простой выпадающий список стран
country_select = FormElement(
    type=SelectionElements.SELECT, # или можно указать как "select"
    name="country",
    options=[
        ("", "-- Выберите страну --"),  # Пустая опция
        ("ru", "Россия"),
        ("us", "Соединенные Штаты"),
        ("de", "Германия"),
        ("fr", "Франция"),
        ("jp", "Япония"),
        ("cn", "Китай")
    ],
    selected="ru",  # Выбранное значение по умолчанию
    required=True,
    classname="form-select",
    id="countrySelect",
    aria_label="Выбор страны"
)

# HTML: <select name="country" required class="form-select" id="countrySelect"
        # aria-label="Выбор страны">
    # <option value="">-- Выберите страну --</option>
    # <option value="ru" selected>Россия</option>
    # <option value="us">Соединенные Штаты</option>
    # <option value="de">Германия</option>
    # <option value="fr">Франция</option>
    # <option value="jp">Япония</option>
    # <option value="cn">Китай</option>
# </select>
```

### 4. datalist - Список подсказок для автозаполнения

```python
from LayoutML.types.FormTypes import SelectionElements,TextField
browsers_datalist = FormElement(
    type=SelectionElements.DATALIST, # или можно указать как "datalist"
    id="browser-options",  # ОБЯЗАТЕЛЬНО нужен ID для связи с input
    options=[
        ("Chrome", "Google Chrome"),
        ("Firefox", "Mozilla Firefox"),
        ("Safari", "Apple Safari"),
        ("Edge", "Microsoft Edge"),
        ("Opera", "Opera Browser"),
        ("Brave", "Brave Browser")
    ]
)

# Текстовое поле, связанное с datalist
browser_input = FormElement(
    type=TextField.TEXT, # или можно указать как "text"
    name="browser",
    placeholder="Введите название браузера",
    list="browser-options",  # Связь с datalist по ID
    autocomplete="off",
    classname="form-control",
    aria_label="Выбор веб-браузера"
)

# HTML:
# <datalist id="browser-options">
#     <option value="Chrome" label="Google Chrome"></option>
#     <option value="Firefox" label="Mozilla Firefox"></option>
#     <option value="Safari" label="Apple Safari"></option>
#     <option value="Edge" label="Microsoft Edge"></option>
#     <option value="Opera" label="Opera Browser"></option>
#     <option value="Brave" label="Brave Browser"></option>
# </datalist>

# <input type="text" name="browser" placeholder="Введите название браузера"
#        list="browser-options" autocomplete="off" class="form-control"
#        aria-label="Выбор веб-браузера">
```

---

### Специальные поля:

- date: Выбор даты
- time: Выбор времени
- datetime-local: Дата и время
- month: Месяц и год
- week: Неделя года
- color: Выбор цвета
- range: Ползунок
- file: Загрузка файлов
  - hidden: Скрытое поле
  - textarea: Многострочный текст

```
class SpecialFields(str, Enum):
    DATE = "date"
    TIME = "time"
    DATETIME_LOCAL = "datetime-local"
    MONTH = "month"
    WEEK = "week"
    COLOR = "color"
    RANGE = "range"
    FILE = "file"
    HIDDEN = "hidden"
    TEXTAREA = "textarea"
```

#### Примеры использования:

### 1. date - Дата

```python
from LayoutML.types.FormTypes import SpecialFields
# Поле для выбора даты
birthday_field = FormElement(
    type=SpecialFields.DATE, # или можно указать как "date"
    name="birthday",
    min="1900-01-01",
    max="2024-12-31",
    value="1990-01-01"
)
# HTML: <input type="date" name="birthday" min="1900-01-01" max="2024-12-31" value="1990-01-01">
```

Использование: даты рождения, события, сроки

### 2. time - Время

```python
from LayoutML.types.FormTypes import SpecialFields
# Поле для выбора времени
meeting_time = FormElement(
    type=SpecialFields.TIME, # или можно указать как "time"
    name="meeting_time",
    min="09:00",
    max="18:00",
    step="1800"  # 30 минут шаг
)
# HTML: <input type="time" name="meeting_time" min="09:00" max="18:00" step="1800">
```

Использование: время встреч, расписание

### 3. datetime-local - Дата и время

```python
from LayoutML.types.FormTypes import SpecialFields
# Поле для выбора даты и времени одновременно
event_datetime = FormElement(
    type=SpecialFields.DATETIME_LOCAL, # или можно указать как "datetime-local"
    name="event_start",
    min="2024-01-01T00:00",
    max="2024-12-31T23:59"
)
# HTML: <input type="datetime-local" name="event_start" min="2024-01-01T00:00" max="2024-12-31T23:59">
```

Использование: начало событий, сроки с точным временем

### 4. month - Месяц

```python
from LayoutML.types.FormTypes import SpecialFields
# Поле для выбора месяца и года
credit_card_month = FormElement(
    type=SpecialFields.MONTH, # или можно указать как "month"
    name="expiry_date",
    min="2024-01",
    max="2030-12"
)
# HTML: <input type="month" name="expiry_date" min="2024-01" max="2030-12">
```

Использование: срок действия карт, месячные отчеты

### 5. week - Неделя

```python
from LayoutML.types.FormTypes import SpecialFields
# Поле для выбора недели года
vacation_week = FormElement(
    type=SpecialFields.WEEK, # или можно указать как "week"
    name="vacation",
    min="2024-W01",
    max="2024-W52"
)
# HTML: <input type="week" name="vacation" min="2024-W01" max="2024-W52">
```

Использование: планирование по неделям, отпуска

### 6. color - Цвет

```python
from LayoutML.types.FormTypes import SpecialFields
# Поле для выбора цвета
favorite_color = FormElement(
    type=SpecialFields.COLOR, # или можно указать как "color"
    name="color",
    value="#ff0000"  # Красный по умолчанию
)
# HTML: <input type="color" name="color" value="#ff0000">
```

Использование: выбор цвета для тем, оформления

### 7. range - Ползунок

```python
from LayoutML.types.FormTypes import SpecialFields
# Ползунок для выбора значения в диапазоне
volume_slider = FormElement(
    type=SpecialFields.RANGE, # или можно указать как "range"
    name="volume",
    min="0",
    max="100",
    step="10",
    value="50"
)
# HTML: <input type="range" name="volume" min="0" max="100" step="10" value="50">

price_range = FormElement(
    type=SpecialFields.RANGE, # или можно указать как "range"
    name="price",
    min="0",
    max="10000",
    step="100",
    value="5000"
)
# HTML: <input type="range" name="price" min="0" max="10000" step="100" value="50000">
```

Использование: регулировка громкости, цены, любых числовых значений визуально

### 8. file - Файл

```python
from LayoutML.types.FormTypes import SpecialFields
# Поле для загрузки файлов
avatar_upload = FormElement(
    type=SpecialFields.FILE, # или можно указать как "file"
    name="avatar",
    accept="image/*"  # Только изображения
)
# HTML: <input type="file" name="avatar" accept="image/*">
document_upload = FormElement(
    type=SpecialFields.FILE, # или можно указать как "file"
    name="documents",
    multiple=True,  # Можно выбрать несколько файлов
    accept=".pdf,.doc,.docx"
)
# HTML: <input type="file" name="documents" multiple accept=".pdf,.doc,.docx">
```

### 9. hidden - Скрытое поле

```python
from LayoutML.types.FormTypes import SpecialFields
# Скрытое поле (не видно пользователю)
csrf_token = FormElement(
    type=SpecialFields.HIDDEN, # или можно указать как "hidden"
    name="csrf_token",
    value="abc123def456"
)
# HTML: <input type="hidden" name="csrf_token" value="abc123def456">

user_id_field = FormElement(
    type=SpecialFields.HIDDEN, # или можно указать как "hidden"
    name="user_id",
    value="42"
)
# HTML: <input type="hidden" name="user_id" value="42">

```

Использование: передача служебных данных, токенов безопасности

### 9. textarea - Многострочное текстовое поле

```python
from LayoutML.types.FormTypes import SpecialFields

# Пример 1: Простой textarea для комментариев
comment_field = FormElement(
    type=SpecialFields.TEXTAREA, # или можно указать как "textarea"
    name="comment",
    rows="5",           # Высота в строках
    cols="40",          # Ширина в символах
    placeholder="Оставьте ваш комментарий здесь...",
    maxlength="1000",   # Максимальная длина текста
    wrap="hard",        # Перенос строк: soft/hard
    required=True,
    classname="form-control comment-box",
    id="userComment"
)

# HTML: <textarea name="comment" rows="5" cols="40" maxlength="1000" wrap="hard" placeholder="Оставьте ваш комментарий здесь..." required class="form-control comment-box" id="userComment"> </textarea>
```

## Использование: загрузка файлов, фотографий, документов

### Кнопки:

- submit: Кнопка отправки
- reset: Кнопка сброса
- button: Обычная кнопка
- image: Кнопка с изображением

```
class Buttons(str, Enum):
    SUBMIT = "submit"
    RESET = "reset"
    BUTTON = "button"
    IMAGE = "image"
```

#### Примеры использования:

### 1. submit - Кнопка отправки

```python
from LayoutML.types.FormTypes import Buttons
# Кнопка для отправки формы
submit_button = FormElement(
    type=Others.SUBMIT, # или можно указать как "submit",
    value="Отправить",  # Текст на кнопке
    classname="btn btn-primary"
)
# HTML: <input type="submit" value="Отправить" class="btn btn-primary">
```

Использование: основная кнопка отправки формы

### 2. reset - Кнопка сброса

```python
from LayoutML.types.FormTypes import Buttons
# Кнопка для сброса формы к исходным значениям
reset_button = FormElement(
    type=Others.RESET, # или можно указать как "reset"
    value="Очистить форму",
    classname="btn btn-secondary"
)
# HTML: <input type="reset" value="Очистить форму" class="btn btn-secondary">
```

Использование: сброс всех полей формы

### 3. button - Обычная кнопка

```python
from LayoutML.types.FormTypes import Buttons
# Простая кнопка (не отправляет форму)
custom_button = FormElement(
    type=Others.BUTTON, # или можно указать как "button"
    value="Показать больше",
    onclick="loadMoreItems()",
    classname="btn"
)
# HTML: <input type="button" value="Показать больше" onclick="loadMoreItems()" class="btn">
```

Использование: любые действия, не связанные с отправкой формы

### 4. image - Кнопка с изображением

````python
from LayoutML.types.FormTypes import Buttons

submit_image = FormElement(
    type=Others.IMAGE, # или можно указать как "image"
    src="/images/submit-button.png",  # ОБЯЗАТЕЛЬНЫЙ параметр!
    alt="Отправить форму",            # Альтернативный текст
    width="120",                      # Ширина изображения
    height="40",                      # Высота изображения
    name="submit_btn",
    value="submit",                   # Значение, отправляемое на сервер
    classname="image-button",
    title="Нажмите для отправки формы",
    onclick="validateBeforeSubmit()",
    aria_label="Кнопка отправки формы"
)
# HTML: <input type="image" src="/images/submit-button.png" alt="Отправить форму" width="120" height="40" name="submit_btn" value="submit" class="image-button" title="Нажмите для отправки формы" onclick="validateBeforeSubmit()" aria-label="Кнопка отправки формы">
"""
---

#### Примеры использования:

---

## Валидация данных

### Встроенная валидация HTML5

```python
# Email с проверкой формата
email_validated = FormElement(
    type="email",
    name="email",
    required=True,
    pattern="[a-z0-9._%+-]+@[a-z0-9.-]+\\.[a-z]{2,}$"
)

# Номер телефона
phone_field = FormElement(
    type="tel",
    name="phone",
    pattern="\\+7\\s?\\(?\\d{3}\\)?\\s?\\d{3}-?\\d{2}-?\\d{2}",
    placeholder="+7 (999) 999-99-99"
)

# Число в диапазоне
age_field = FormElement(
    type="number",
    name="age",
    min=0,
    max=150,
    step=1,
    title="Возраст должен быть от 0 до 150 лет"
)
````

## Особенности использования

### Комбинирование атрибутов

```python
# Поле с множеством атрибутов
advanced_field = FormElement(
    # Основные атрибуты
    type="text",
    name="advanced",
    id="advanced-field",

    # Валидация
    required=True,
    minlength=5,
    maxlength=100,
    pattern="^[A-Za-z0-9\\s]+$",

    # Поведение
    autocomplete="off",
    autofocus=True,
    readonly=False,
    disabled=False,

    # Доступность
    aria_label="Расширенное поле",
    aria_required="true",

    # Стилизация
    classname="form-control advanced",
    style="border: 2px solid #007bff;",

    # События
    onfocus="handleFocus(event)",
    onblur="handleBlur(event)",
    oninput="handleInput(event)",

    # Data-атрибуты
    data_validation="strict",
    data_async="true",
    data_target="#result"
)
```

## Рекомендации

### Доступность

-     Всегда добавляйте aria-label или aria-labelledby для элементов без видимого текста
-     Используйте aria-required вместе с HTML5 required
-     Добавляйте aria-describedby для элементов с подсказками

### Безопасность

- Для полей паролей используйте autocomplete="off" или autocomplete="new-password"
- Валидируйте все пользовательские данные на стороне сервера
- Используйте CSRF-токены для защищенных форм

### UX/UI

- Используйте placeholder для примеров заполнения
- Добавляйте autofocus для основного поля формы
- Используйте соответствующие type для лучшей мобильной поддержки

### Ограничения

- Нет поддержки элементов <select> и <textarea> - только стандартные <input> элементы
- Ограниченная поддержка атрибутов - не все HTML5 атрибуты включены
- Нет валидации типов - ответственность за правильные типы лежит на разработчике
  Совместимость

### Все сгенерированные атрибуты совместимы с:

- HTML5 спецификацией
- Все современные браузеры (Chrome, Firefox, Safari, Edge)
- Мобильные браузеры
- Скринридеры и вспомогательные технологии
