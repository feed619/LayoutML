from typing import List, Dict, Optional, Any
from LayoutML.base import HTMLElement


class Body(HTMLElement):
    """
    Класс для HTML body элемента
    Содержит основное содержимое страницы
    """

    def __init__(self, content: str = "", **kwargs):
        super().__init__(**kwargs)
        self.content = content
        self.elements: List = []
        self.scripts_footer: List[Dict] = []  # Скрипты в конце body

    def add_content(self, content: str) -> "Body":
        """Добавить текстовое содержимое"""
        self.content += content
        return self

    def add_element(self, element: Any) -> "Body":
        """
        Добавить HTML элемент

        Пример:
        body.add_element(div.render())
        body.add_element(str(button))
        """
        self.elements.append(element)

        if hasattr(element, "render"):
            self.elements.append(element.render())
        else:
            self.elements.append(str(element))
        return self

    def add_raw_html(self, html: str) -> "Body":
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

    def set_background(self, color: str = None, image: str = None) -> "Body":
        """Установить фон body"""
        style_parts = []

        if color:
            style_parts.append(f"background-color: {color};")

        if image:
            style_parts.append(f'background-image: url("{image}");')
            style_parts.append("background-size: cover;")
            style_parts.append("background-position: center;")

        if style_parts:
            current_style = self._attributes.get("style", "")
            new_style = " ".join(style_parts)
            if current_style:
                self._attributes["style"] = f"{current_style} {new_style}"
            else:
                self._attributes["style"] = new_style

        return self

    def _render_scripts_footer(self) -> str:
        """Рендеринг скриптов в конце body"""
        if not self.scripts_footer:
            return ""

        scripts = []
        for script in self.scripts_footer:
            content = script.pop("_content", None)
            attrs = " ".join(f'{k}="{v}"' for k, v in script.items() if not k.startswith("_"))

            if content:
                scripts.append(f"<script {attrs}>\n{content}\n</script>")
            else:
                scripts.append(f"<script {attrs}></script>")

        return "\n    ".join(scripts)

    def render(self) -> str:
        """Рендеринг всего body"""
        # Собираем все элементы
        all_content = self.content

        if self.elements:
            html_context = ""
            for element in self.elements:
                html_context += "\n" + element.render()
            if all_content:
                all_content += "\n"
            all_content += "\n" + html_context

        # Скрипты в конце
        footer_scripts = self._render_scripts_footer()
        if footer_scripts:
            all_content += f"\n{footer_scripts}"

        # Атрибуты body
        attrs = self.get_attributes_string()

        if attrs:
            return f"<body {attrs}>\n{all_content}\n</body>"
        else:
            return f"<body>\n{all_content}\n</body>"

    def get_html(self) -> str:
        """Алиас для render"""
        return self.render()

    def __str__(self) -> str:
        return self.render()

    def __repr__(self) -> str:
        return f"Body(elements={len(self.elements)}, content_length={len(self.content)})"

    def __iadd__(self, other: Any) -> "Body":
        """Перегрузка оператора += для удобного добавления"""
        self.add_element(other)
        return self
