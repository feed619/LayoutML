from typing import Dict
from .CSSBase import CSSBase


class CSSInline(CSSBase):

    styles: dict

    def __init__(self, style=None):
        super().__init__(style=style)

    def get_styles_str(self, space=False):
        styles = self.get_styles_string(space=space)
        if styles:
            return f'style="{self.get_styles_string(space=space)}"'
        else:
            return ""

    def copy(self, copy_element: "CSSInline" = None) -> "CSSInline":
        if copy_element is None:
            copy_element = CSSInline()
        super().copy(copy_element=copy_element)
        return copy_element
