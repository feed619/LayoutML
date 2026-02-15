# Anchor

`Anchor` - это специализированный класс для создания HTML ссылок (<a>). Класс наследуется от [BaseElement](../base/BaseElement.md) и предоставляет удобный интерфейс для создания гиперссылок с автоматической установкой обязательных атрибутов href и target.

---

## Импорт

```python
from layoutML.elements import Anchor
```

## Наследование

- Родительский класс: BaseElement
- Тип элемента: a (не самозакрывающийся тег)
- Назначение: Создание гиперссылок для навигации

## Атрибуты класса

| Атрибут     | Тип | Описание                             | Значение по умолчанию |
| ----------- | --- | ------------------------------------ | --------------------- |
| href        | str | URL или якорь ссылки                 | Обязательный параметр |
| text        | str | Текст ссылки                         | Пустая строка         |
| target      | str | Способ открытия ссылки               | "\_self"              |
| object_type | str | Тип объекта (всегда "AnchorElement") | "AnchorElement"       |
| tag         | str | HTML тег (всегда "a")                | "a"                   |

## Конструктор

### **init**(href, text="", target="\_self", object_name=None, style=None, boolean_attributes=[], \*\*kwargs)

Создаёт новый элемент ссылки с указанными параметрами.

Параметры:

- href (str): URL или якорь, на который ведёт ссылка. Обязательный параметр
- text (str): Текст ссылки (отображается между тегами). По умолчанию пустая строка
- target (str): Способ открытия ссылки. По умолчанию "\_self". Возможные значения: "\_self", "\_blank", "\_parent", "\_top"
- object_name (опционально): Имя/идентификатор элемента
- style (опционально): CSS строка для inline стилей
- boolean_attributes (опционально): Список булевых атрибутов
- \*\*kwargs: Дополнительные HTML атрибуты (id, class\_, rel, download и т.д.)

Автоматически устанавливаемые свойства:

- Тег: a
- self_closing: False (не самозакрывающийся тег)
- object_type: "AnchorElement"
- href: URL ссылки
- text: текст ссылки
- target: способ открытия ссылки

## Примеры:

```python
# Простая ссылка
link = Anchor(href="https://example.com", text="Перейти на сайт")
# Ссылка с дополнительными атрибутами
link = Anchor(
    href="/about",
    text="О нас",
    target="_blank",
    class_="nav-link",
    id="aboutLink",
    rel="noopener noreferrer"
)

# Ссылка с inline стилями
link = Anchor(
    href="#section1",
    text="Перейти к разделу",
    style="color: blue; text-decoration: none;",
    class_="anchor-link"
)
```

## Примеры использования

### Внутренние ссылки

```python
# Ссылка на главную страницу
home_link = Anchor(href="/", text="Главная")

# Ссылка на страницу "О нас"
about_link = Anchor(href="/about", text="О нас", class_="nav-link")

# Ссылка на раздел внутри страницы
section_link = Anchor(href="#services", text="Наши услуги")
```

### Внешние ссылки

```python
# Внешняя ссылка, открывающаяся в новой вкладке
external_link = Anchor(
    href="https://google.com",
    text="Google",
    target="_blank",
    rel="noopener noreferrer"
)

# Ссылка с дополнительными атрибутами безопасности
secure_link = Anchor(
    href="https://example.com",
    text="Example",
    target="_blank",
    rel="noopener noreferrer nofollow"
)
```

### Ссылки-якоря

```python

# Ссылка наверх страницы
top_link = Anchor(href="#top", text="↑ Наверх")

# Ссылка на конкретный элемент
section_link = Anchor(href="#comments", text="Перейти к комментариям")
```

### Ссылки для скачивания

```python
# Ссылка на скачивание файла
download_link = Anchor(
    href="/files/document.pdf",
    text="Скачать PDF",
    download="",
    target="_blank"
)

# Ссылка с указанием имени файла
image_link = Anchor(
    href="/images/photo.jpg",
    text="Скачать фото",
    download="my_photo.jpg"
)
```

### Почтовые и телефонные ссылки

```python
# Email ссылка
email_link = Anchor(
    href="mailto:info@example.com",
    text="Написать нам"
)

# Телефонная ссылка
phone_link = Anchor(
    href="tel:+79991234567",
    text="+7 (999) 123-45-67"
)
```
