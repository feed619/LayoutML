from typing import Optional

from layoutml.base import HTMLElement, BaseElement
from .Body import Body
from .Head import Head


class Page(BaseElement):
    """
    Полный HTML документ
    Объединяет Head и Body
    """

    object_type: str

    doctype: str
    head: Head
    body: Body

    def __init__(self, doctype: str = "html", title: str = "LayoutML", lang="ru", object_name=None, **kwargs):
        super().__init__(tag="html", object_name=object_name, lang=lang, **kwargs)

        self.object_type = "Page"
        self.doctype = doctype
        self.head = Head(title=title)
        self.body = Body()

    def set_head(self, head: Head) -> "Page":
        self.head = head
        return self

    def set_body(self, body: Body) -> "Page":
        self.body = body
        return self

    def set_doctype(self, doctype: str) -> "Page":
        """
        Установить doctype
        """
        self.doctype = doctype
        return self

    def set_language(self, lang: str) -> "Page":
        """Установить язык документа"""
        self.add_attributes(lang=lang)
        return self

    def _get_doctype(self) -> str:
        """Получить строку doctype"""
        doctypes = {
            "html": "<!DOCTYPE html>",
            "html5": "<!DOCTYPE html>",
            "xhtml": '<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">',
            "strict": '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">',
            "transitional": '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">',
        }
        return doctypes.get(self.doctype, "<!DOCTYPE html>")

    def get_css_text(self) -> str:
        css_styles: dict = self.body.get_styles()
        css_text: str = ""
        for selector_name, css in css_styles.items():
            css_text += f"{selector_name} " + "{\n" + css + "}\n"

        return css_text

    def render(self) -> str:
        """Рендеринг полного HTML документа"""

        css_text = self.get_css_text()
        if css_text:
            css_file_name = f"styles/{self.body.object_name}.css" if self.body.object_name else f"styles/{self.body.object_type}.css"
            with open(css_file_name, "w") as f:
                f.write(css_text)
            self.head.add_stylesheet(css_file_name)

        return self.get_html()

    def create_css(self):
        pass

    def get_styles(self):

        css_styles: dict = {}
        css_styles.update(super().get_styles())
        css_styles.update(self.head.get_styles())
        css_styles.update(self.body.get_styles())

        return css_styles

    def get_html(self):
        parts = []
        parts.append(self._get_doctype())

        attrs = self.get_attributes_string()
        parts.append(f"<{self.tag} {attrs}>")

        parts.append(self.head.get_html())
        parts.append(self.body.get_html())

        parts.append("</html>")

        return "\n".join(parts)

    def save(self, filename: str, encoding: str = "utf-8") -> None:
        """Сохранить документ в файл"""
        with open(filename, "w", encoding=encoding) as f:
            f.write(self.get_html())
        print(f"Документ сохранен в {filename}")

    def __str__(self) -> str:
        return self.get_html()

    def __repr__(self) -> str:
        return f'{self.get_object_name()}", title="{self.head.title}")'
