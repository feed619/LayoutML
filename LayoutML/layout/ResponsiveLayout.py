from .Layout import Layout


class ResponsiveLayout(Layout):
    """Адаптивный layout, меняющий направление при определенной ширине"""

    def __init__(
        self,
        breakpoint: str = "768px",
        is_mobile=False,
        desktop_direction="row",
        mobile_direction="column",
        **kwargs,
    ):
        super().__init__(**kwargs)
        self._type = "responsive_layout"

        self._breakpoint = breakpoint
        self._is_mobile = is_mobile
        self._desktop_direction = desktop_direction
        self._mobile_direction = mobile_direction

        # Генерируем адаптивные стили
        self._generate_responsive_styles()

    def _generate_responsive_styles(self) -> None:
        """Генерация медиа-запросов для адаптивности"""

        self.styles["flex-direction"] = self._desktop_direction

        mobile_style = f"""
            display: flex;
            flex-direction: {self._mobile_direction};
            justify-content: {self.styles["justify-content"]};
            align-items: {self.styles["align-items"]};
            gap: {self.styles["gap"]};
            padding: {self.styles["padding"]};
            margin: {self.styles["margin"]};
        """

        self.styles[f"@media (max-width: {self._breakpoint}) {{"] = f"{mobile_style}}}"

    def set_breakpoint(self, breakpoint: str) -> "ResponsiveLayout":
        """Установить точку перелома для адаптивности"""
        self._breakpoint = breakpoint
        self._generate_responsive_styles()
        return self

    def set_directions(self, desktop: str, mobile: str) -> "ResponsiveLayout":
        """Установить направления для десктопа и мобильных"""
        self._desktop_direction = desktop
        self._mobile_direction = mobile
        self._generate_responsive_styles()
        return self
