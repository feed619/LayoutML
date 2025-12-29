from .HTMLElement import HTMLElement


class FormElement(HTMLElement):
    """
    Класс для создания элементов HTML форм с расширенными возможностями.

    Наследует все возможности HTMLElement и добавляет специфические атрибуты форм.
    Поддерживает все стандартные атрибуты элементов ввода HTML5.

    Attributes
    ----------
    _type : str
        Тип элемента формы (text, email, password, checkbox и т.д.)
    _name : str, optional
        Имя элемента формы (используется при отправке формы)
    _value : any, optional
        Значение элемента
    _placeholder : str, optional
        Текст-подсказка в пустом поле ввода
    _required : bool
        Обязательное ли поле для заполнения
    _readonly : bool
        Только для чтения (пользователь не может редактировать)
    _disabled : bool
        Отключен ли элемент (нельзя взаимодействовать)
    _maxlength : int, optional
        Максимальная длина текста в символах
    _minlength : int, optional
        Минимальная длина текста в символах
    _max : any, optional
        Максимальное значение (для чисел, дат, времени)
    _min : any, optional
        Минимальное значение (для чисел, дат, времени)
    _step : any, optional
        Шаг изменения значения (для чисел, дат, времени, range)
    _pattern : str, optional
        Регулярное выражение для валидации текста
    _autofocus : bool
        Автофокус при загрузке страницы
    _multiple : bool
        Разрешить множественный выбор (для select и file)
    _checked : bool
        Выбран ли элемент (для checkbox/radio)
    _autocomplete : str
        Автозаполнение (on/off или другие значения)
    _size : int, optional
        Видимая ширина текстового поля в символах
    _accept : str, optional
        Типы файлов, которые можно загрузить (для type="file")
    _capture : str, optional
        Способ захвата медиа на мобильных устройствах (для type="file")
    _dirname : str, optional
        Имя поля для отправки направления текста (ltr/rtl)
    _form : str, optional
        ID формы, с которой связан элемент (даже если он вне тега <form>)
    _formaction : str, optional
        Альтернативный URL для отправки формы (для type="submit"/"image")
    _formenctype : str, optional
        Способ кодирования данных формы при отправке
    _formmethod : str, optional
        HTTP метод для отправки формы (GET/POST/PUT/DELETE)
    _formnovalidate : bool
        Отключение валидации формы при отправке
    _formtarget : str, optional
        Целевое окно/фрейм для результата отправки формы
    _height : int, optional
        Высота изображения в пикселях (для type="image")
    _width : int, optional
        Ширина изображения в пикселях (для type="image")
    _list : str, optional
        ID элемента <datalist> для автозаполнения
    _alt : str, optional
        Альтернативный текст для изображения (обязателен для type="image")
    _src : str, optional
        URL источника изображения (обязателен для type="image")
    _rows : int, optional
        Количество видимых строк текста (для textarea)
    _cols : int, optional
        Количество видимых колонок текста (для textarea)
    _wrap : str
        Определяет, как текст переносится в textarea (soft/hard/off)
    _options : list
        Список опций для элементов select и datalist
    _selected : any, optional
        Выбранное значение/значения для элемента select
    _text : str
        Текст внутри элемента textarea

    Examples
    --------
    >>> # Создание текстового поля
    >>> text_input = FormElement(
    ...     type="text",
    ...     name="username",
    ...     placeholder="Введите имя",
    ...     required=True,
    ...     maxlength=50
    ... )
    >>>
    >>> # Создание поля email
    >>> email_input = FormElement(
    ...     type="email",
    ...     name="email",
    ...     placeholder="user@example.com",
    ...     required=True,
    ...     pattern="[a-z0-9._%+-]+@[a-z0-9.-]+\\.[a-z]{2,}$"
    ... )
    >>>
    >>> # Создание поля загрузки файлов
    >>> file_input = FormElement(
    ...     type="file",
    ...     name="document",
    ...     accept=".pdf,.docx",
    ...     multiple=True
    ... )
    """

    def __init__(self, **kwargs):
        """
        Инициализирует элемент формы.

        Parameters
        ----------
        **kwargs : dict
            Атрибуты элемента формы в дополнение к наследуемым от HTMLElement:

            Основные атрибуты:
            - type: Тип элемента (text, password, email, number, checkbox, radio и т.д.)
            - name: Имя элемента для отправки на сервер
            - value: Значение по умолчанию
            - placeholder: Подсказка в пустом поле
            - required: Обязательное поле
            - readonly: Только чтение
            - disabled: Отключенное поле
            - maxlength: Максимальная длина текста
            - minlength: Минимальная длина текста
            - max: Максимальное значение (для чисел, дат)
            - min: Минимальное значение (для чисел, дат)
            - step: Шаг изменения значения
            - pattern: Регулярное выражение для валидации
            - autofocus: Автофокус при загрузке
            - multiple: Множественный выбор (для select и file)
            - checked: Выбрано (для checkbox/radio)
            - autocomplete: Автозаполнение (on/off)

            Дополнительные атрибуты:
            - size: Видимая ширина поля в символах
            - accept: Разрешенные типы файлов для загрузки
            - capture: Способ захвата медиа (user/environment)
            - dirname: Имя поля для направления текста
            - form: ID связанной формы
            - formaction: Альтернативный URL отправки
            - formenctype: Способ кодирования данных (multipart/form-data и т.д.)
            - formmethod: HTTP метод отправки
            - formnovalidate: Отключить валидацию
            - formtarget: Целевое окно для результата
            - height: Высота изображения (пиксели)
            - width: Ширина изображения (пиксели)
            - list: ID связанного datalist
            - alt: Альтернативный текст для изображения
            - src: URL источника изображения
            - rows: Количество строк textarea
            - cols: Количество колонок textarea
            - wrap: Перенос текста в textarea

            Специальные параметры:
            - options: Список опций для select/datalist
            - selected: Выбранное значение для select
            - text: Текст внутри textarea

        Notes
        -----
        Значения по умолчанию:
        - type: 'text'
        - required: False
        - readonly: False
        - disabled: False
        - autofocus: False
        - multiple: False
        - checked: False
        - autocomplete: 'on'
        - formnovalidate: False
        - wrap: 'soft'

        Обязательные атрибуты для определенных типов:
        - Для type="image": обязательны src и alt
        - Для type="file" с capture: рекомендуется использовать accept
        - Для элементов с list: должен существовать datalist с соответствующим ID

        Examples
        --------
        >>> # Элемент с автозаполнением через datalist
        >>> browser_field = FormElement(
        ...     type="text",
        ...     name="browser",
        ...     list="browser-options",
        ...     placeholder="Выберите браузер"
        ... )
        >>>
        >>> # Кнопка с изображением
        >>> image_button = FormElement(
        ...     type="image",
        ...     src="/submit.png",
        ...     alt="Отправить форму",
        ...     width="100",
        ...     height="40",
        ...     formaction="/custom_submit"
        ... )
        >>>
        >>> # Поле загрузки файлов с камеры
        >>> selfie_field = FormElement(
        ...     type="file",
        ...     name="selfie",
        ...     accept="image/*",
        ...     capture="user"
        ... )
        >>>
        >>> # Textarea с настройками
        >>> comments_field = FormElement(
        ...     type="textarea",
        ...     name="comments",
        ...     rows="5",
        ...     cols="40",
        ...     wrap="hard",
        ...     text="Начальный текст"
        ... )
        """
        super().__init__(**kwargs)

        # Атрибуты форм
        self._type = kwargs.get("type", "text")
        self._name = kwargs.get("name")
        self._value = kwargs.get("value")
        self._placeholder = kwargs.get("placeholder")
        self._required = kwargs.get("required", False)
        self._readonly = kwargs.get("readonly", False)
        self._disabled = kwargs.get("disabled", False)
        self._maxlength = kwargs.get("maxlength")
        self._minlength = kwargs.get("minlength")
        self._max = kwargs.get("max")
        self._min = kwargs.get("min")
        self._step = kwargs.get("step")
        self._pattern = kwargs.get("pattern")
        self._autofocus = kwargs.get("autofocus", False)
        self._multiple = kwargs.get("multiple", False)
        self._checked = kwargs.get("checked", False)
        self._autocomplete = kwargs.get("autocomplete", "on")

        # Дополнительные атрибуты
        self._size = kwargs.get("size")
        self._accept = kwargs.get("accept")
        self._capture = kwargs.get("capture")
        self._dirname = kwargs.get("dirname")
        self._form = kwargs.get("form")
        self._formaction = kwargs.get("formaction")
        self._formenctype = kwargs.get("formenctype")
        self._formmethod = kwargs.get("formmethod")
        self._formnovalidate = kwargs.get("formnovalidate", False)
        self._formtarget = kwargs.get("formtarget")
        self._height = kwargs.get("height")
        self._width = kwargs.get("width")
        self._list = kwargs.get("list")
        self._alt = kwargs.get("alt")
        self._src = kwargs.get("src")
        self._rows = kwargs.get("rows")
        self._cols = kwargs.get("cols")
        self._wrap = kwargs.get("wrap", "soft")

        # Для select и datalist
        self._options = kwargs.get("options", [])
        self._selected = kwargs.get("selected")

        # Для textarea
        self._text = kwargs.get("text", "")

    def get_form_attributes(self):
        """
        Генерирует строку специфических атрибутов формы.

        Returns
        -------
        list
            Список строк атрибутов формы

        Examples
        --------
        >>> field = FormElement(
        ...     name="email",
        ...     type="email",
        ...     required=True,
        ...     placeholder="test@example.com"
        ... )
        >>> attrs = field.get_form_attributes()
        >>> print(attrs)
        ['name="email"', 'type="email"', 'required', 'placeholder="test@example.com"']

        Notes
        -----
        Этот метод возвращает только атрибуты формы. Для получения всех
        атрибутов (включая глобальные) используйте get_attributes_string()
        от родительского класса.
        """
        attrs = []

        if self._name:
            attrs.append(f'name="{self._name}"')

        if self._value is not None:
            attrs.append(f'value="{self._value}"')

        if self._placeholder:
            attrs.append(f'placeholder="{self._placeholder}"')

        if self._required:
            attrs.append("required")

        if self._readonly:
            attrs.append("readonly")

        if self._disabled:
            attrs.append("disabled")

        if self._maxlength:
            attrs.append(f'maxlength="{self._maxlength}"')

        if self._minlength:
            attrs.append(f'minlength="{self._minlength}"')

        if self._max is not None:
            attrs.append(f'max="{self._max}"')

        if self._min is not None:
            attrs.append(f'min="{self._min}"')

        if self._step:
            attrs.append(f'step="{self._step}"')

        if self._pattern:
            attrs.append(f'pattern="{self._pattern}"')

        if self._autofocus:
            attrs.append("autofocus")

        if self._multiple:
            attrs.append("multiple")

        if self._checked:
            attrs.append("checked")

        if self._autocomplete != "on":
            attrs.append(f'autocomplete="{self._autocomplete}"')

        return attrs
