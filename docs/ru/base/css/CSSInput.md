# CSSInput

`CSSInput` - это класс для динамического управления CSS селекторами и их стилями. Он предоставляет возможность создавать, модифицировать и рендерить CSS правила в виде стилевых блоков для использования в HTML документах. Класс использует паттерн "динамических атрибутов" для удобного доступа к селекторам.

---

## Основные возможности

    Динамическое создание CSS селекторов
    Поддержка классов, ID и тегов
    Цепочное добавление стилей через CSSBase
    Автоматическая генерация CSS блоков
    Управление селекторами через методы

## Импорт

```python
from LayoutML.base.css import CSSInline
```

## Конструктор

### def **init**(self)

Создает пустой экземпляр CSSInput без селекторов.

Пример

```python
css_input = CSSInput()
```

### Атрибуты

#### selectors

Словарь, содержащий все созданные селекторы. Ключи - имена селекторов, значения - экземпляры CSSBase.

## Типы селекторов

Классы (.class)

```python
css_input.add_selector("my-class", "class")
# Генерирует: .my-class { ... }
```

ID (#id)

```python
css_input.add_selector("main", "id")
# Генерирует: #main { ... }
```

Теги (tag)

```python
css_input.add_selector("p", "tag")
# Генерирует: p { ... }
```

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

Удаляет селектор из коллекции.
Параметры:

- name (str): Имя удаляемого селектора

Пример:

```python
css_input.delete_selector("old-class")
```

### clear()

Удаляет все селекторы из коллекции.

Пример:

```python
css_input.selectors.clear()
```

### render(space=True)

Генерирует полный CSS блок со всеми селекторами.
Параметры:

- space (bool): Если True, добавляет форматирование с отступами. По умолчанию True
  Возвращает:
- str: Строка с CSS блоками внутри тега <style>

Пример:

```
css_output = css_input.render()
# <style>
# .container {
#   width: 100%;
#   padding: 20px;
# }
# #header {
#   background: #333;
#   color: white;
# }
# </style>
```

### **getattr**(name) -> CSSBase

Динамически создает и возвращает селектор при обращении к несуществующему атрибуту.

Параметры:

- name (str): Имя селектора

Возвращает:

- [CSSBase](CSSBase.md): Экземпляр CSSBase для указанного селектора

Пример:

```python
# Динамическое создание селектора
css_input.container.set_width("100%")
# Эквивалентно:
# css_input.add_selector("container").set_width("100%")
```

Примеры использования

```python
from LayoutML.base.css import CSSInput, CSSInline

css_inline = CSSInput()
css_inline.add_selector("body", type="tag", style="color:red;margin:0;margin2:0")
css_inline.body.set_text_align("left")

css_inline.add_selector("media (max-width: 600px)", type="media", style="color:red;margin:0;margin2:0")

css_inline:  = CSSInline(style="color:red;margin:0;margin2:0")
css_inline.set_text_align("left")

```
