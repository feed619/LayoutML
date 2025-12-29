
from enum import Enum


class TextField(str, Enum):
    """Текстовые поля:
    text: Обычное текстовое поле
    password: Поле для пароля
    email: Поле для email адреса
    number: Числовое поле
    tel: Поле для телефона
    url: Поле для URL
    search: Поле поиска"""

    TEXT = "text"
    PASSWORD = "password"
    EMAIL = "email"
    NUMBER = "number"
    TEL = "tel"
    URL = "url"
    SEARCH = "search"


class SelectionElements(str, Enum):
    """Элементы выбора:
    checkbox: Флажок
    radio: Радиокнопка
    select: Выпадающий список (требует options)
    datalist: Список подсказок
    """

    CHECKBOX = "checkbox"
    RADIO = "radio"
    SELECT = "select"
    DATALIST = "datalist"


class SpecialFields(str, Enum):
    """Специальные поля:
    date: Выбор даты
    time: Выбор времени
    datetime-local: Дата и время
    month: Месяц и год
    week: Неделя года
    color: Выбор цвета
    range: Ползунок
    file: Загрузка файлов
    hidden: Скрытое поле
    textarea: Многострочный текст
    """

    DATE = "date"
    TIME = "time"
    DATETIME_LOCAL = "datetime-local"
    MONTH = "month"
    WEEK = "week"
    COLOR = "color"
    RANGE = "range"
    FILE = "file"
    HIDDEN = "hidden"
    TEXTAREA = "textarea"

class Buttons(str, Enum):
    """Кнопки:
    submit: Кнопка отправки
    reset: Кнопка сброса
    button: Обычная кнопка
    image: Кнопка с изображением
    """

    SUBMIT = "submit"
    RESET = "reset"
    BUTTON = "button"
    IMAGE = "image"

