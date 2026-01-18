# Body

`Body` - является специализированным наследником базового класса [HTMLElement](base/HTMLElement.md), предназначенным для создания HTML <body> элемента с управлением основным содержимым страницы. Этот класс предоставляет удобный объектно-ориентированный интерфейс для добавления элементов, скриптов и управления фоном веб-страницы.

---

## Импорт

```python
from LayoutML import Body
```

## Конструктор

### **init**(content: str = "", \*\*kwargs)

Инициализирует новый Body элемент с начальным содержимым и атрибутами.

Параметры:

| Параметр   | Тип  | По умолчанию | Описание                                |
| ---------- | ---- | ------------ | --------------------------------------- |
| content    | str  | ""           | Начальное текстовое содержимое body     |
| \*\*kwargs | dict | -            | Дополнительные атрибуты для тега <body> |

Примеры инициализации:

```python
# Пустой body с базовыми атрибутами
body = Body()
# Body с начальным содержимым
body = Body(content="Добро пожаловать на наш сайт!")
# Body с атрибутами класса
body = Body(
    content="Содержимое страницы",
    class_="main-body dark-theme",
    id="pageBody",
    data_page="home"
)
# Body с обработчиками событий
body = Body(
    onload="initPage()",
    onscroll="handleScroll()",
    onresize="handleResize()"
)
```

## Атрибуты класса

| Атрибут        | Тип        | Описание                                    |
| -------------- | ---------- | ------------------------------------------- |
| content        | str        | Текстовое содержимое body                   |
| elements       | List[Any]  | Список HTML элементов для рендеринга        |
| scripts_footer | List[Dict] | Список скриптов для размещения в конце body |

## Методы

### add_content(content: str) -> "Body"

Добавляет текстовое содержимое к body.

Параметры:

- content (str): Текст для добавления

Возвращает:

- self: Позволяет использовать цепочки вызовов

Примеры:

```python
# Простое добавление текста
body = Body()
body.add_content("Добро пожаловать на наш сайт!")
# Цепочка вызовов
body.add_content("Основной контент").add_content("Дополнительный текст")
# Добавление форматированного текста
body.add_content("<h1>Заголовок</h1>")
body.add_content("<p>Абзац текста с <strong>выделением</strong>.</p>")
# Многострочный контент
body.add_content("""
    <div class="intro">
        <h2>Введение</h2>
        <p>Это первая страница нашего сайта.</p>
    </div>
""")
```

### add_element(element: Any) -> "Body"

Добавляет HTML элемент к содержимому body. Элемент должен иметь метод render() или быть преобразуемым в строку.

Параметры:

- element: Любой объект с методом render() или строковым представлением

Возвращает:

- self: Позволяет использовать цепочки вызовов

Примеры:

```python
from LayoutML.elements import FormElement

# Добавление элемента с методом render()
form = FormElement(
    form_type="email",
    id="user_email",
    name="email",
    required=True,
    pattern="[a-z0-9._%+-]+@[a-z0-9.-]+\\.[a-z]{2,}$"
))
body.add_element(form)

```

### delete_spaces(self)

Удаляет внешние и внутренние отступы у HTML-элемента, устанавливая нулевые значения для свойств margin и padding.

### set_overflow_hidden(self)

Устанавливает свойство overflow в значение hidden, что скрывает содержимое, выходящее за границы элемента.

### add_raw_html(html: str) -> "Body"

Добавляет сырой HTML код напрямую в body.

Параметры: - html (str): HTML код для добавления

Возвращает: - self: Позволяет использовать цепочки вызовов

Примеры:

```python
# Простой HTML
body.add_raw_html('<div class="alert">Внимание!</div>')


# Таблицы
body.add_raw_html("""
    <table class="data-table">
        <thead>
            <tr>
                <th>Имя</th>
                <th>Email</th>
                <th>Роль</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>Иван</td>
                <td>ivan@example.com</td>
                <td>Администратор</td>
            </tr>
        </tbody>
    </table>
""")
```

### add_script(src: Optional[str] = None, content: Optional[str] = None, \*\*attributes) -> "Body"

Добавляет скрипт в конец body (перед закрывающим тегом </body>).

Параметры:

- src (Optional[str]): URL внешнего скрипта
- content (Optional[str]): Встроенный JavaScript код
- \*\*attributes: Дополнительные атрибуты скрипта

Возвращает:

- self: Позволяет использовать цепочки вызовов

Примеры:

```python
# Внешний скрипт
body.add_script_footer(src="/js/main.js")
body.add_script_footer(src="/js/analytics.js", async=True)
# Внешний скрипт с defer
body.add_script_footer(src="/js/app.js", defer=True)
# Встроенный скрипт
body.add_script_footer(content="""
    // Инициализация после загрузки DOM
    page.addEventListener('DOMContentLoaded', function() {
        console.log('Страница загружена');
        initComponents();
        setupEventListeners();
    });
""")
# Несколько скриптов
body.add_script_footer(src="/js/vendor.js")
    .add_script_footer(src="/js/components.js")
    .add_script_footer(src="/js/main.js")
    .add_script_footer(content="console.log('Все скрипты загружены');")
```

### set_background(color: str = None, image: str = None) -> "Body"

Устанавливает фон для body (цвет, изображение или оба).

Параметры:

- color (str): Цвет фона (HEX, RGB, имя цвета)
- image (str): URL изображения для фона

Возвращает:

- self: Позволяет использовать цепочки вызовов

Примеры:

```python
# Только цвет фона
body.set_background(color="#f5f5f5")
# Только изображение фона
body.set_background(image="/images/background.jpg")
# Цвет и изображение
body.set_background(color="#000000", image="/images/pattern.png")
# Градиентный фон
body.set_background(color="linear-gradient(135deg, #667eea 0%, #764ba2 100%)")
```

### Методы рендеринга

render() -> str

Создает полный HTML код элемента <body> со всем содержимым и скриптами.

Возвращает:

- str: Полный HTML тег <body> с содержимым

Порядок рендеринга:

- Текстовое содержимое (self.content)
- HTML элементы (self.elements)
- Скрипты в конце body (self.scripts_footer)
- Атрибуты тега <body>

### get_html() -> str

Алиас для метода render().

Возвращает:

- str: Полный HTML тег <body> с содержимым

### **iadd**(other: Any) -> "Body"

Перегрузка оператора += для удобного добавления элементов.

Параметры:

- other: Элемент для добавления

Возвращает:

- self: Обновленный объект Body

Примеры:

```python
body = Body()
# Использование оператора +=
body += '<p>Текст</p>'
# Эквивалентно:
body.add_element(div)
    .add_element('<p>Текст</p>')
    .add_element(Button(content="Кнопка"))
```

## Практические примеры

```python
from LayoutML import Body
from LayoutML.elements import FormElement

# Создаем body
body = Body(class_="main-body")

form = FormElement(
    form_type="email",
    id_="user_email",
    name="email",
    required=True,
    pattern="[a-z0-9._%+-]+@[a-z0-9.-]+\\.[a-z]{2,}$"
))

body.add_element(form)
# Добавляем скрипты
body.add_script_footer(src="/js/main.js")
```
