from typing import Dict
from .CSSBase import CSSBase


class CSSInput:
    selectors: dict[CSSBase]

    def __init__(self):

        self.selectors = {}

    def __getattr__(self, name) -> CSSBase:
        if name not in self.selectors:
            self.selectors[name] = CSSBase()
        return self.selectors[name]

    def add_selector(self, name, type="class", style=None):
        """параметры type может принимать class, id, tag"""
        if name not in self.selectors:
            self.selectors[name] = CSSBase(type=type, style=style)
        return self.selectors[name]

    def delete_selector(self, name):
        if name in self.selectors:
            del self.selectors[name]

    def clear(self) -> "CSSBase":
        """Удалить все селекторы"""
        self.selectors.clear()
        return self

    def render(self, space=True):
        """Генерирует строку стилей"""
        selectors_str_list = []
        for selector_name, selector in self.selectors.items():
            selector_prefix = ""
            if selector.type == "class":
                selector_prefix = "."
            elif selector.type == "id":
                selector_prefix = "#"
            elif selector.type == "media":
                selector_prefix = "@"

            selectors_str_list.append(f"{selector_prefix}{selector_name}" + " {\n" + selector.get_styles_string(space=space) + "}\n")
        if selectors_str_list:
            return f"<style>\n {''.join(selectors_str_list)}</style>"
        else:
            return ""
