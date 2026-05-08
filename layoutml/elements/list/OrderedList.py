from .ListElement import ListElement


class OrderedList(ListElement):
    """
    Нумерованный список <ol>
    """

    def __init__(self, items=None, object_name=None, style=None, boolean_attributes=[], **kwargs):
        super().__init__(
            tag="ol",
            items=items,
            object_name=object_name,
            style=style,
            boolean_attributes=boolean_attributes,
            **kwargs,
        )
        self.object_type = "OrderedListElement"

    def copy(self, copy_element: "OrderedList" = None) -> "OrderedList":
        if not copy_element:
            copy_element = OrderedList(object_name=self.object_name)
        super().copy(copy_element=copy_element)
        return copy_element
