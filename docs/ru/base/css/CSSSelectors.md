# CSSSelectors

`CSSSelectors` - это контейнерный класс для управления коллекцией CSS селекторов и их стилей. Класс позволяет удобно работать с множеством селекторов (классы, ID, теги, медиа-запросы) и генерировать из них полноценные CSS стили.

---

## Архитектура

- Контейнер селекторов: Хранит коллекцию объектов CSSBase
- Динамическое создание: Селекторы создаются автоматически при обращении
- Гибкая настройка: Поддержка классов, ID, тегов и медиа-запросов
- Два режима вывода: Чистый CSS или HTML тег <style>

## Импорт

```python
from layoutML.base.css import CSSInline
```

## Конструктор

### **init**(inline: bool = False)

Создаёт новый контейнер для CSS селекторов.

Параметры:

- inline (bool): Если True, метод get_styles_str() будет оборачивать CSS в тег <style>. По умолчанию False.

Примеры:

```python
# Создание контейнера для внешнего CSS файла
css = CSSSelectors()
# Создание контейнера для inline стилей в HTML
css_inline = CSSSelectors(inline=True)
```

## Атрибуты класса

| Атрибут   | Тип           | Описание                                | Значение по умолчанию |
| --------- | ------------- | --------------------------------------- | --------------------- |
| selectors | dict[CSSBase] | Словарь, содержащий все селекторы       | {} (пустой словарь)   |
| inline    | bool          | Флаг, определяющий режим вывода стилей. | False                 |

## Методы

### add_selector(name, type="class", style=None)

Явное добавление селектора с указанным типом и начальными стилями.

Параметры:

- name (str): Имя селектора
- type (str): Тип селектора. Допустимые значения: "class", "id", "tag". По умолчанию "class"
- style (str, optional): Начальная строка CSS стилей

Возвращает:

- CSSBase: Экземпляр CSSBase для добавленного селектора

Примеры:

```python
# Добавление класса
css_input.add_selector("container", "class", "width: 100%;")
# Добавление ID
css_input.add_selector("header", "id", "background: #333;")
# Добавление тега
css_input.add_selector("p", "tag", "margin: 10px 0;")
# Без начальных стилей
css_input.add_selector("button", "class")
```

### delete_selector(name)

Удаляет селектор из коллекции self.selectors.

Параметры:

- name (str): Имя удаляемого селектора

Пример:

```python
css = CSSSelectors()
css.add_selector("temp-class")
print("temp-class" in css.selectors)  # True
css.delete_selector("temp-class")
print("temp-class" in css.selectors)  # False
```

### clear() -> "CSSBase"

Очищает словарь self.selectors, удаляя все селекторы.

Пример:

```python
css = CSSSelectors()
css.add_selector("class1")
css.add_selector("class2")
print(len(css.selectors))  # 2
css.clear()
print(len(css.selectors))  # 0
print(css.selectors)  # {}
```

### selector_exists(name: str) -> tuple[bool, str]

Проверяет существование селектора в self.selectors.

Параметры:

- name (str): Имя проверяемого селектора

Возвращает:

- Кортеж (bool, str) - существует ли селектор

Пример:

```python

css = CSSSelectors()
css.add_selector("my-class")

exists = css.selector_exists("my-class")  # (True, "class")
not_exists = css.selector_exists("other")  # (False, "")
```

### add_styles(selector_name: str, styles: dict | CSSBase)

Добавляет стили к существующему селектору в self.selectors.

Параметры:

- selector_name (str): Имя селектора
- styles (dict | CSSBase): Стили для добавления

Пример:

```python
css = CSSSelectors()
css.add_selector("box")
# Проверка начального состояния
print(css.selectors["box"].styles)  # {}

# Добавление стилей через словарь
css.add_styles("box", {"width": "100px", "height": "100px"})
print(css.selectors["box"].styles)  # {'width': '100px', 'height': '100px'}
```

### get_styles(space=True) -> dict

Генерирует словарь со стилями для всех селекторов из self.selectors.

Параметры:

- space (bool): Если True, форматирует с пробелами и переносами строк

Возвращает:

- Словарь, где ключи - имена селекторов с префиксами, значения - CSS строки

