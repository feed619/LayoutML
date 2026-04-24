# LayoutML

`LayoutML` - это основной класс фреймворка, который объединяет маршрутизацию, генерацию стилей и обработку HTTP запросов. Класс предоставляет ASGI-совместимый интерфейс для создания веб-приложений с автоматической генерацией CSS файлов на основе стилей определённых в страницах.

---

## Импорт

```python
from layoutml import LayoutML
```

## Назначение

- Маршрутизация: Обработка HTTP запросов и вызов соответствующих обработчиков
- Генерация CSS: Автоматическое создание CSS файлов из стилей определённых в компонентах
- Статические файлы: Обслуживание статических ресурсов (изображения, CSS, JS)
- ASGI совместимость: Поддержка асинхронного ASGI интерфейса для интеграции с серверами (Uvicorn, Hypercorn)

## Конструктор

### **init**(styles_dirname: str = "styles")

Создаёт новый экземпляр приложения LayoutML.

Параметры: - styles_dirname (str): Имя директории для хранения сгенерированных CSS файлов. По умолчанию "styles"

Автоматически инициализируемые свойства:

- \_router: экземпляр Router для маршрутизации
- error_page: страница для отображения ошибки 404
- \_static_dirs: словарь расширений и MIME-типов для статических файлов
- styles_dirname: имя директории CSS
- stylesheet_files: словарь для хранения соответствий путей и CSS файлов
- \_css_generated: флаг генерации CSS

### Примеры:

```python
# Создание приложения с настройками по умолчанию
app = LayoutML()
# Создание с кастомной директорией стилей
app = LayoutML(styles_dirname="assets/css")
```

## Атрибуты класса

| Атрибут          | Тип    | Описание                               |
| ---------------- | ------ | -------------------------------------- |
| \_router         | Router | Внутренний роутер для маршрутизации    |
| error_page       | Page   | Страница для отображения ошибки 404    |
| \_static_dirs    | dict   | Маппинг расширений файлов на MIME-типы |
| styles_dirname   | str    | Директория для CSS файлов              |
| stylesheet_files | dict   | Соответствие путей и CSS файлов        |
| \_css_generated  | bool   | Флаг генерации CSS                     |

## Основные методы

### ensure_css_generated()

Генерирует CSS файлы, если они ещё не были созданы.

```python
app = LayoutML()
app.ensure_css_generated()  # Создаст CSS файлы в директории styles/
```

### route(endpoint)

Добавляет обработку эндпоинта

Параметры:

- enpoint: название эндпоинта

```python
from layoutml import LayoutML, Page, Body, Paragraph
# Создание приложения
app = LayoutML()
@app.route("/")
def home():
    page = Page(title="Главная страница")
    page.body.get_html(content="<h1>Добро пожаловать!</h1>")
    return page

```

### include_router(router: Router, prefix: str = "")

Включает дочерний роутер в основное приложение с опциональным префиксом.

Параметры:

- router (Router): Роутер для включения
- prefix (str): Префикс для всех маршрутов роутера

```python
from layoutml import Router

# Создание API роутера
api_router = Router(prefix="/api")

@api_router.route("/users")
def get_users():
    return Page(title="Пользователи")

# Включение в приложение
app = LayoutML()
app.include_router(api_router)
```


### set_error_page(page: Page)

Устанавливает страницу, которая будет отображаться при ошибке 404.

Параметры:

- page (Page): Страница для отображения ошибки

```python

from layoutml import Page

error_page = Page(title="404 - Страница не найдена")
error_page.body.get_html(content="<h1>404</h1><p>Страница не найдена</p>")

app = LayoutML()
app.set_error_page(error_page)
```

### render_css_files()

Генерирует CSS файлы для всех зарегистрированных маршрутов.

Особенности:

- Собирает стили из всех страниц через get_styles()
- Создаёт отдельные CSS файлы для каждой страницы
- Сохраняет соответствие между маршрутами и CSS файлами в stylesheet_files

```python
app = LayoutML()

# ... регистрация маршрутов

app.render_css_files() # Создаст CSS файлы в styles_dirname

start(host: str = "localhost", port: int = 5005)
```

Запускает встроенный ASGI сервер в режиме совместимости.
Параметры:

- host (str): Хост для запуска сервера
- port (int): Порт для запуска сервера

Примечание: Этот метод предназначен для упрощённого запуска и использует asyncio сервер.

```python
app = LayoutML()
# ... настройка маршрутов
app.start(host="0.0.0.0", port=8000)
```

### ASGI метод **call**(scope, receive, send)

Основной ASGI метод, который делает приложение совместимым с ASGI серверами (Uvicorn, Hypercorn).
Параметры:

- scope (Dict[str, Any]): ASGI scope с информацией о запросе
- receive (Callable): Функция для получения тела запроса
- send (Callable): Функция для отправки ответа

```python
# Запуск с Uvicorn
import uvicorn

app = LayoutML()
# ... настройка маршрутов

if **name** == "**main**":
uvicorn.run(app, host="0.0.0.0", port=8000)
```

## Внутренние методы

### \_is_static_file(path: str) -> bool

Проверяет, является ли путь статическим файлом.

### \_serve_html(scope, receive, send, html_content=None, path=None)

Отдаёт HTML страницу клиенту.

### \_serve_static_file(path, scope, receive, send)

