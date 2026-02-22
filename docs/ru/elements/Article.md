# Article

`Article` - это специализированный класс для создания семантического HTML элемента <article>. Класс наследуется от [BaseElement](../base/BaseElement.md) и предназначен для создания самодостаточных, независимых частей контента, таких как статьи в блоге, новостные посты, комментарии или любые другие автономные фрагменты информации.

---

## Импорт

```python
from layoutML.elements import Article
```

Наследование

- Родительский класс: BaseElement
- Тип элемента: article (не самозакрывающийся тег)
- Назначение: Создание семантических контейнеров для независимого контента

## Конструктор

### **init**(object_name=None, style=None, boolean_attributes=[], \*\*kwargs)

Создаёт новый элемент статьи с указанными параметрами.

Параметры:

- object_name (опционально): Имя/идентификатор элемента
- style (опционально): CSS строка для inline стилей
- boolean_attributes (опционально): Список булевых атрибутов
- \*_kwargs: Дополнительные HTML атрибуты (id, class\_, aria-_ и т.д.)

Автоматически устанавливаемые свойства:

- Тег: article
- self_closing: False (не самозакрывающийся тег)
- object_type: "ArticleElement"

Примеры:

```python
# Простая статья
article = Article()

# Статья с именем и классами
article = Article(
    object_name="blogPost",
    class_="post featured",
    id="post123"
)

# Статья с inline стилями
article = Article(
    style="margin-bottom: 20px; padding: 15px; border: 1px solid #ddd;",
    aria_label="Статья о веб-разработке"
)
```

## Примеры

```python
article = Article(object_name="styledPost")

# Добавление inline стилей
article.inline_styles.set_margin_bottom("30px")\
                     .set_padding("20px")\
                     .set_background_color("#f9f9f9")\
                     .set_border_radius("8px")\
                     .set_box_shadow("0 2px 8px rgba(0,0,0,0.1)")

# Добавление CSS стилей через object_styles
article.object_styles.set_font_family("Arial, sans-serif")\
                     .set_line_height("1.6")\
                     .set_color("#333")

# Добавление содержимого
article.get_html(content="<h2>Заголовок</h2><p>Содержимое...</p>")
```
