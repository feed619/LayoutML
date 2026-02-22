# Header

`Header` - это специализированный класс для создания семантического HTML элемента <header>. Класс наследуется от [BaseElement](../base/BaseElement.md) и предназначен для создания шапок страниц или секций, содержащих вводную информацию, навигацию, логотипы, заголовки и другие элементы, обычно размещаемые в верхней части документа.
---

## Импорт

```python
from layoutML.elements import Header
```


## Наследование

- Родительский класс: BaseElement
- Тип элемента: header (не самозакрывающийся тег)
- Назначение: Создание семантических контейнеров для шапок страниц и секций

## Конструктор
### __init__(object_name=None, style=None, boolean_attributes=[], **kwargs)

Создаёт новый элемент шапки с указанными параметрами.

Параметры:

- object_name (опционально): Имя/идентификатор элемента
- style (опционально): CSS строка для inline стилей
- boolean_attributes (опционально): Список булевых атрибутов
- **kwargs: Дополнительные HTML атрибуты (id, class_, aria-* и т.д.)

Автоматически устанавливаемые свойства:

- Тег: header
- self_closing: False (не самозакрывающийся тег)
- object_type: "HeaderElement"

## Примеры:
```python
# Простая шапка
header = Header()

# Шапка с именем и классами
header = Header(
    object_name="pageHeader",
    class_="header main-header",
    id="siteHeader"
)

# Шапка с inline стилями
header = Header(
    style="background-color: #333; color: white; padding: 20px;",
    aria_label="Шапка сайта"
)
```