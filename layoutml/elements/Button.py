from layoutml.base import BaseElement


class Button(BaseElement):
    """
    Элемент кнопки <button>
    """

    def __init__(self, text="", object_name=None, style=None, boolean_attributes=[], **kwargs):
        super().__init__(
            tag="button",
            self_closing=False,
            object_name=object_name,
            style=style,
            boolean_attributes=boolean_attributes,
            **kwargs,
        )
        self.object_type = "ButtonElement"
        self.text = text

    def get_html(self, tab: int = 0):
        return super().get_html(content=self.text, tab=tab)
