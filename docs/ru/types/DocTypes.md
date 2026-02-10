# DocTypes

`DocTypes` содержит константы, представляющие различные типы документов (DOCTYPE), которые поддерживаются в параметрах doctype класса Document.

---

## Назначение

Класс предоставляет набор предопределенных типов документов для использования при создании HTML/XML документов, обеспечивая типобезопасность и предотвращая ошибки в написании значений DOCTYPE.

## Импорт

```python
from layoutml.types import DocTypes
```

## Полный справочник констант

Константы

| Константа    | Значение       | Описание                                                                          |
| ------------ | -------------- | --------------------------------------------------------------------------------- |
| HTML         | "html"         | Стандартный HTML DOCTYPE (без версии)                                             |
| HTML5        | "html5"        | DOCTYPE для HTML5 (современный стандарт)                                          |
| XHTML        | "xhtml"        | Базовый DOCTYPE для XHTML                                                         |
| STRICT       | "strict"       | Строгий DOCTYPE (обычно для HTML 4.01 Strict или XHTML 1.0 Strict)                |
| TRANSITIONAL | "transitional" | Переходный DOCTYPE (обычно для HTML 4.01 Transitional или XHTML 1.0 Transitional) |

## Примеры использования

```python
# Импорт всего класса
from layoutml.types import DocTypes
from layoutml import Document
# Создание документа с HTML5 DOCTYPE
document = Document(doctype=DocTypes.HTML5)
# Создание документа со строгим XHTML DOCTYPE
document = Document(doctype=DocTypes.STRICT)
# Создание документа с переходным DOCTYPE
document = Document(doctype=DocTypes.TRANSITIONAL)
```
