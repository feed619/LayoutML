from .Layout import Layout


class VerticalLayout(Layout):
    """Вертикальный layout (колонка)"""

    def __init__(
        self,
        justify_content="center",
        align_items="center",
        object_name=None,
        **kwargs,
    ):
        super().__init__(justify_content=justify_content, align_items=align_items, object_name=object_name, **kwargs)

        self.object_type = "VerticalLayout"

        self.object_styles["flex-direction"] = "column"
        # Добавляем box-sizing для правильного расчета размеров
        self.object_styles["box-sizing"] = "border-box"

    def set_reverse(self, reverse: bool = True) -> "VerticalLayout":
        """
        Установить обратное направление элементов

        Args:
            reverse: Если True - элементы идут справа налево
        """
        if reverse:
            self.object_styles["flex-direction"] = "column-reverse"
        else:
            self.object_styles["flex-direction"] = "column"
        return self
