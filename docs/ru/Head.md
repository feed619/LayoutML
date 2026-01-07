# Head

`Head` - является специализированным наследником базового класса HTMLElement, предназначенным для создания HTML <head> элемента с полным набором мета-тегов, стилей, скриптов и других ресурсов, необходимых для веб-страницы. Этот класс предоставляет удобный объектно-ориентированный интерфейс для управления мета-информацией и ресурсами страницы.

---

## Импорт

```python
from LayoutML import Head
```

## Конструктор

### **init**(title: str = "", \*\*kwargs)

Инициализирует новый Head элемент с базовой конфигурацией.

Параметры:

| Параметр   | Тип  | По умолчанию | Описание                                              |
| ---------- | ---- | ------------ | ----------------------------------------------------- |
| title      | str  | ""           | Заголовок страницы (отображается во вкладке браузера) |
| \*\*kwargs | dict | -            | Дополнительные атрибуты для тега <head>               |

Автоматически добавляемые мета-теги:

- `<meta charset="UTF-8">` - кодировка UTF-8
- `<meta name="viewport" content="width=device-width, initial-scale=1.0">` - адаптивность для мобильных устройств

## Атрибуты класса

| Константа  | Тип           | По умолчанию                                   |
| ---------- | ------------- | ---------------------------------------------- |
| title      | str           | Заголовок страницы                             |
| meta_tags  | List[Dict]    | Список словарей с атрибутами мета-тегов        |
| links      | List[Dict]    | Список словарей с атрибутами link тегов        |
| scripts    | List[Dict]    | Список словарей с атрибутами script тегов      |
| styles_css | List[str]     | Список строк с CSS кодом для встроенных стилей |
| base_url   | Optional[str] | Базовый URL для страницы                       |

## Методы

### set_title(title: str) -> "Head"

Устанавливает или изменяет заголовок страницы.

Параметры:

- title (str): Новый заголовок страницы
  Возвращает:
- self: Позволяет использовать цепочки вызовов

Примеры:

```python
# Установка заголовка при создании
head = Head(title="Исходный заголовок")

# Изменение заголовка
head.set_title("Новый заголовок страницы")

# Цепочка вызовов
head.set_title("Продукты").add_meta(name="description", content="Каталог продукции")
```

### add_meta(\*\*attributes) -> "Head"

Добавляет мета-тег с указанными атрибутами.

Параметры:

- \*\*attributes: Пары ключ-значение для атрибутов мета-тега

Возвращает:

- self: Позволяет использовать цепочки вызовов

Типичные мета-теги:

```python
# Кодировка (уже добавлена по умолчанию)
head.add_meta(charset="UTF-8")
# Viewport для мобильных устройств (уже добавлен по умолчанию)
head.add_meta(name="viewport", content="width=device-width, initial-scale=1.0")
# Описание страницы для SEO
head.add_meta(
    name="description",
    content="Интернет-магазин электроники с доставкой по всей России"
)
# Ключевые слова для SEO
head.add_meta(
    name="keywords",
    content="электроника, смартфоны, ноутбуки, доставка, интернет-магазин"
)
```

### add_link(rel: str, href: str, \*\*attributes) -> "Head"

Добавляет тег <link> с указанными атрибутами.

Параметры:

- rel (str): Тип отношения между текущим документом и ссылаемым ресурсом
- href (str): URL ресурса
- \*\*attributes: Дополнительные атрибуты

Возвращает:

- self: Позволяет использовать цепочки вызовов

Примеры:

```python
# CSS стили
head.add_link(rel="stylesheet", href="/css/main.css")
head.add_link(rel="stylesheet", href="/css/print.css", media="print")
# Иконки (favicon)
head.add_link(rel="icon", href="/favicon.ico", type="image/x-icon")
head.add_link(rel="icon", href="/icon.svg", type="image/svg+xml")
# Канонические ссылки
head.add_link(rel="canonical", href="https://example.com/original-page")
# Предварительная загрузка
head.add_link(rel="preload", href="/fonts/roboto.woff2", as_="font", type="font/woff2", crossorigin="anonymous")
```

### add_script(src: Optional[str] = None, content: Optional[str] = None, \*\*attributes) -> "Head"

Добавляет тег <script> с указанными параметрами.

Параметры:

- src (Optional[str]): URL внешнего скрипта
- content (Optional[str]): Встроенный JavaScript код
- \*\*attributes: Дополнительные атрибуты

Возвращает:

- self: Позволяет использовать цепочки вызовов

Примеры:

```python
# Внешний скрипт с defer
head.add_script(src="/js/main.js", defer=True)
# Внешний скрипт с async
head.add_script(src="/js/analytics.js", async=True)
# Внешний модуль
head.add_script(src="/js/app.js", type="module")
# Встроенный скрипт
head.add_script(
    content="""
        console.log('Страница загружается');
        window.APP_CONFIG = {
            apiUrl: 'https://api.example.com',
            debug: false
        };
    """,
    type="application/javascript"
)

```

### add_style_css(css: str) -> "Head"

Добавляет встроенные CSS стили.

Параметры:

- css (str): CSS код

Возвращает:

- self: Позволяет использовать цепочки вызовов

Примеры:

