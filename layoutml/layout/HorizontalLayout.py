from copy import deepcopy

from layoutml.layout import Layout


class HorizontalLayout(Layout):
    """Горизонтальный layout (flex-direction: row)"""

    def __init__(
        self,
        justify_content="center",
        align_items="center",
        object_name=None,
        **kwargs,
    ):
        super().__init__(justify_content=justify_content, align_items=align_items, object_name=object_name, **kwargs)

        self.object_type = "HorizontalLayout"

        self.object_styles["flex-direction"] = "row"

    def set_reverse(self, reverse: bool = True) -> "HorizontalLayout":
        """
        Установить обратное направление элементов

        Args:
            reverse: Если True - элементы идут справа налево
        """
        if reverse:
            self.object_styles["flex-direction"] = "row-reverse"
        else:
            self.object_styles["flex-direction"] = "row"
        return self

    def copy(self, copy_element: "HorizontalLayout" = None) -> "HorizontalLayout":
        if copy_element is None:
            copy_element = HorizontalLayout(object_name=self.object_name)
        super().copy(copy_element=copy_element)
        # copy_element.object_styles = deepcopy(self.object_styles)
        return copy_element
