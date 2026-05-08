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

    def copy(self, copy_element: "Button" = None) -> "Button":
        if copy_element is None:
            copy_element = Button(object_name=self.object_name)
        super().copy(copy_element=copy_element)
        copy_element.text = self.text
        return copy_element