```python
# Простые стили
head.add_style_css("body { margin: 0; padding: 0; }")
# Критические стили для ускорения загрузки
head.add_style_css("""
    .critical { display: block; }
    .hidden { display: none; }
    * { box-sizing: border-box; }
""")
# Анимации
head.add_style_css("""
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }
    .fade-in { animation: fadeIn 0.5s ease-in; }
""")

```

## Специализированные методы

### set_base(url: str, target: str = "\_blank") -> "Head"

Устанавливает базовый URL для всех относительных ссылок на странице.

Параметры:

- url (str): Базовый URL
- target (str): Целевое окно по умолчанию

Возвращает:

- self: Позволяет использовать цепочки вызовов

Примеры:

```python
# Установка базового URL
head.set_base("https://example.com/")
# С указанием target
head.set_base("https://example.com/", target="_self")
```

### add_icon(href: str, type: str = "image/x-icon") -> "Head"

Добавляет фавиконку (иконку сайта).

Параметры:

- href (str): Путь к иконке
- type (str): MIME-тип иконки

Возвращает:

- self: Позволяет использовать цепочки вызовов

Примеры:

```python
# Стандартная favicon
head.add_icon("/favicon.ico")
# SVG иконка
head.add_icon("/icon.svg", type="image/svg+xml")
# PNG иконка
head.add_icon("/icon-32x32.png", type="image/png")

```

### add_stylesheet(href: str, media: str = "all") -> "Head"

Добавляет внешнюю CSS таблицу стилей.

Параметры:

- href (str): Путь к CSS файлу
- media (str): Медиа-запрос для применения стилей

Возвращает:

- self: Позволяет использовать цепочки вызовов

Примеры:

```python
# Основной CSS файл
head.add_stylesheet("/css/main.css")
# CSS для печати
head.add_stylesheet("/css/print.css", media="print")
# CSS для мобильных устройств
head.add_stylesheet("/css/mobile.css", media="(max-width: 768px)")
```

### add_preconnect(url: str) -> "Head"

Добавляет предварительное подключение к домену для ускорения загрузки ресурсов.

Параметры:

- url (str): URL домена для предварительного подключения

Возвращает:

- self: Позволяет использовать цепочки вызовов

Примеры:

```python
# Предварительное подключение к CDN
head.add_preconnect("https://fonts.googleapis.com")
head.add_preconnect("https://fonts.gstatic.com")
# Для API
head.add_preconnect("https://api.example.com")
# Для аналитики
head.add_preconnect("https://www.google-analytics.com")
```

### add_preload(href: str, as_type: str, \*\*attributes) -> "Head"

Добавляет предзагрузку важных ресурсов для ускорения отображения страницы.

Параметры:

- href (str): Путь к ресурсу
- as_type (str): Тип ресурса (font, style, script, image, etc.)
- \*\*attributes: Дополнительные атрибуты

Возвращает:

- self: Позволяет использовать цепочки вызовов

Примеры:

```python
# Предзагрузка шрифтов
head.add_preload(
    href="/fonts/roboto.woff2",
    as_type="font",
    type="font/woff2",
    crossorigin="anonymous"
)
# Предзагрузка критического CSS
head.add_preload(
    href="/css/critical.css",
    as_type="style"
)
# Предзагрузка изображений для hero-секции
head.add_preload(
    href="/images/hero-banner.jpg",
    as_type="image",
    imagesrcset="hero-banner-320w.jpg 320w, hero-banner-640w.jpg 640w",
    imagesizes="100vw"
)
# Предзагрузка JavaScript
head.add_preload(
    href="/js/main.js",
    as_type="script"
)
```

### render() -> str

Создает полный HTML код элемента <head> со всем содержимым.

Возвращает:

- str: Полный HTML тег <head> с содержимым

Порядок рендеринга:

- Заголовок <title>
- Мета-теги
- Link теги (включая <base>)
- Встроенные стили <style>
- Script теги
- Атрибуты самого тега <head>

### get_html() -> str

Вызывает метода render().

Возвращает:
str: Полный HTML тег <head> с содержимым

### Практические примеры

```python
from LayoutML import Head

head = Head(
    title="Интернет-магазин электроники",
    lang="ru"
)
# Мета-теги для SEO
head.add_meta(
    name="description",
    content="Купить смартфоны, ноутбуки, телевизоры и другую электронику по выгодным ценам"
)
head.add_meta(
    name="keywords",
    content="электроника, смартфоны, ноутбуки, телевизоры, купить, цена"
)
head.add_meta(name="author", content="ООО 'Электроник'")
# Open Graph для социальных сетей
head.add_meta(property="og:title", content="Интернет-магазин электроники")
head.add_meta(property="og:type", content="website")
head.add_meta(property="og:url", content="https://electronics-shop.ru")
head.add_meta(property="og:image", content="https://electronics-shop.ru/og-image.jpg")
# Стили
head.add_stylesheet("/css/bootstrap.min.css")
head.add_stylesheet("/css/main.css")
head.add_stylesheet("/css/responsive.css", media="(max-width: 768px)")
# Иконки
head.add_icon("/favicon.ico")
head.add_link(rel="apple-touch-icon", href="/apple-touch-icon.png")
# Скрипты
head.add_script(src="/js/jquery.min.js", defer=True)
head.add_script(src="/js/main.js", defer=True)
# Критические стили для ускорения загрузки
head.add_style_css("""
    * { box-sizing: border-box; }
    body { margin: 0; font-family: Arial, sans-serif; }
    .loader { display: none; }
""")
```
