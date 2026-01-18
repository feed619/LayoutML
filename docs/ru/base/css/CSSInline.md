# CSSInline

`CSSInline` - это специализированный класс, наследующий от [CSSBase](CSSBase.md), предназначенный для генерации inline стилей HTML элементов. Класс предоставляет удобный способ создания строки CSS стилей в формате, пригодном для вставки в HTML атрибут style.

---

## Импорт

```python
from LayoutML.base.css import CSSInline
```

## Наследование

CSSInline наследует все методы и свойства от родительского класса [CSSBase](CSSBase.md), добавляя специализированный функционал для рендеринга inline стилей.

## Конструктор

### **init**(self, style=None)

Параметры:

| Параметр | Тип | По умолчанию | Описание                                                                   |
| -------- | --- | ------------ | -------------------------------------------------------------------------- |
| style    | str | None         | Начальная строка CSS стилей. Формат: "property: value; property2: value2;" |

Пример

```python
# Пустой экземпляр
css_inline = CSSInline()
# С начальными стилями
css_inline = CSSInline(style="color: red; font-size: 16px; margin: 10px;")
```

## Методы

### render(space=False)

Генерирует строку inline стилей в формате HTML атрибута.

Параметры:

- space (bool, optional): Если True, добавляет форматирование с пробелами и переносами строк. По умолчанию False.

Возвращает:

- str: Строка в формате style="property:value; property2:value2;"

Примеры:

```python
# Создание экземпляра
css = CSSInline()
# Установка стилей
css.set_color("red")
.set_font_size("16px")
.set_margin("10px")
# Рендеринг без форматирования
result = css.render()
# style="color:red;font-size:16px;margin:10px;"
# Рендеринг с форматированием
result_formatted = css.render(space=True)
# style="
# color:red;
# font-size:16px;
# margin:10px;
# "
```

### Унаследованные методы

CSSInline наследует все методы из [CSSBase](CSSBase.md)
