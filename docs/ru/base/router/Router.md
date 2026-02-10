# Router

`Router` - это класс для маршрутизации URL в веб-приложениях. Он предоставляет систему декларативного определения маршрутов, поддержку параметров пути, вложенных роутеров и диспетчеризацию запросов как для синхронных, так и для асинхронных обработчиков.

## Атрибуты класса

| Атрибут         | Тип                 | Описание                                  |
| --------------- | ------------------- | ----------------------------------------- |
| routes          | Dict[str, Dict]     | Словарь всех зарегистрированных маршрутов |
| prefix          | str                 | Префикс всех маршрутов этого роутера      |
| \_child_routers | Dict[str, "Router"] | Словарь дочерних роутеров                 |

## Конструктор

### **init**(prefix: str = "")

Создаёт новый роутер с опциональным префиксом для всех маршрутов.

Параметры:

- prefix (str): Префикс для всех маршрутов этого роутера. По умолчанию пустая строка

Примеры:

```python
# Роутер без префикса
router = Router()
# Роутер с префиксом /api
api_router = Router(prefix="/api")
# Роутер с префиксом /admin
admin_router = Router(prefix="/admin")
```

## Основные методы

### Декоратор route(path: str)

Декоратор для регистрации функции как обработчика маршрута.

Параметры:

- path (str): Путь маршрута (может содержать параметры в формате <name>)

Примеры:

```python
router = Router()

# Простой маршрут
@router.route("/")
def home():
    return "Главная страница"

# Маршрут с параметром
@router.route("/user/<user_id>")
def get_user(user_id: str):
    return f"Пользователь {user_id}"

# Асинхронный маршрут
@router.route("/data")
async def get_data():
    data = await fetch_from_db()
    return data
```

### add(endpoint: str) -> Callable

Альтернативный метод для регистрации маршрутов (синоним для route).

```python
router = Router()

@router.add("/about")
def about():
    return "О нас"
```

### include_router(router: "Router", prefix: str = "")

Включает другой роутер в текущий с опциональным префиксом.

Параметры:

- router (Router): Роутер для включения
- prefix (str): Дополнительный префикс для маршрутов включаемого роутера

Особенности:

- Поддерживает рекурсивное включение (роутеры внутри роутеров)
- Автоматически обрабатывает префиксы
- Проверяет циклические зависимости

Примеры:

```python
# Создание основного роутера
main_router = Router()

# Создание API роутера
api_router = Router(prefix="/api")
@api_router.route("/users")
def get_users():
    return ["user1", "user2"]

# Включение API роутера в основной
main_router.include_router(api_router)
# Теперь маршрут доступен по /api/users

# Включение с дополнительным префиксом
main_router.include_router(api_router, prefix="/v1")
# Теперь маршрут доступен по /v1/api/users
```

### dispatch(path: str, \*args, \*\*kwargs) -> Any

Выполняет обработчик для указанного пути.

Параметры:

- path (str): Путь для диспетчеризации
- \*args: Позиционные аргументы для передачи в обработчик
- \*\*kwargs: Именованные аргументы для передачи в обработчик

Возвращает:

- Результат выполнения обработчика

Особенности:

- Автоматически определяет синхронный или асинхронный обработчик
- Извлекает параметры из пути
- Объединяет параметры пути с переданными аргументами

Примеры:

```python
router = Router()

@router.route("/hello/<name>")
def greet(name: str, greeting: str = "Привет"):
    return f"{greeting}, {name}!"

# Синхронный вызов
result = router.dispatch("/hello/Иван")
print(result)  # "Привет, Иван!"

# С дополнительными параметрами
result = router.dispatch("/hello/Мария", greeting="Здравствуй")
print(result)  # "Здравствуй, Мария!"

# Асинхронный вызов (если обработчик async)
@router.route("/async")
async def async_handler():
    await asyncio.sleep(1)
    return "Готово"

# Внутри async функции
result = await router.dispatch("/async")
```

### get_all_routes() -> Dict[str, Any]

Возвращает словарь всех зарегистрированных маршрутов.

```python
router = Router()
router.route("/home")(lambda: "Home")
router.route("/about")(lambda: "About")

routes = router.get_all_routes()
# {
#     '/home': {...},
#     '/about': {...}
# }
```

### print_routes()

Выводит все маршруты в читаемом формате в консоль.

```python
router = Router()
router.route("/")(lambda: "Home")
router.route("/user/<id>")(lambda id: f"User {id}")

router.print_routes()
# Вывод:
# Router: /
# --------------------------------------------------
# [SYNC]  / -> <lambda>
# [SYNC]  /user/<id> -> <lambda>
```