Отдаёт статические файлы (CSS, изображения, JS).

### \_serve_404(scope, receive, send)

Отдаёт страницу ошибки 404.

## Примеры использования

### Простое приложение

```python
from layoutml import LayoutML, Page, Body, Paragraph
# Создание приложения
app = LayoutML()
# Регистрация маршрута

@app.route("/")
def home():
    page = Page(title="Главная страница")
    page.body.get_html(content="<h1>Добро пожаловать!</h1>")
    return page

# Запуск приложения
app.start(host="localhost", port=5005)
```

### Приложение с несколькими страницами

```python
from layoutml import LayoutML, Page, Header, Paragraph, Anchor
app = LayoutML()
# Главная страница

@app.route("/")
def home():
    page = Page(title="Главная")
    page.body.get_html(content="""
    <h1>Главная страница</h1>
    <nav>
    <a href="/about">О нас</a> |
    <a href="/contact">Контакты</a>
    </nav>
    """)
    return page

# Страница "О нас"
@app.route("/about")
def about():
    page = Page(title="О нас")
    page.body.get_html(content="<h1>О компании</h1><p>Мы лучшие!</p>")
    return page

# Страница "Контакты"
@app.route("/contact")
def contact():
    page = Page(title="Контакты")
    page.body.get_html(content="<h1>Контакты</h1><p>Email: info@example.com</p>")
    return page

# Установка страницы ошибки
error_page = Page(title="404")
error_page.body.get_html(content="<h1>404</h1><p>Страница не найдена</p>")
app.set_error_page(error_page)

# Запуск
app.start()
```

### Приложение со стилями

```python
from layoutml import LayoutML, Page, Header, Paragraph, Image

app = LayoutML()

@app.route("/styled")
def styled_page():
    page = Page(title="Стилизованная страница")
    # Добавление стилей через object_styles
    header = Header(object_name="mainHeader")
    header.object_styles.set_background_color("linear-gradient(135deg, #667eea 0%, #764ba2 100%)")\
                        .set_color("white")\
                        .set_padding("60px 20px")\
                        .set_text_align("center")
    header.get_html(content="<h1>Стилизованная страница</h1>")

    paragraph = Paragraph(text="Этот текст будет стилизован через CSS.")
    paragraph.object_styles.set_font_size("18px")\
                           .set_line_height("1.6")\
                           .set_color("#333")

    page.body.add_element(header)
    page.body.add_element(paragraph)

    return page

# При запуске CSS будет сгенерирован автоматически
app.start()
```

### Приложение с вложенными роутерами

```python
from layoutml import LayoutML, Router, Page

app = LayoutML()

# API роутер
api_router = Router(prefix="/api")

@api_router.route("/users")
def get_users():
    page = Page(title="Пользователи API")
    page.body.get_html(content="""
    <h1>Список пользователей</h1>
    <ul>
    <li>Иван Петров</li>
    <li>Мария Иванова</li>
    </ul>
    """)
    return page

@api_router.route("/posts")
def get_posts():
    page = Page(title="Посты API")
    page.body.get_html(content="<h1>Список постов</h1>")
    return page

# Админ роутер
admin_router = Router(prefix="/admin")

@admin_router.route("/dashboard")
def admin_dashboard():
    page = Page(title="Админ панель")
    page.body.get_html(content="<h1>Добро пожаловать в админку!</h1>")
    return page

# Включение роутеров
app.include_router(api_router)
app.include_router(admin_router)

# Основной маршрут
@app.route("/")
def home():
    page = Page(title="Главная")
    page.body.get_html(content="""
    <h1>Добро пожаловать!</h1>
    <nav>
    <a href="/api/users">API Пользователи</a> |
    <a href="/api/posts">API Посты</a> |
    <a href="/admin/dashboard">Админ панель</a>
    </nav>
    """)
    return page

app.start()
```

### Интеграция с Uvicorn

```python

import uvicorn
from layoutml import LayoutML, Page

app = LayoutML()

@app.route("/")
def home():
    return Page(title="Главная")

# Запуск через uvicorn

if __name__ == "__main__":

uvicorn.run(app, host="0.0.0.0", port=8000)
```

### Приложение со статическими файлами

```python
from layoutml import LayoutML, Page

app = LayoutML()

@app.route("/image-page")
def image_page():
    page = Page(title="Изображения")
    page.body.get_html(content='''
    <h1>Галерея изображений</h1>
    <img src="/static/logo.png" alt="Логотип">
    <img src="/images/photo.jpg" alt="Фото">
    ''')
return page

# Статические файлы автоматически обслуживаются
# Файлы из корня проекта: logo.png, images/photo.jpg и т.д.
```

## Лучшие практики

1. Организация кода

```python
# main.py
from layoutml import LayoutML
from routers import api_router, admin_router

app = LayoutML(styles_dirname="static/css")

# Регистрация роутеров
app.include_router(api_router, prefix="/api")
app.include_router(admin_router, prefix="/admin")

# Запуск
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

2. Разделение маршрутов

```python
# routers/users.py
from layoutml import Router, Page

users_router = Router(prefix="/users")

@users_router.route("/")
def list_users():
    return Page(title="Пользователи")

@users_router.route("/<user_id>")
def user_detail(user_id: str):
    return Page(title=f"Пользователь {user_id}")

# main.py
app.include_router(users_router)
```
