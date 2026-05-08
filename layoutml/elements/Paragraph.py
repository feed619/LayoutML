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

    def copy(self, copy_element: "Paragraph" = None) -> "Paragraph":
        if not copy_element:
            copy_element = Paragraph(object_name=self.object_name)
        super().copy(copy_element=copy_element)
        copy_element.text = self.text
        return copy_element
