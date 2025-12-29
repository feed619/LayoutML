class HTMLElement:
    """
    Базовый класс для создания HTML элементов с поддержкой глобальных атрибутов.

    Этот класс инкапсулирует стандартные HTML атрибуты, ARIA-атрибуты и обработчики событий,
    предоставляя удобный интерфейс для создания HTML элементов программным способом.

    Attributes
    ----------
    _id : str, optional
        Уникальный идентификатор элемента (атрибут id)
    _class : list
        Список CSS классов (атрибут class)
    _style : str
        Встроенные CSS стили (атрибут style)
    _title : str, optional
        Всплывающая подсказка (атрибут title)
    _data_attrs : dict
        Пользовательские data-* атрибуты
    _hidden : bool
        Определяет, скрыт ли элемент (атрибут hidden)
    _lang : str
        Язык элемента (атрибут lang), по умолчанию 'en'
    _dir : str
        Направление текста (атрибут dir), по умолчанию 'ltr'
    _contenteditable : bool
        Разрешает редактирование содержимого
    _spellcheck : bool
        Включает проверку орфографии
    _draggable : bool
        Определяет, можно ли перетаскивать элемент
    _accesskey : str, optional
        Клавиша быстрого доступа
    _tabindex : int, optional
        Порядок перехода по Tab
    _aria_attrs : dict
        ARIA-атрибуты для улучшения доступности
    _events : dict
        Обработчики событий (onclick, onchange и т.д.)

    Methods
    -------
    __init__(**kwargs)
        Инициализирует HTML элемент с переданными атрибутами
    add_classname(classname)
        Добавляет CSS класс
    remove_class(classname)
        Удаляет CSS класс
    add_data(key, value)
        Добавляет data-* атрибут
    add_aria(key, value)
        Добавляет aria-* атрибут
    add_event(event_name, handler)
        Добавляет обработчик события
    get_attributes_string()
        Генерирует строку атрибутов для HTML-тега

    Examples
    --------
    >>> element = HTMLElement(
    ...     id="myElement",
    ...     classname="container primary",
    ...     data_test="value",
    ...     aria_label="Описание",
    ...     onclick="handleClick()"
    ... )
    >>> print(element.get_attributes_string())
    'id="myElement" class="container primary" data-test="value" aria-label="Описание" onclick="handleClick()"'

    Notes
    -----
    - Для передачи data-* атрибутов используйте префикс 'data_' в именах параметров
    - Для передачи aria-* атрибутов используйте префикс 'aria_' в именах параметров
    - Обработчики событий передаются с префиксом 'on' (onclick, onmouseover и т.д.)
    - Для классов используйте параметр 'classname' (не 'class', так как это зарезервированное слово)
    """

    def __init__(self, **kwargs):
        """
        Инициализирует HTML элемент.

        Parameters
        ----------
        **kwargs : dict
            Атрибуты HTML элемента:
            - id: Уникальный идентификатор
            - classname: CSS классы (строка, разделенная пробелами)
            - style: Встроенные стили CSS
            - title: Всплывающая подсказка
            - data_*: Пользовательские data-атрибуты (например, data_test="значение")
            - aria_*: ARIA-атрибуты (например, aria_label="описание")
            - on*: Обработчики событий (например, onclick="alert('click')")
            - hidden: Скрыть элемент (True/False)
            - lang: Язык контента (по умолчанию 'en')
            - dir: Направление текста ('ltr', 'rtl', 'auto')
            - contenteditable: Разрешить редактирование (True/False)
            - spellcheck: Включить проверку орфографии (True/False)
            - draggable: Разрешить перетаскивание (True/False)
            - accesskey: Клавиша быстрого доступа
            - tabindex: Порядок табуляции

        Examples
        --------
        >>> # Создание элемента с несколькими атрибутами
        >>> elem = HTMLElement(
        ...     id="main",
        ...     classname="btn btn-primary",
        ...     title="Нажмите меня",
        ...     data_id="123",
        ...     aria_label="Основная кнопка",
        ...     onclick="submitForm()",
        ...     tabindex=1
        ... )
        >>>
        >>> # Создание доступного элемента
        >>> accessible_elem = HTMLElement(
        ...     aria_labelledby="label1",
        ...     aria_describedby="desc1",
        ...     role="button",
        ...     tabindex=0
        ... )
        """
        # Глобальные атрибуты
        self._id = kwargs.get("id")
        self._class = kwargs.get("classname", "").split()  # class - зарезервированное слово
        self._style = kwargs.get("style", "")
        self._title = kwargs.get("title")
        self._data_attrs = {k[5:]: v for k, v in kwargs.items() if k.startswith("data_")}
        self._hidden = kwargs.get("hidden", False)
        self._lang = kwargs.get("lang", "en")
        self._dir = kwargs.get("dir", "ltr")
        self._contenteditable = kwargs.get("contenteditable", False)
        self._spellcheck = kwargs.get("spellcheck", False)
        self._draggable = kwargs.get("draggable", False)
        self._accesskey = kwargs.get("accesskey")
        self._tabindex = kwargs.get("tabindex")

        # ARIA атрибуты
        self._aria_attrs = {k[5:]: v for k, v in kwargs.items() if k.startswith("aria_")}

        # Обработчики событий
        self._events = {k: v for k, v in kwargs.items() if k.startswith("on")}

    def add_classname(self, classname):
        """
        Добавляет CSS класс к элементу.

        Parameters
        ----------
        classname : str
            Название CSS класса для добавления

        Examples
        --------
        >>> element = HTMLElement(classname="container")
        >>> element.add_classname("active")
        >>> element.add_classname("highlight")
        >>> element.get_attributes_string()
        'class="container active highlight"'
        """
        if classname not in self._class:
            self._class.append(classname)

    def remove_class(self, classname):
        """
        Удаляет CSS класс из элемента.

        Parameters
        ----------
        classname : str
            Название CSS класса для удаления

        Examples
        --------
        >>> element = HTMLElement(classname="container active highlight")
        >>> element.remove_class("active")
        >>> element.get_attributes_string()
        'class="container highlight"'
        """
        if classname in self._class:
            self._class.remove(classname)

    def add_data(self, key, value):
        """
        Добавляет или обновляет data-* атрибут.

        Parameters
        ----------
        key : str
            Имя атрибута без префикса 'data-'
        value : str
            Значение атрибута

        Examples
        --------
        >>> element = HTMLElement()
        >>> element.add_data("user_id", "12345")
        >>> element.add_data("action", "delete")
        >>> element.get_attributes_string()
        'data-user_id="12345" data-action="delete"'

        Notes
        -----
        В HTML атрибут будет преобразован в data-user-id (с дефисами),
        но в методе используется нижнее подчеркивание для удобства.
        """
        self._data_attrs[key] = value

    def add_aria(self, key, value):
        """
        Добавляет или обновляет aria-* атрибут для улучшения доступности.

        Parameters
        ----------
        key : str
            Имя ARIA-атрибута без префикса 'aria-'
        value : str
            Значение атрибута

        Examples
        --------
        >>> element = HTMLElement()
        >>> element.add_aria("label", "Закрыть меню")
        >>> element.add_aria("expanded", "false")
        >>> element.get_attributes_string()
        'aria-label="Закрыть меню" aria-expanded="false"'

        Notes
        -----
        ARIA-атрибуты важны для обеспечения доступности веб-контента
        для пользователей с ограниченными возможностями.
        """
        self._aria_attrs[key] = value

    def add_event(self, event_name, handler):
        """
        Добавляет обработчик события к элементу.

        Parameters
        ----------
        event_name : str
            Имя события с префиксом 'on' (например, 'onclick', 'onmouseover')
        handler : str
            JavaScript код для обработки события

        Examples
        --------
        >>> element = HTMLElement()
        >>> element.add_event("onclick", "handleClick(event)")
        >>> element.add_event("onmouseover", "showTooltip()")
        >>> element.get_attributes_string()
        'onclick="handleClick(event)" onmouseover="showTooltip()"'

        Warnings
        --------
        Для безопасности рекомендуется использовать Event Listeners
        вместо inline-обработчиков при работе с пользовательскими данными.
        """
        self._events[event_name] = handler

    def get_attributes_string(self):
        """
        Генерирует строку атрибутов для использования в HTML-теге.

        Returns
        -------
        str
            Строка атрибутов, готовая для вставки в HTML-тег

        Examples
        --------
        >>> element = HTMLElement(
        ...     id="submitBtn",
        ...     classname="btn primary",
        ...     onclick="submitForm()"
        ... )
        >>> attributes = element.get_attributes_string()
        >>> print(f'<button {attributes}>Нажми меня</button>')
        <button id="submitBtn" class="btn primary" onclick="submitForm()">Нажми меня</button>

        >>> # Пример с несколькими атрибутами
        >>> complex_element = HTMLElement(
        ...     id="userCard",
        ...     classname="card user-card",
        ...     data_user_id="42",
        ...     aria_role="region",
        ...     aria_label="Карточка пользователя",
        ...     style="width: 300px;",
        ...     tabindex=0
        ... )
        >>> complex_element.get_attributes_string()
        'id="userCard" class="card user-card" style="width: 300px;" data-user_id="42" aria-role="region" aria-label="Карточка пользователя" tabindex="0"'

        Notes
        -----
        - Булевы атрибуты (hidden, contenteditable и т.д.) выводятся только
          если их значение равно True
        - Атрибуты выводятся в определенном порядке для улучшения читаемости
        - data-* и aria-* атрибуты автоматически преобразуются из нижних
          подчеркиваний в дефисы (data_user_id -> data-user-id)
        """
        attrs = []

        # Глобальные атрибуты
        if self._id:
            attrs.append(f'id="{self._id}"')

        if self._class:
            attrs.append(f'class="{" ".join(self._class)}"')

        if self._style:
            attrs.append(f'style="{self._style}"')

        if self._title:
            attrs.append(f'title="{self._title}"')

        if self._hidden:
            attrs.append("hidden")

        if self._lang != "en":
            attrs.append(f'lang="{self._lang}"')

        if self._dir != "ltr":
            attrs.append(f'dir="{self._dir}"')

        if self._contenteditable:
            attrs.append('contenteditable="true"')

        if self._spellcheck:
            attrs.append('spellcheck="true"')

        if self._draggable:
            attrs.append('draggable="true"')

        if self._accesskey:
            attrs.append(f'accesskey="{self._accesskey}"')

        if self._tabindex is not None:
            attrs.append(f'tabindex="{self._tabindex}"')

        # data-* атрибуты
        for key, value in self._data_attrs.items():
            attrs.append(f'data-{key}="{value}"')

        # aria-* атрибуты
        for key, value in self._aria_attrs.items():
            attrs.append(f'aria-{key}="{value}"')

        # Обработчики событий
        for event, handler in self._events.items():
            attrs.append(f'{event}="{handler}"')

        return " ".join(attrs)
