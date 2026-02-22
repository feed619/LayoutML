from .Form import Form


class Input(Form):
    """
    Специализированный Input элемент с удобными методами
    """

    def __init__(
        self,
        input_type="text",
        placeholder="",
        value="",
        name=None,
        id=None,
        object_name=None,
        style=None,
        boolean_attributes=[],
        **kwargs,
    ):
        super().__init__(
            form_type=input_type,
            object_name=object_name,
            style=style,
            boolean_attributes=boolean_attributes,
            **kwargs,
        )
        self.object_type = "InputElement"
        self.placeholder = placeholder
        self.value = value
        self.name = name
        self.id = id

    def get_attributes_string(self):
        attrs = []
        attrs_str = super().get_attributes_string()

        if self.placeholder:
            attrs.append(f'placeholder="{self.placeholder}"')
        if self.value:
            attrs.append(f'value="{self.value}"')
        if self.name:
            attrs.append(f'name="{self.name}"')
        if self.id:
            attrs.append(f'id="{self.id}"')
        return " ".join(attrs) + " " + attrs_str
