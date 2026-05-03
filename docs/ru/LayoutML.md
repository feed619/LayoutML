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

### **init**(self, styles_dirname: str = "styles")

Параметры:

- styles_dirname (str): Директория для хранения сгенерированных CSS файлов. По умолчанию "styles"

Пример:

```python
app = LayoutML(styles_dirname="assets/css")
```

### Атрибуты

| Атрибут         | Тип    | Описание                                     |
| --------------- | ------ | -------------------------------------------- |
| router          | Router | Объект маршрутизатора для обработки запросов |
| error_page      | Page   | Страница для отображения ошибки 404          |
| \_pages         | list   | Список зарегистрированных страниц            |
| \_static_dirs   | dict   | MIME типы для статических файлов             |
| styles_dirname  | str    | Директория для CSS файлов                    |
| \_css_generated | bool   | Флаг генерации CSS файлов                    |

## Методы

### include_page(page: Page)

Регистрирует страницу для предварительной генерации CSS и JavaScript.

Параметры:

- page (Page): Экземпляр страницы для регистрации

Важно: Метод необходим для обработки страницы и создания её CSS файлов до обработки запросов.

Пример:

```python
from layoutml import Page

main_page = Page(title="Главная")
main_page.body.add_content("<h1>Добро пожаловать!</h1>")

app.include_page(main_page) # Регистрация страницы
```

### include_router(router: Router, prefix: str = "")

Включает под-роутер в основное приложение.

Параметры:

- router (Router): Экземпляр роутера для включения
- prefix (str): Префикс для всех маршрутов под-роутера

Пример:

```python
api_router = Router(prefix="/api")
app.include_router(api_router, prefix="/v1")
```

### route(endpoint: str)

Декоратор для регистрации обработчика маршрута.

Параметры:

- endpoint (str): Путь маршрута

Возвращает:
Декоратор для функции-обработчика

Пример:

```python

@app.route("/user")
async def get_user(request: Request, response: Response, user_id: int):
    page = main_page.copy() # Важно: копируйте страницу!
    page.body.add_content(f"<h1>Пользователь {user_id}</h1>")
    return page
```

### print_routes()

Выводит список всех зарегистрированных маршрутов в консоль.

```python
app.print_routes()

# Router: /
# --------------------------------------------------
# / -> home
# /user -> get_user
```

### set_error_page(page: Page)

Устанавливает кастомную страницу для ошибки 404.
Параметры:
page (Page): Страница ошибки

Пример:

```python
custom_404 = Page(title="Страница не найдена")
custom_404.body.add_content("<h1>404 - Не найдено</h1>")
app.set_error_page(custom_404)
```

### start(host: str = "localhost", port: int = 3700)

Запускает совместимый HTTP сервер.

Параметры:

- host (str): Хост для прослушивания
- port (int): Порт для прослушивания

Пример:

```python
if **name** == "**main**":
    app.start(host="0.0.0.0", port=8000)
```
