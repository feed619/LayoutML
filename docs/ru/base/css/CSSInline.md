# CSSInline

`CSSInline` - это специализированный класс, наследующий от [CSSBase](CSSBase.md), предназначенный для генерации inline стилей HTML элементов. Класс предоставляет удобный способ создания строки CSS стилей в формате, пригодном для вставки в HTML атрибут style.

---

## Импорт

```python
from LayoutML.base.css import CSSInline
```

## Наследование

- Родительский класс: [CSSBase](CSSBase.md)
- Наследует все методы из [CSSBase](CSSBase.md)
- Добавляет специальные методы для работы с inline стилями

## Конструктор

### **init**(style=None)

Создаёт новый экземпляр CSSInline для работы с inline стилями.

Параметры:

- style (опционально): CSS строка стилей для парсинга

Примеры:

```python
# Создание пустого объекта
css = CSSInline()
# Создание с начальными стилями
css = CSSInline(style="color: red; font-size: 16px;")
# Наследование всех методов CSSBase
css.set_width("100px").set_background_color("blue")
```

## Основные методы

### copy(copy_element: "CSSInline") -> "CSSInline"

Создает глубокую копию объекта CSSInline.

Параметры:

- copy_element (CSSInline): Существующий объект для копирования (опционально)

Возвращает:

- Копию текущего объекта CSSInline

Пример:

```python
# Создание исходного объекта
original = CSSInline(style="color: red; padding: 10px;")
original.set_margin("20px")
# Создание копии
copy_obj = original.copy()
# Изменение копии не влияет на оригинал
copy_obj.set_color("blue")
copy_obj.set_margin("30px")
print(original.get_styles_string())  # 'color:red;padding:10px;margin:20px;'
print(copy_obj.get_styles_string())  # 'color:blue;padding:10px;margin:30px;'
```

### get_styles_str(space=False) -> str

Генерирует готовую строку атрибута style для HTML тега.

Параметры:

- space (bool): Если True, форматирует с пробелами и переносами строк внутри атрибута

Возвращает:

- Строку атрибута style или пустую строку, если стилей нет

Примеры:

```python
css = CSSInline()
css.set_color("red").set_font_size("16px")
# Без форматирования
print(css.get_styles_str())
# Результат: 'style="color:red;font-size:16px;"'
# С форматированием
print(css.get_styles_str(space=True))
# Результат: 'style="  color: red;\n  font-size: 16px;"'
# Пустые стили
css_empty = CSSInline()
print(css_empty.get_styles_str())
# Результат: ""
```

## Наследованные методы

CSSInline наследует все методы из CSSBase, включая:
Категории методов:

- Блочная модель: set_width(), set_height(), set_margin(), и т.д.
- Позиционирование: set_position(), set_top(), set_left(), и т.д.
- Flexbox: set_flex_direction(), set_justify_content(), и т.д.
- Grid: set_grid_template_columns(), set_grid_area(), и т.д.
- Текст: set_color(), set_font_family(), set_text_align(), и т.д.
- CSS переменные: set_css_variable(), get_css_variable()
- Утилитные методы: add_style(), remove_style(), clear_styles(), и т.д.
