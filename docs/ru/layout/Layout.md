# Layout

`Layout` - это специализированный контейнерный класс для создания гибких макетов (layout) на основе Flexbox. Наследуется от [BaseElement](../base/BaseElement.md) и предоставляет удобный интерфейс для управления компоновкой элементов с автоматической генерацией HTML и CSS.

---

## Наследование

- Родительский класс: BaseElement
- Тип элемента: div с Flexbox
- Назначение: Контейнер для упорядочивания дочерних элементов

## Атрибуты класса

| Атрибут       | Тип               | Описание                      | Наследование  |
| ------------- | ----------------- | ----------------------------- | ------------- |
| elements      | List[BaseElement] | Список дочерних элементов     | Новый         |
| is_stretched  | bool              | Флаг растянутого состояния    | Новый         |
| object_type   | str               | Тип объекта (всегда "Layout") | Переопределён |
| object_styles | CSSBase           | Стили layout (наследуется) Из | BaseElement   |
| tag           | str               | HTML тег (всегда "div") Из    | BaseElement   |

## Конструктор

### **init**(object_name=None, justify_content="center", align_items="center", \*\*kwargs)

Создаёт новый layout контейнер с настройками Flexbox.

Параметры:

- object_name (опционально): Имя/идентификатор layout
- justify_content (str): Выравнивание по главной оси. По умолчанию "center"
- align_items (str): Выравнивание по поперечной оси. По умолчанию "center"
- \*\*kwargs: Дополнительные атрибуты HTML элемента

Автоматически устанавливаемые свойства:

- Тег: div
- display: flex
- flex-direction: row
- flex-wrap: nowrap
- background: transparent

### Примеры:

```python
from layoutml.layout import Layout
# Простой layout
layout = Layout()
# Layout с именем и настройками выравнивания
header_layout = Layout(
    object_name="headerLayout",
    justify_content="space-between",
    align_items="center",
    class_="container"
)
# Layout с дополнительными атрибутами
main_layout = Layout(
    object_name="mainLayout",
    justify_content="flex-start",
    align_items="stretch",
    id="main",
    data_role="content"
)
```

## Основные методы

### Управление размерами

#### stretch(fullscreen: bool = True) -> "Layout"

Растягивает layout на весь экран или доступную ширину.

Параметры:

- fullscreen (bool): Если True - 100vw x 100vh, если False - 100% ширины

Пример:

```python
layout = Layout()
# На весь экран
layout.stretch()  # width: 100vw, height: 100vh
# На всю доступную ширину
layout.stretch(fullscreen=False)  # width: 100%, height: auto
```

#### unstretch() -> "Layout"

Отменяет растяжение layout.

Пример:

```python
layout = Layout()
layout.stretch()
print(layout.is_stretched)  # True
layout.unstretch()
print(layout.is_stretched)  # False
```

#### set_size(width: str = None, height: str = None) -> "Layout"

Устанавливает конкретные размеры layout.

Параметры:

- width (опционально): Ширина (например, "500px", "50%", "100vw")
- height (опционально): Высота (например, "300px", "100vh")

Пример:

```python
layout = Layout()
# Фиксированные размеры
layout.set_size(width="800px", height="600px")
# Процентные размеры
layout.set_size(width="90%", height="auto")
# Автоматическое определение stretched состояния
layout.set_size(width="100vw")  # is_stretched становится True
```

### Управление элементами

#### add_element(element: Any) -> "Layout"

Добавляет один элемент в layout.

Пример:

```python
layout = Layout()
button = BaseElement(tag="button", object_name="myButton")
layout.add_element(button)
print(len(layout))  # 1
```

#### add_elements(\*elements: Any) -> "Layout"

Добавляет несколько элементов одновременно.

Пример:

```python
layout = Layout()
button1 = BaseElement(tag="button", object_name="btn1")
button2 = BaseElement(tag="button", object_name="btn2")
div = BaseElement(tag="div", object_name="container")
layout.add_elements(button1, button2, div)
print(len(layout))  # 3
```

#### clear() -> "Layout"

Очищает все элементы из layout.

Пример:

```python
layout = Layout()
layout.add_elements(button1, button2)
print(len(layout))  # 2
layout.clear()
print(len(layout))  # 0
```

#### insert_element(index: int, element: Any) -> "Layout"

Вставляет элемент на указанную позицию.

Пример:

```python
layout = Layout()
layout.add_elements(button1, button3)  # [btn1, btn3]
layout.insert_element(1, button2)      # [btn1, btn2, btn3]
```

#### remove_element(index: int) -> "Layout"

Удаляет элемент по указанному индексу.

Пример:

```python

layout = Layout()
layout.add_elements(button1, button2, button3)
layout.remove_element(1)  # Удаляет button2
```

### Генерация HTML и CSS

#### get_html() -> str

Генерирует HTML строку layout со всеми дочерними элементами.
Особенности:

- Рекурсивно вызывает get_html() у дочерних элементов
- Добавляет отступы для форматирования
- Возвращает полную структуру с вложенностью

Пример:

```python
layout = Layout(object_name="mainLayout")
layout.add_element(BaseElement(tag="p", object_name="text").get_html(content="Hello"))

html = layout.get_html()
# Результат:
# <div class="mainLayout" >
#     <p class="text" >Hello</p>
# </div>
```

#### get_styles() -> dict

Собирает CSS стили layout и всех дочерних элементов.

Особенности:

- Рекурсивно собирает стили из дочерних элементов
- Объединяет все стили в один словарь
- Автоматически обрабатывает вложенные layouts

Пример:

```python
layout = Layout(object_name="container")
layout.object_styles.set_background_color("red")

child = BaseElement(tag="div", object_name="child")
child.object_styles.set_width("100px")

layout.add_element(child)

styles = layout.get_styles()
# Результат: {
#   '.container': 'background-color:red;...',
#   '.child': 'width:100px;'
# }
```

### Специальные методы Python

#### **len**() -> int

Возвращает количество элементов в layout.

```python
layout = Layout()
layout.add_elements(btn1, btn2, btn3)
print(len(layout))  # 3
```

#### **getitem**(index: int) -> Any

Получает элемент по индексу.

```python
layout = Layout()
layout.add_elements(btn1, btn2, btn3)
second_element = layout[1]  # btn2
```

#### **setitem**(index: int, element: Any) -> None

Заменяет элемент по указанному индексу.

```python
layout = Layout()
layout.add_elements(btn1, btn2, btn3)
layout[1] = new_button  # Заменяет btn2 на new_button
```

#### **delitem**(index: int) -> None

Удаляет элемент по указанному индексу.

```python
layout = Layout()
layout.add_elements(btn1, btn2, btn3)
del layout[1]  # Удаляет btn2
```
