from enum import Enum


class FormTypes:
    """Все возможные типы полей ввода HTML"""

    # Текстовые поля
    TEXT = "text"
    PASSWORD = "password"
    EMAIL = "email"
    NUMBER = "number"
    TEL = "tel"
    URL = "url"
    SEARCH = "search"

    # Элементы выбора
    CHECKBOX = "checkbox"
    RADIO = "radio"
    SELECT = "select"
    DATALIST = "datalist"

    # Специальные поля
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

    # Кнопки
    SUBMIT = "submit"
    RESET = "reset"
    BUTTON = "button"
    IMAGE = "image"
