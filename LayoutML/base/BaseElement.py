from layoutml.base import HTMLElement
from layoutml.base.css import CSSBase, CSSSelectors


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

        self.self_closing = self_closing
        self.selectors_styles: CSSSelectors = CSSSelectors()
        self.object_styles: CSSBase = CSSBase()
        self.tag = tag

    def get_html(self, content: str = "", tab: int = 0):
        if not self.object_name:
            self.object_name = self.object_type
        if not self.class_:
            self.add_class(self.object_name)
        attrs = self.get_attributes_string()
        if content:
            content += "\n"
        if self.self_closing:
            return f"<{self.tag} {attrs}>"
        return f"<{self.tag} {attrs}>{content}{'    '*tab}</{self.tag}>"

    def get_styles(self, space: bool = True):
        if self.object_styles:
            if not self.object_name:
                self.object_name = self.object_type
            if not self.class_:
                self.add_class(self.object_name)

            class_name = " ".join(self.class_)
            if not self.selectors_styles.selector_exists(name=class_name):
                self.selectors_styles.add_selector(name=class_name, selector_type="class")
            self.selectors_styles.add_styles(class_name, dict(self.object_styles))

        return self.selectors_styles.get_styles(space=space)

    # def __getattr__(self, name) -> CSSBase:

    #     if hasattr(self.object_styles, name):
    #         # return self.object_styles
    #         return getattr(self.object_styles, name)

    #     raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{name}'")
