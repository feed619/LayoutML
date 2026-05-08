from .ListElement import ListElement


class UnorderedList(ListElement):
    """
    Ненумерованный список <ul>
    """

    def __init__(self, items=None, object_name=None, style=None, boolean_attributes=[], **kwargs):
        super().__init__(
            tag="ul",
            items=items,
            object_name=object_name,
            style=style,
            boolean_attributes=boolean_attributes,
            **kwargs,
        )
        self.object_type = "UnorderedListElement"

    def copy(self, copy_element: "UnorderedList" = None) -> "UnorderedList":
        if copy_element is None:
            copy_element = UnorderedList(object_name=self.object_name)
        super().copy(copy_element=copy_element)
        return copy_element
