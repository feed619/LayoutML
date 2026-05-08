from copy import deepcopy

from layoutml.base import HTMLElement
from layoutml.base.css import CSSBase, CSSSelectors, StyleType


class BaseElement(HTMLElement):
    object_styles: CSSBase
    selectors_styles: CSSSelectors
    tag: str

    def __init__(
        self,
        tag="",
        self_closing: bool = False,
        object_name=None,
        style=None,
        boolean_attributes=[],
        **kwargs,
    ):
        super().__init__(object_name=object_name, style=style, boolean_attributes=boolean_attributes, **kwargs)

        self.tag = tag
        self.self_closing = self_closing
        self.selectors_styles: CSSSelectors = CSSSelectors()
        self.object_styles: CSSBase = CSSBase()

    def copy(self, copy_element: "BaseElement" = None) -> "BaseElement":
        if copy_element is None:
            copy_element = BaseElement(
                tag=self.tag,
                self_closing=self.self_closing,
            )

        super().copy(copy_element=copy_element)
        copy_element.object_styles = self.object_styles.copy()
        copy_element.selectors_styles = self.selectors_styles.copy()
        return copy_element

    def set_styles_mode(self, style_type: str) -> "BaseElement":
        """'global' or 'external'"""
        if style_type == "global":
            self.selectors_styles.styles_type = StyleType.GLOBAL
        elif style_type == "external":
            self.selectors_styles.styles_type = StyleType.EXTERNAL
        return self

    def get_html(self, content: str = "", tab: int = 0):
        if not self.object_name:
            self.object_name = self.object_type
        if not self.class_:
            self.add_class(self.object_name)
        attrs = self.get_attributes_string()
        if content:
            content = str(content) + "\n"
        if self.self_closing:
            return f"<{self.tag} {attrs}>"
        return f"<{self.tag} {attrs}>{content}{'    '*tab}</{self.tag}>"

    def get_styles(self, styles_type: StyleType = StyleType.EXTERNAL, space: bool = True):
        if not styles_type is self.selectors_styles.styles_type:
            return {}
        if self.object_styles:
            if not self.class_:
                self.add_class(self.get_object_name())
            class_name = " ".join(self.class_)
            if not self.selectors_styles.selector_exists(name=class_name):
                self.selectors_styles.add_selector(name=class_name, selector_type="class")
            self.selectors_styles.add_styles(class_name, dict(self.object_styles))
        return self.selectors_styles.get_styles(space=space)
