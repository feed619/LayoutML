from layoutml.base import BaseElement


class Paragraph(BaseElement):
    """
    Элемент параграфа <p>
    """

    def __init__(self, text="", object_name=None, style=None, boolean_attributes=[], **kwargs):
        super().__init__(
            tag="p",
            self_closing=False,
            object_name=object_name,
            style=style,
            boolean_attributes=boolean_attributes,
            **kwargs,
        )
        self.object_type = "ParagraphElement"
        self.text = text

    def get_html(self, content: str = "", tab: int = 0):
        if not content and self.text:
            content = self.text
        return super().get_html(content=content, tab=tab)
