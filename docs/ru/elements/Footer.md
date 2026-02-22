# Footer

`Footer` - это специализированный класс для создания семантического HTML элемента <footer>. Класс наследуется от [BaseElement](../base/BaseElement.md) и предназначен для создания подвалов страниц или секций, содержащих информацию об авторе, копирайт, ссылки на связанные документы, контактную информацию и другие элементы, обычно размещаемые в нижней части документа.

---

## Импорт

```python
from layoutML.elements import Footer
```

Наследование

- Родительский класс: BaseElement
- Тип элемента: footer (не самозакрывающийся тег)
- Назначение: Создание семантических контейнеров для подвалов страниц и секций

## Конструктор

### **init**(object_name=None, style=None, boolean_attributes=[], \*\*kwargs)

Создаёт новый элемент подвала с указанными параметрами.

Параметры:

- object_name (опционально): Имя/идентификатор элемента
- style (опционально): CSS строка для inline стилей
- boolean_attributes (опционально): Список булевых атрибутов
- \*_kwargs: Дополнительные HTML атрибуты (id, class\_, aria-_ и т.д.)

Автоматически устанавливаемые свойства:

- Тег: footer
- self_closing: False (не самозакрывающийся тег)
- object_type: "FooterElement"

## Примеры:

```python
# Простой подвал
footer = Footer()

# Подвал с именем и классами
footer = Footer(
    object_name="pageFooter",
    class_="footer main-footer",
    id="siteFooter"
)

# Подвал с inline стилями
footer = Footer(
    style="background-color: #333; color: white; padding: 20px;",
    aria_label="Подвал сайта"
)
```

### Стилизованный подвал

```python
footer = Footer(object_name="styledFooter")

# Inline стили
footer.inline_styles.set_background_color("#2c3e50")\
                     .set_color("white")\
                     .set_padding("40px 20px 20px")\
                     .set_margin_top("50px")\
                     .set_font_family("Arial, sans-serif")

# CSS стили через object_styles
footer.object_styles.set_text_align("center")\
                     .set_border_top("3px solid #3498db")

""")
```
