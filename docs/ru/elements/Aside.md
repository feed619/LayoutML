# Aside

`Aside` - это специализированный класс для создания семантического HTML элемента <aside>. Класс наследуется от [BaseElement](../base/BaseElement.md) и предназначен для создания боковых панелей, которые содержат контент, косвенно связанный с основным содержимым страницы (сайдбары, блоки с дополнительной информацией, рекламные блоки, списки связанных ссылок и т.д.).

---

## Импорт

```python
from layoutML.elements import Aside
```

## Наследование

- Родительский класс: BaseElement
- Тип элемента: aside (не самозакрывающийся тег)
- Назначение: Создание семантических контейнеров для дополнительного контента

## Конструктор

### **init**(object_name=None, style=None, boolean_attributes=[], \*\*kwargs)

Создаёт новый элемент боковой панели с указанными параметрами.

Параметры:

- object_name (опционально): Имя/идентификатор элемента
- style (опционально): CSS строка для inline стилей
- boolean_attributes (опционально): Список булевых атрибутов
- \*_kwargs: Дополнительные HTML атрибуты (id, class\_, aria-_ и т.д.)

Автоматически устанавливаемые свойства:

- Тег: aside
- self_closing: False (не самозакрывающийся тег)
- object_type: "AsideElement"

Примеры:

```python
# Простая боковая панель
aside = Aside()

# Боковая панель с именем и классами
aside = Aside(
    object_name="sidebar",
    class_="sidebar right-sidebar",
    id="mainSidebar"
)

# Боковая панель с inline стилями
aside = Aside(
    style="width: 300px; padding: 20px; background-color: #f5f5f5;",
    aria_label="Дополнительная информация"
)
```

### Стилизованная боковая панель

```python
sidebar = Aside(object_name="styledSidebar")

# Inline стили
sidebar.inline_styles.set_width("280px")\
                     .set_padding("20px")\
                     .set_background_color("#f8f9fa")\
                     .set_border_radius("8px")\
                     .set_box_shadow("0 2px 10px rgba(0,0,0,0.1)")

# CSS стили через object_styles
sidebar.object_styles.set_font_family("Arial, sans-serif")\
                     .set_color("#555")\
                     .set_line_height("1.6")

# Добавление содержимого
sidebar.get_html(content="""
    <h3 style="margin-top: 0; color: #333;">Интересное</h3>
    <p>Здесь могла быть ваша реклама или полезная информация.</p>
""")
```
