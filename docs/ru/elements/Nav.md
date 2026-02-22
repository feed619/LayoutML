# Nav

`Nav` - это специализированный класс для создания семантического HTML элемента <nav>. Класс наследуется от [BaseElement](../base/BaseElement.md) и предназначен для создания навигационных блоков, содержащих ссылки для навигации по сайту или по странице.

---

## Импорт

```python
from layoutML.elements import Nav
```

## Наследование

- Родительский класс: BaseElement
- Тип элемента: nav (не самозакрывающийся тег)
- Назначение: Создание семантических контейнеров для навигационных элементов

## Конструктор

### **init**(object_name=None, style=None, boolean_attributes=[], \*\*kwargs)

Создаёт новый элемент навигации с указанными параметрами.

### Параметры:

- object_name (опционально): Имя/идентификатор элемента
- style (опционально): CSS строка для inline стилей
- boolean_attributes (опционально): Список булевых атрибутов
- \*_kwargs: Дополнительные HTML атрибуты (id, class\_, aria-_ и т.д.)

### Автоматически устанавливаемые свойства:

- Тег: nav
- self_closing: False (не самозакрывающийся тег)
- object_type: "NavElement"

### Примеры:

```python
# Простой навигационный блок
nav = Nav()

# Навигация с именем и классами
nav = Nav(
    object_name="mainNav",
    class_="navigation main-nav",
    id="siteNavigation"
)

# Навигация с inline стилями
nav = Nav(
    style="background-color: #333; padding: 15px;",
    aria_label="Основная навигация по сайту"
)
```
