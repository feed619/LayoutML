from typing import Dict
from .CSSBase import CSSBase


class CSSSelectors:
    selectors: dict[CSSBase]
    class_name: str

    def __init__(self, inline: bool = False):

        self.inline = inline
        self.selectors: dict[CSSBase] = {}
        # self.class_name = class_name
        # self.add_selector(class_name, selector_type="class")

    # def object(self) -> CSSBase:
    #     return self.selectors[self.class_name]

    def __repr__(self):
        return str(self.selectors)

    def __getattr__(self, name) -> CSSBase:
        # if name == "main":
        #     return self.selectors[self.class_name]
        if name not in self.selectors:
            self.selectors[name] = CSSBase()
        return self.selectors[name]

    def add_selector(self, name, selector_type="class", style: str | CSSBase = None):
        """параметры type может принимать class, id, tag"""
        if name not in self.selectors:
            if type(style) is CSSBase:
                self.selectors[name] = style
            else:
                self.selectors[name] = CSSBase(type=selector_type, style=style)
        return self.selectors[name]

    def delete_selector(self, name):
        if name in self.selectors:
            del self.selectors[name]

    def clear(self) -> "CSSBase":
        """Удалить все селекторы"""
        self.selectors.clear()
        return self

    def selector_exists(self, name: str) -> tuple[bool, str]:
        """
        Проверяет существование селектора и возвращает его тип
        """
        if name in self.selectors:
            return True
        return False

    def add_styles(self, selector_name: str, styles: dict | CSSBase):
        """Добавляет стили к селектору"""
        if selector_name in self.selectors:
            for prop, value in styles.items():
                self.selectors[selector_name].styles[prop] = value

    def get_styles(self, space=True):
        """Генерирует словарь стилей"""
        selectors_styles = {}
        for selector_name, selector in self.selectors.items():

            if selector.type:
                if selector.type == "class":
                    selector_prefix = "."
                elif selector.type == "id":
                    selector_prefix = "#"
                elif selector.type == "media":
                    selector_prefix = "@"
            else:
                selector_prefix = ""

            selectors_styles[f"{selector_prefix}{selector_name}"] = selector.get_styles_string(space=space)

        return selectors_styles

    def get_styles_str(self):
        styles = self.get_styles()
        styles_str: str = ""
        for selector_name, css in styles.items():
            styles_str += f"{selector_name} " + "{\n" + css + "}\n"

        if self.inline:
            return f"<style>\n{styles_str}</style>"
        return styles_str

    def __iter__(self):
        return iter(self.selectors.items())

    def __getitem__(self, key) -> CSSBase:
        selector = self.selectors.get(key, None)
        if not selector:
            self.add_selector(key)
            return self.selectors.get(key, None)
        return selector

    def __setitem__(self, key, value: CSSBase | dict | str):

        if type(value) is str:
            self.selectors[key] = CSSBase(style=value)
        else:
            if type(value) is CSSBase:
                self.selectors[key] = CSSBase()

                self.selectors[key].styles = value.styles.copy_styles()
            elif type(value) is dict:
                self.selectors[key] = CSSBase()
                self.selectors[key].styles = value
            else:
                raise

    def __delitem__(self, key):
        if key in self.selectors:
            del self.selectors[key]

    def __len__(self):
        return len(self.selectors)

    def __bool__(self):
        return bool(self.selectors)

    def __call__(self, *args, **kwds):
        return self
