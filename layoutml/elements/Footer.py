from layoutml.base import BaseElement


class Footer(BaseElement):
    """
    Семантический элемент подвала <footer>
    """

    def __init__(self, object_name=None, style=None, boolean_attributes=[], **kwargs):
        super().__init__(
            tag="footer",
            self_closing=False,
            object_name=object_name,
            style=style,
            boolean_attributes=boolean_attributes,
            **kwargs,
        )
        self.object_type = "FooterElement"

    def copy(self, copy_element: "Footer" = None) -> "Footer":
        if copy_element is None:
            copy_element = Footer(object_name=self.object_name)
        super().copy(copy_element=copy_element)
        return copy_element
