from typing import Dict
from .CSSBase import CSSBase


class CSSInline(CSSBase):

    styles: dict

    def __init__(self, style=None):
        super().__init__(style=style)

    def render(self, space=False):
        styles = self.get_styles_string(space=space)
        if styles:
            return f'style="{self.get_styles_string(space=space)}"'
        else:
            return ""
