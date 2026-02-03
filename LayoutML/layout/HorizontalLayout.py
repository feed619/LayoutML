from typing import Any, List
from layoutml.base import HTMLElement

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