Пример:

```python
css = CSSSelectors()
css.add_selector("container", "class").set_width("100%")
css.add_selector("header", "id").set_background_color("blue")

styles_dict = css.get_styles()
# Результат: {'.container': 'width:100%;', '#header': 'background-color:blue;'}
```

### get_styles_str() -> str

Генерирует строку с CSS стилями. Использует атрибут inline для определения формата вывода.

Логика работы:

- Получает стили через self.get_styles()
- Формирует строку CSS для каждого селектора
- Если self.inline == True, оборачивает в тег <style>

Примеры:

```python
# Режим для внешнего CSS файла
css = CSSSelectors(inline=False)
css.add_selector("container").set_width("100%")
print(css.get_styles_str())
# Результат:
# .container {
# width:100%;
# }

# Режим для inline стилей в HTML
css_inline = CSSSelectors(inline=True)
css_inline.add_selector("container").set_width("100%")
print(css_inline.get_styles_str())
# Результат:
# <style>
# .container {
# width:100%;
# }
# </style>
```

## Специальные методы Python

### Динамический доступ к селекторам через атрибуты

```python
css = CSSSelectors()

# Автоматическое создание селектора при обращении к атрибуту
css.container.set_width("100%")  # Создаёт селектор "container" в self.selectors
css.header.set_background_color("blue")  # Создаёт селектор "header"

# Проверка
print(css.selectors.keys())  # dict_keys(['container', 'header'])
```

### Работа как со словарём

```python

css = CSSSelectors()

# Получение селектора (автоматическое создание при отсутствии)
selector = css["my-class"]
print("my-class" in css.selectors)  # True

# Установка селектора разными способами
css["my-class"] = CSSBase().set_width("100px")
css["another"] = {"width": "100px"}  # через словарь
css["third"] = "width: 100px;"  # через строку

# Удаление селектора
del css["my-class"]
print("my-class" in css.selectors)  # False

# Проверка количества через len()
count = len(css)  # Использует len(self.selectors)

# Проверка на пустоту через bool()
if css:  # True, если self.selectors не пуст
    print("Есть селекторы")

# Итерация по селекторам
for name, selector in css:
    print(f"Селектор: {name}, Стили: {selector.get_styles_string()}")
```

## Типы селекторов и их префиксы

Типы селекторов хранятся в атрибуте type каждого объекта CSSBase в self.selectors:

| Атрибут | Тип | Описание |

| Тип     | Префикс | Пример в CSS              |
| ------- | ------- | ------------------------- |
| "class" | .       | .container                |
| "id"    | #       | #header                   |
| "tag"   | нет     | div                       |
| "media" | нет     | @media (max-width: 768px) |

## Примеры использования

### Пример 1: Создание компонента кнопки с использованием атрибутов

```python
css = CSSSelectors(inline=True)  # Для вставки в HTML
print(f"Режим inline: {css.inline}")
print(f"Начальное количество селекторов: {len(css.selectors)}")

# Базовый стиль кнопки
css.btn.set_display("inline-block")\
       .set_padding("10px 20px")\
       .set_background_color("#007bff")

# Hover состояние (автоматическое создание)
css["btn:hover"].set_background_color("#0056b3")

print(f"Конечное количество селекторов: {len(css.selectors)}")
print(f"Имена селекторов: {list(css.selectors.keys())}")

# Генерация CSS
print(css.get_styles_str())
```

### Пример 2: Работа с атрибутом inline

```python
def generate_page_styles(inline_mode=False):
    """Генератор стилей с разными режимами вывода"""
    css = CSSSelectors(inline=inline_mode)

    # Определение стилей
    css.container.set_width("100%").set_max_width("1200px")
    css.header.set_background_color("#333").set_color("white")

    return css.get_styles_str()

# Для внешнего файла
external_css = generate_page_styles(inline=False)
with open("styles.css", "w") as f:
    f.write(external_css)

# Для inline в HTML
inline_css = generate_page_styles(inline=True)
html_template = f"""
<!DOCTYPE html>
<html>
<head>
    {inline_css}
</head>
<body>
    <!-- содержимое -->
</body>
</html>
"""
```
