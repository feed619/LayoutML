from layoutml.base import BaseElement


class Nav(BaseElement):
    """
    Семантический элемент навигации <nav>
    """

    def __init__(self, object_name=None, style=None, boolean_attributes=[], **kwargs):
        super().__init__(
            tag="nav",
            self_closing=False,
            object_name=object_name,
            style=style,
            boolean_attributes=boolean_attributes,
            **kwargs,
        )
        self.object_type = "NavElement"

    def copy(self, copy_element: "Nav" = None) -> "Nav":
        if copy_element is None:
            copy_element = Nav(object_name=self.object_name)
        super().copy(copy_element=copy_element)
        return copy_element
