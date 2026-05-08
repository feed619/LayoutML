from layoutml.base import BaseElement


class Header(BaseElement):
    """
    Семантический элемент шапки <header>
    """

    def __init__(self, object_name=None, style=None, boolean_attributes=[], **kwargs):
        super().__init__(
            tag="header",
            self_closing=False,
            object_name=object_name,
            style=style,
            boolean_attributes=boolean_attributes,
            **kwargs,
        )
        self.object_type = "HeaderElement"

    def copy(self, copy_element: "Header" = None) -> "Header":
        if copy_element is None:
            copy_element = Header(object_name=self.object_name)
        super().copy(copy_element=copy_element)
        return copy_element
