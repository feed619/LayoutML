from layoutml.base import BaseElement


class Label(BaseElement):
    """
    Элемент метки <label>
    """

    def __init__(self, for_id=None, text="", object_name=None, style=None, boolean_attributes=[], **kwargs):
        super().__init__(
            tag="label",
            self_closing=False,
            object_name=object_name,
            style=style,
            boolean_attributes=boolean_attributes,
            **kwargs,
        )
        self.object_type = "LabelElement"
        self.text = text
        self.for_id = for_id

    def get_attributes_string(self):
        attrs = []
        attrs_str = super().get_attributes_string()

        if self.for_id:
            attrs.append(f'for="{self.for_id}"')
        return " ".join(attrs) + " " + attrs_str

    def get_html(self, content: str = "", tab: int = 0):
        if not content and self.text:
            content = self.text
        return super().get_html(content=content, tab=tab)
