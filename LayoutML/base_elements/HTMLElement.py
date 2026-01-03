from LayoutML.html_core.HTMLAttributes import ValueAttributes


class HTMLElement:
    class_: list[str]
    styles: dict
    events: dict
    value_attributes: dict
    custom_attributes: dict
    boolean_attributes: list

    def __init__(self, boolean_attributes=[], **kwargs):

        self.custom_attributes = {}
        self.events = {}
        self.boolean_attributes = boolean_attributes if type(boolean_attributes) is list else []

        if "class_" in kwargs:
            self.class_ = kwargs.get("class_", "").split()
            del kwargs["class_"]
        if "style" in kwargs:
            self.styles = self.parse_style_string(kwargs.get("style", ""))
            del kwargs["style"]
        self.value_attributes: dict = kwargs

    def parse_style_string(self, style_str: str) -> dict:
        """Парсит CSS-строку стилей в словарь."""
        styles = {}

        for item in style_str.split(";"):
            item = item.strip()
            if not item:
                continue

            if ":" not in item:
                continue
            key, value = item.split(":", 1)
            styles[key.strip()] = value.strip()

        return styles

    def add_class(self, classname):
        """
        Добавляет CSS класс к элементу.

        Parameters
        ----------
        classname : str
            Название CSS класса для добавления

        """
        if classname not in self.class_:
            self.class_.append(classname)

    def del_class(self, classname):
        """
        Удаляет CSS класс из элемента.

        Parameters
        ----------
        classname : str
            Название CSS класса для удаления

        """
        if classname in self.class_:
            self.class_.remove(classname)

    def add_style(self, style):
        """
        Добавляет стили в словарь styles.

        Parameters
        ----------
        style : str
        """
        new_styles = self.parse_style_string(style)
        for style_name, style_value in new_styles.items():
            self.styles[style_name] = style_value

    def del_style(self, style_name):
        """
        Удаляет стиля из словаря styles.

        Parameters
        ----------
        stryle_name : str
            Название стиля для удаления

        """
        if style_name in self.styles:
            del self.styles[style_name]

    def add_event(self, event_name, handler):
        """
        Добавляет обработчик события к элементу.

        Parameters
        ----------
        event_name : str
            Имя события с префиксом 'on' (например, 'onclick', 'onmouseover')
        handler : str
            JavaScript код для обработки события

        Warnings
        --------
        Для безопасности рекомендуется использовать Event Listeners
        вместо inline-обработчиков при работе с пользовательскими данными.
        """
        self.events[event_name] = handler

    def del_event(self, event_name):
        if event_name in self.events:
            del self.events[event_name]

    def get_attributes_string(self):
        """
        Генерирует строку атрибутов для использования в HTML-теге.

        Returns
        -------
        str
            Строка атрибутов, готовая для вставки в HTML-тег
        """
        attrs = []
        print(self.value_attributes)
        if self.class_:
            attrs.append(f'class="{" ".join(self.class_)}"')
        if self.styles:
            style_str_list = []
            for style_name, style_value in self.styles.items():
                style_str_list.append(f"{style_name}:{style_value};")
            attrs.append(f'style="{" ".join(style_str_list)}"')
        if self.events:
            for event, handler in self.events.items():
                attrs.append(f'{event}="{handler}"')
        if self.boolean_attributes:
            for bool_atr in self.boolean_attributes:
                attrs.append(bool_atr)

        for key, value in self.value_attributes.items():
            try:
                atr_name = getattr(ValueAttributes, key)
            except AttributeError:
                raise AttributeError(
                    f"Attribute '{key}' not found in HTMLElementAttributes class. "
                    f"Available attributes are defined in the HTMLElementAttributes class."
                )
            attrs.append(f'{atr_name}="{value}"')

            print(atr_name, value)
        return " ".join(attrs)

        # data-* атрибуты
        for key, value in self._data_attrs.items():
            attrs.append(f'data-{key}="{value}"')

        # aria-* атрибуты
        for key, value in self._aria_attrs.items():
            attrs.append(f'aria-{key}="{value}"')
