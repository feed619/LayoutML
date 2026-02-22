from layoutml.base import BaseElement


class Select(BaseElement):
    """
    Элемент выпадающего списка <select>
    """

    def __init__(
        self,
        options=None,
        selected_value=None,
        name=None,
        id=None,
        object_name=None,
        style=None,
        boolean_attributes=[],
        **kwargs,
    ):
        super().__init__(
            tag="select",
            self_closing=False,
            object_name=object_name,
            style=style,
            boolean_attributes=boolean_attributes,
            **kwargs,
        )
        self.object_type = "SelectElement"
        self.options = options or []
        self.selected_value = selected_value
        self.name = name
        self.id = id

    def add_option(self, value, text, selected=False):
        """
        Добавляет опцию в список
        """
        self.options.append({"value": value, "text": text, "selected": selected})

    def get_attributes_string(self):
        attrs = []
        attrs_str = super().get_attributes_string()

        if self.name:
            attrs.append(f'name="{self.name}"')
        if self.id:
            attrs.append(f'id="{self.id}"')
        return " ".join(attrs) + " " + attrs_str

    def get_html(self, content: str = "", tab: int = 0):
        # Формируем опции
        options_html = ""
        for option in self.options:
            selected = ""
            if option.get("selected") or option.get("value") == self.selected_value:
                selected = " selected"
            options_html += f"{'    '*(tab+1)}<option value=\"{option['value']}\"{selected}>{option['text']}</option>\n"

        if options_html:
            content = f"\n{options_html}{'    '*tab}"
        return super().get_html(content=content, tab=tab)
