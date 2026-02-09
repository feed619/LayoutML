from typing import Any, List
from layoutml.base import BaseElement


class Layout(BaseElement):
    """Базовый класс для всех layout'ов"""

    elements: List[BaseElement]

    def __init__(
        self,
        object_name=None,
        justify_content="center",
        align_items="center",
        **kwargs,
    ):
        super().__init__(tag="div", object_name=object_name, **kwargs)

        self.object_type = "Layout"

        self.is_stretched = False
        self.object_styles["background"] = "transparent"
        self.object_styles["display"] = "flex"
        self.object_styles["flex-direction"] = "row"
        self.object_styles["flex-wrap"] = "nowrap"

        self.object_styles["justify-content"] = justify_content
        self.object_styles["align-items"] = align_items

        self.elements: List[BaseElement] = []

    def stretch(self, fullscreen: bool = True) -> "Layout":
        """
        Растянуть layout на весь экран

        Args:
            fullscreen: Если True - на весь экран (100vw x 100vh)
                       Если False - на всю доступную ширину (100%)
        """
        self.is_stretched = True
        if fullscreen:
            self.object_styles["width"] = "100vw"
            self.object_styles["height"] = "100vh"
        else:
            self.object_styles["width"] = "100%"
            self.object_styles["height"] = "auto"
        return self

    def unstretch(self) -> "Layout":
        """Отменить растяжение"""
        self.is_stretched = False
        self.object_styles["width"] = "auto"
        self.object_styles["height"] = "auto"
        return self

    def set_size(self, width: str = None, height: str = None) -> "Layout":
        """Установить размеры layout'а"""
        if width:
            self.object_styles["width"] = width
        if height:
            self.object_styles["height"] = height

        if width == "100%" or width == "100vw":
            self.is_stretched = True
        else:
            self.is_stretched = False

        return self

    # ============ МЕТОДЫ ДЛЯ ЭЛЕМЕНТОВ ============

    def add_element(self, element: Any) -> "Layout":
        """Добавить элемент в layout"""
        self.elements.append(element)
        return self

    def add_elements(self, *elements: Any) -> "Layout":
        """Добавить несколько элементов"""
        for element in elements:
            self.elements.append(element)
        return self

    def clear(self) -> "Layout":
        """Очистить все элементы"""
        self.elements.clear()
        return self

    def insert_element(self, index: int, element: Any) -> "Layout":
        """Вставить элемент по индексу"""
        self.elements.insert(index, element)
        return self

    def remove_element(self, index: int) -> "Layout":
        """Удалить элемент по индексу"""
        if 0 <= index < len(self.elements):
            del self.elements[index]
        return self

    def get_html(self) -> str:
        elements_html = ""
        for element in self.elements:
            if hasattr(element, "get_html"):
                elements_html += f"\n\t\t{element.get_html()}"
            else:
                elements_html += f"\n\t\t{element}"
        return super().get_html(content=elements_html, tab=2)

    def get_styles(self) -> str:

        css_styles: dict = super().get_styles()
        for element in self.elements:
            css_styles.update(element.get_styles())
        return css_styles

    def __len__(self) -> int:
        """Количество элементов"""
        return len(self.elements)

    def __getitem__(self, index: int) -> Any:
        """Получить элемент по индексу"""
        return self.elements[index]

    def __setitem__(self, index: int, element: Any) -> None:
        """Установить элемент по индексу"""
        self.elements[index] = element

    def __delitem__(self, index: int) -> None:
        """Удалить элемент по индексу"""
        del self.elements[index]
