# Section

`Section` - это специализированный класс для создания семантического HTML элемента <section>. Класс наследуется от [BaseElement](../base/BaseElement.md) и предназначен для создания тематических групп контента, обычно с собственным заголовком, которые являются частью более крупного документа или приложения.

---

## Импорт

```python
from layoutML.elements import Section
```

## Наследование

- Родительский класс: BaseElement
- Тип элемента: section (не самозакрывающийся тег)
- Назначение: Создание семантических контейнеров для тематически связанного контента

## Конструктор

### **init**(object_name=None, style=None, boolean_attributes=[], \*\*kwargs)

Создаёт новый элемент секции с указанными параметрами.

### Параметры:

- object_name (опционально): Имя/идентификатор элемента
- style (опционально): CSS строка для inline стилей
- boolean_attributes (опционально): Список булевых атрибутов
- \*_kwargs: Дополнительные HTML атрибуты (id, class\_, aria-_ и т.д.)

### Автоматически устанавливаемые свойства:

- Тег: section
- self_closing: False (не самозакрывающийся тег)
- object_type: "SectionElement"

### Примеры:

```python
# Простая секция
section = Section()

# Секция с именем и классами
section = Section(
    object_name="featuresSection",
    class_="features highlight",
    id="mainFeatures"
)

# Секция с inline стилями
section = Section(
    style="background-color: #f8f9fa; padding: 40px 20px;",
    aria_label="Основные преимущества"
)
```
