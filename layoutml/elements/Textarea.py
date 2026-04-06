from layoutml.base import BaseElement


class Textarea(BaseElement):
    """
    Элемент многострочного текстового поля <textarea>
    """

    def __init__(
        self,
        placeholder="",
        value="",
        rows=4,
        cols=50,
        name=None,
        id=None,
        object_name=None,
        style=None,
        boolean_attributes=[],
        **kwargs,
    ):
        super().__init__(
            tag="textarea",
            self_closing=False,
            object_name=object_name,
            style=style,
            boolean_attributes=boolean_attributes,
            **kwargs,
        )
        self.object_type = "TextareaElement"
        self.placeholder = placeholder
        self.value = value
        self.rows = rows
        self.cols = cols
        self.name = name
        self.id = id

    def get_attributes_string(self):
        attrs = []
        attrs_str = super().get_attributes_string()

        if self.placeholder:
            attrs.append(f'placeholder="{self.placeholder}"')
        if self.rows:
            attrs.append(f'rows="{self.rows}"')
        if self.cols:
            attrs.append(f'cols="{self.cols}"')
        if self.name:
            attrs.append(f'name="{self.name}"')
        if self.id:
            attrs.append(f'id="{self.id}"')
        return " ".join(attrs) + " " + attrs_str

    def get_html(self, content: str = "", tab: int = 0):
        # Для textarea содержимое - это значение между тегами
        if not content and self.value:
            content = self.value
        return super().get_html(content=content, tab=tab)
