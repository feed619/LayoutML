from copy import deepcopy
from typing import List, Dict, Optional, Any
from layoutml.base import BaseElement
from layoutml.base.css.CSSSelectors import StyleType
from .base import BaseElement


class Body(BaseElement):
    """
    Класс для HTML body элемента
    Содержит основное содержимое страницы
    """

    object_type: str

    def __init__(self, content: str = "", object_name=None, **kwargs):
        super().__init__(tag="body", object_name=object_name, **kwargs)

        self.object_type = "Body"
        self.links = {}
        self.content = content
        self.elements: List[BaseElement] = []
        self.scripts_footer: List[Dict] = []

    def add_content(self, content: str) -> "Body":
        """Добавить текстовое содержимое"""
        self.content += content
        return self

    def add_element(self, element: Any) -> "Body":
        """
        Добавить HTML элемент
        """
        self.elements.append(element)
        return self

    def add_html(self, html: str) -> "Body":
        """Добавить сырой HTML"""
        self.elements.append(html)
        return self

    def add_script(self, src: Optional[str] = None, content: Optional[str] = None, **attributes) -> "Body":
        """
        Добавить script в конец body

        Пример:
        body.add_script_footer(src="app.js", defer=True)
        """
        script_attrs = attributes
        if src:
            script_attrs["src"] = src
        if content:
            script_attrs["_content"] = content
        self.scripts_footer.append(script_attrs)
        return self

    def _get_scripts_footer_str(self) -> str:
        """Рендеринг скриптов в конце body"""
        scripts = []
        for script in self.scripts_footer:
            content = script.pop("_content", None)
            attrs = " ".join(f'{k}="{v}"' for k, v in script.items() if not k.startswith("_"))

            if content:
                scripts.append(f"<script {attrs}>\n{content}\n</script>")
            else:
                scripts.append(f"<script {attrs}></script>")

        return "\n    ".join(scripts)

    def get_html(self):
        parts = []
        parts.append(self.content)

        if self.elements:
            html_context = ""
            for element in self.elements:
                if hasattr(element, "get_html"):
                    html_context += "\n\t" + element.get_html()
                else:
                    html_context += "\n\t" + str(element)
            parts.append(html_context)

        if self.scripts_footer:
            parts.append(self._get_scripts_footer_str())

        return super().get_html(content="\n".join(parts))

    def get_styles(self, styles_type: StyleType = StyleType.EXTERNAL) -> dict:
        css_styles: dict = {}
        css_styles.update(super().get_styles(styles_type=styles_type))
        for element in self.elements:
            css_styles.update(element.get_styles(styles_type=styles_type))
        return css_styles

    def __str__(self) -> str:
        return self.get_html()

    def __repr__(self) -> str:
        return f"Body(elements={len(self.elements)}, content_length={len(self.content)})"

    def __iadd__(self, other: Any) -> "Body":
        self.add_element(other)
        return self

    def copy(self, copy_element: "Body" = None) -> "Body":
        if copy_element is None:
            copy_element = Body(object_name=self.object_name)
        super().copy(copy_element=copy_element)

        copy_element.content = self.content
        copy_element.links = deepcopy(self.links)
        copy_element.scripts_footer = deepcopy(self.scripts_footer)

        for element in self.elements:
            copy_element.add_element(element.copy())
        return copy_element
