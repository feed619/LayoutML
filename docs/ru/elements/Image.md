# Image

`Image` - это специализированный класс для создания HTML элемента изображения <img>. Класс наследуется от [BaseElement](../base/BaseElement.md) и предоставляет удобный интерфейс для вставки изображений с автоматической установкой обязательных атрибутов src и alt.

---

## Импорт

```python
from layoutML.elements import Image
```

## Наследование

- Родительский класс: BaseElement
- Тип элемента: img (самозакрывающийся тег)
- Назначение: Вставка изображений в HTML документ

## Конструктор

### **init**(src, alt="", object_name=None, style=None, boolean_attributes=[], \*\*kwargs)

Создаёт новый элемент изображения с указанными параметрами.

## Параметры:

- src (str): Путь к файлу изображения. Обязательный параметр
- alt (str): Альтернативный текст для изображения. По умолчанию пустая строка
- object_name (опционально): Имя/идентификатор элемента
- style (опционально): CSS строка для inline стилей
- boolean_attributes (опционально): Список булевых атрибутов
- \*\*kwargs: Дополнительные HTML атрибуты (width, height, loading, decoding и т.д.)

## Автоматически устанавливаемые свойства:

- Тег: img
- self_closing: True (самозакрывающийся тег)
- object_type: "ImageElement"
- src: путь к изображению
- alt: альтернативный текст

## Примеры:

```python
# Простое изображение
img = Image(src="photo.jpg", alt="Фотография")

# Изображение с дополнительными атрибутами
img = Image(
    src="images/logo.png",
    alt="Логотип компании",
    object_name="companyLogo",
    class_="logo",
    width="200",
    height="100",
    loading="lazy"
)

# Изображение с inline стилями
img = Image(
    src="banner.jpg",
    alt="Баннер",
    style="border-radius: 8px; box-shadow: 0 2px 10px rgba(0,0,0,0.1);",
    decoding="async"
)
```

## Примеры использования

### Базовые изображения

```python
# Обычное изображение
img1 = Image(src="photo.jpg", alt="Пейзаж")

# Изображение с размерами
img2 = Image(
    src="avatar.png",
    alt="Аватар пользователя",
    width="100",
    height="100"
)

# Изображение с классами
img3 = Image(
    src="banner.jpg",
    alt="Рекламный баннер",
    class_="banner responsive",
    id="mainBanner"
)
```

### Изображения с ленивой загрузкой

```python
# Ленивая загрузка для оптимизации производительности
lazy_img = Image(
    src="large-image.jpg",
    alt="Большое изображение",
    loading="lazy",
    decoding="async",
    fetchpriority="low"
)

# Критическое изображение (загружается немедленно)
hero_img = Image(
    src="hero.jpg",
    alt="Главное изображение",
    loading="eager",
    fetchpriority="high",
    decoding="sync"
)
```

### Адаптивные изображения

```python
# Изображение с srcset для разных разрешений
responsive_img = Image(
    src="image-medium.jpg",  # Запасной вариант
    alt="Адаптивное изображение",
    srcset="""
        image-small.jpg 300w,
        image-medium.jpg 600w,
        image-large.jpg 900w,
        image-xlarge.jpg 1200w
    """,
    sizes="(max-width: 600px) 300px, (max-width: 900px) 600px, 900px"
)

# Изображение с разными форматами
webp_img = Image(
    src="image.jpg",
    alt="Изображение в современном формате",
    srcset="image.webp, image.jpg"
)
```

### Стилизованные изображения

````python
# Изображение с CSS стилями
styled_img = Image(
    src="profile.jpg",
    alt="Фото профиля",
    class_="profile-photo"
)

# Inline стили
styled_img.inline_styles.set_border_radius("50%")\
                         .set_border("3px solid #007bff")\
                         .set_box_shadow("0 4px 12px rgba(0,0,0,0.15)")

# CSS стили через object_styles
styled_img.object_styles.set_width("150px")\
                         .set_height("150px")\
                         .set_object_fit("cover")

# Hover эффект через selectors_styles
styled_img.selectors_styles.add_selector("profile-photo:hover")\
    .set_transform("scale(1.05)")\
    .set_transition("transform 0.3s")
    ```
````
