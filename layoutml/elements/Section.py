from layoutml.base import BaseElement


class Section(BaseElement):
    """
    Семантический элемент секции <section>
    """

    def __init__(self, object_name=None, style=None, boolean_attributes=[], **kwargs):
        super().__init__(
            tag="section",
            self_closing=False,
            object_name=object_name,
            style=style,
            boolean_attributes=boolean_attributes,
            **kwargs,
        )
        self.object_type = "SectionElement"

    def copy(self, copy_element: "Section" = None) -> "Section":
        if copy_element is None:
            copy_element = Section(object_name=self.object_name)
        super().copy(copy_element=copy_element)
        return copy_element
