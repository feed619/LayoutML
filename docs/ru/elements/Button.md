# Button

`Button` - это специализированный класс для создания HTML кнопок (<button>). Класс наследуется от [BaseElement](../base/BaseElement.md) и предоставляет упрощенный интерфейс для создания кнопок с текстом, стилями и атрибутами.

---

## Импорт

```python
from layoutML.elements import Button
```

## Наследование

- Родительский класс: BaseElement
- Тип элемента: button (не самозакрывающийся тег)
- Назначение: Создание интерактивных кнопок для форм, навигации и действий

## Конструктор

### **init**(text="", object_name=None, style=None, boolean_attributes=[], \*\*kwargs)

Создаёт новый элемент кнопки с указанным текстом и атрибутами.

Параметры:

- text (str): Текст кнопки (отображается между тегами). По умолчанию пустая строка
- object_name (опционально): Имя/идентификатор элемента
- style (опционально): CSS строка для inline стилей
- boolean_attributes (опционально): Список булевых атрибутов (disabled, readonly и т.д.)
- \*\*kwargs: Дополнительные HTML атрибуты (type, onclick, id, class\_ и т.д.)

Автоматически устанавливаемые свойства:

- Тег: button
- self_closing: False (не самозакрывающийся тег)
- object_type: "ButtonElement"
- text: текст кнопки

## Примеры:

## Пример 1: Базовые кнопки

```python
# Простая текстовая кнопка
simple_btn = Button(text="Нажми меня")

# Кнопка с типами
submit_btn = Button(
    text="Отправить",
    type="submit",
    class_="btn-submit"
)

reset_btn = Button(
    text="Сбросить",
    type="reset",
    class_="btn-reset"
)

# Кнопка с JavaScript обработчиком
action_btn = Button(
    text="Выполнить",
    onclick="doAction()",
    onmouseover="this.style.backgroundColor='yellow'"
)

# Кнопка с data атрибутами
data_btn = Button(
    text="Удалить",
    data_action="delete",
    data_id="123",
    data_confirm="Вы уверены?"
)
```

## Пример 2: Стилизованные кнопки с CSS

```python
# Создание кнопки с CSS классами
btn = Button(
    text="Стилизованная кнопка",
    object_name="fancyBtn",
    class_="btn btn-primary btn-large"
)

# Добавление inline стилей
btn.inline_styles.set_padding("10px 20px")\
                 .set_font_size("16px")\
                 .set_border_radius("5px")\
                 .set_cursor("pointer")

# Добавление CSS стилей через object_styles
btn.object_styles.set_background_color("#4CAF50")\
                 .set_color("white")\
                 .set_border("none")\
                 .set_transition("background-color 0.3s")

# Добавление эффектов через selectors_styles
btn.selectors_styles.add_selector("fancyBtn:hover")\
    .set_background_color("#45a049")

btn.selectors_styles.add_selector("fancyBtn:active")\
    .set_transform("scale(0.98)")
```
