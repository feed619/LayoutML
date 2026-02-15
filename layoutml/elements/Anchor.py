from layoutml.base import BaseElement


class Anchor(BaseElement):
    """
    Элемент ссылки <a>
    """

    def __init__(self, href, text="", target="_self", object_name=None, style=None, boolean_attributes=[], **kwargs):
        super().__init__(
            tag="a",
            self_closing=False,
            object_name=object_name,
            style=style,
            boolean_attributes=boolean_attributes,
            **kwargs,
        )
        self.object_type = "AnchorElement"
        self.href = href
        self.text = text
        self.target = target

    def get_attributes_string(self):
        attrs = []
        attrs_str = super().get_attributes_string()

        attrs.append(f'href="{self.href}"')
        attrs.append(f'target="{self.target}"')
        return " ".join(attrs) + " " + attrs_str

    def get_html(self, tab: int = 0):
        return super().get_html(content=self.text, tab=tab)
