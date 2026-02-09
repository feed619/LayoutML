# VerticalLayout

`VerticalLayout` - это специализированный класс для создания вертикальных макетов с использованием Flexbox. Наследуется от базового класса [Layout](Layout.md) и предназначен для управления элементами, расположенными в колонку. Идеально подходит для создания форм, списков, навигационных панелей и других интерфейсов с вертикальной структурой.

---

## Наследование

- Родительский класс: Layout
- Направление: Вертикальное (flex-direction: column)
- Специализация: Управление элементами в колонку с возможностью реверса направления
- Дополнительно: Автоматически устанавливает box-sizing: border-box для корректного расчета размеров

## Атрибуты класса

| Атрибут                         | Тип | Описание                              | Наследование                             |
| ------------------------------- | --- | ------------------------------------- | ---------------------------------------- |
| object_type                     | str | Тип объекта (всегда "VerticalLayout") | Переопределён                            |
| object_styles["flex-direction"] | str | Направление элементов                 | Наследуется, но фиксируется как "column" |
| object_styles["box-sizing"]     | str | Модель расчета размеров               | Новый                                    |
| Все остальные атрибуты          |     | Наследуются от Layout                 | Из Layout                                |

## Конструктор

### **init**(justify_content="center", align_items="center", object_name=None, \*\*kwargs)

Создаёт новый вертикальный layout с указанными настройками выравнивания.

Параметры:

- justify_content (str): Выравнивание по главной оси (вертикальной). По умолчанию "center"
- align_items (str): Выравнивание по поперечной оси (горизонтальной). По умолчанию "center"
- object_name (опционально): Имя/идентификатор layout
- \*\*kwargs: Дополнительные атрибуты HTML элемента

Автоматически устанавливаемые свойства:

- Наследует все свойства Layout
- flex-direction: column (вертикальное направление)
- box-sizing: border-box (для корректного расчета размеров)
- object_type: "VerticalLayout"

Важно: В вертикальном layout justify_content работает по вертикальной оси, а align_items - по горизонтальной.

Примеры:

```python
# Простой вертикальный layout
v_layout = VerticalLayout()

# Вертикальный layout с настраиваемым выравниванием
sidebar = VerticalLayout(
    object_name="sidebar",
    justify_content="flex-start",  # Элементы сверху
    align_items="stretch",         # Элементы растягиваются по ширине
    class_="navigation-sidebar"
)

# Layout с дополнительными атрибутами
form_container = VerticalLayout(
    object_name="signupForm",
    justify_content="center",
    align_items="stretch",
    id="signup-form",
    data_role="form-container"
)
```

## Основные методы

### set_reverse(reverse: bool = True) -> "VerticalLayout"

Устанавливает обратное направление расположения элементов в колонке.

Параметры:

- reverse (bool): Если True - элементы располагаются снизу вверх (column-reverse). Если False - сверху вниз (column). По умолчанию True

Возвращает:

- Сам объект VerticalLayout для цепочки вызовов

Примеры:

```python
layout = VerticalLayout()
# Обычное направление (сверху вниз)
layout.set_reverse(False)
print(layout.object_styles["flex-direction"])  # "column"

# Обратное направление (снизу вверх)
layout.set_reverse(True)
print(layout.object_styles["flex-direction"])  # "column-reverse"
```

## Наследованные методы

VerticalLayout наследует все методы из Layout, включая:

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
