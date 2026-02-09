# HorizontalLayout

`HorizontalLayout` - это специализированный класс для создания горизонтальных макетов с использованием Flexbox. Наследуется от базового класса [Layout](Layout.md) и предоставляет дополнительные методы для управления горизонтальным расположением элементов.

---

## Наследование

- Родительский класс: Layout
- Направление: Горизонтальное (flex-direction: row)
- Специализация: Управление элементами в строку с возможностью реверса направления

## Атрибуты класса

| Атрибут                         | Тип | Описание                                | Наследование                          |
| ------------------------------- | --- | --------------------------------------- | ------------------------------------- |
| object_type                     | str | Тип объекта (всегда "HorizontalLayout") | Переопределён                         |
| object_styles["flex-direction"] | str | Направление элементов (row/row-reverse) | Наследуется, но фиксируется как "row" |
| Все остальные атрибуты          |     | Наследуются от Layout Из                | Layout                                |

## Конструктор

### **init**(justify_content="center", align_items="center", object_name=None, \*\*kwargs)

Создаёт новый горизонтальный layout с указанными настройками выравнивания.

Параметры:

- justify_content (str): Выравнивание по главной оси (горизонтальной). По умолчанию "center"
- align_items (str): Выравнивание по поперечной оси (вертикальной). По умолчанию "center"
- object_name (опционально): Имя/идентификатор layout
- \*\*kwargs: Дополнительные атрибуты HTML элемента

Автоматически устанавливаемые свойства:

- Наследует все свойства Layout
- flex-direction: row (горизонтальное направление)
- object_type: "HorizontalLayout"

Примеры:

```python
# Простой горизонтальный layout
h_layout = HorizontalLayout()

# Горизонтальный layout с настраиваемым выравниванием
nav_bar = HorizontalLayout(
    object_name="navbar",
    justify_content="space-between",
    align_items="center",
    class_="navigation"
)
# Layout с дополнительными атрибутами
toolbar = HorizontalLayout(
    object_name="mainToolbar",
    justify_content="flex-start",
    align_items="stretch",
    id="toolbar",
    data_role="toolbar"
)
```

## Основные методы

### set_reverse(reverse: bool = True) -> "HorizontalLayout"

Устанавливает обратное направление расположения элементов.

Параметры:

- reverse (bool): Если True - элементы располагаются справа налево (row-reverse). Если False - слева направо (row). По умолчанию True

Возвращает:

- Сам объект HorizontalLayout для цепочки вызовов

Примеры:

```python
layout = HorizontalLayout()
# Обычное направление (слева направо)
layout.set_reverse(False)
print(layout.object_styles["flex-direction"]) # "row"
# Обратное направление (справа налево)
layout.set_reverse(True)
print(layout.object_styles["flex-direction"]) # "row-reverse"
```

## Наследованные методы

HorizontalLayout наследует все методы из Layout, включая:

### Управление размерами:

- stretch(fullscreen: bool = True) -> "Layout" - растягивает layout
- unstretch() -> "Layout" - отменяет растяжение
- set_size(width: str = None, height: str = None) -> "Layout" - устанавливает размеры

### Управление элементами:

- add_element(element: Any) -> "Layout" - добавляет один элемент
- add_elements(\*elements: Any) -> "Layout" - добавляет несколько элементов
- clear() -> "Layout" - очищает все элементы
- insert_element(index: int, element: Any) -> "Layout" - вставляет элемент
- remove_element(index: int) -> "Layout" - удаляет элемент

### Генерация:

- get_html() -> str - генерирует HTML
- get_styles() -> dict - собирает CSS стили

### Специальные методы:

- **len**() -> int - количество элементов
- **getitem**(index: int) -> Any - получение элемента по индексу
- **setitem**(index: int, element: Any) -> None - установка элемента
- **delitem**(index: int) -> None - удаление элемента
