from typing import Optional

from LayoutML.base import HTMLElement
from .Body import Body
from .Head import Head


class Page(HTMLElement):
    """
    Полный HTML документ
    Объединяет Head и Body
    """

    doctype: str
    head: Head
    body: Body
    custom_prefix: Optional[str] = None
    custom_suffix: Optional[str] = None

    def __init__(self, doctype: str = "html", title: str = "LayoutML", **kwargs):
        super().__init__(**kwargs)

        self.doctype = doctype
        self.head = Head(title=title)
        self.body = Body()
        self.custom_prefix: Optional[str] = None
        self.custom_suffix: Optional[str] = None

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

    def add_prefix(self, html: str) -> "Page":
        """Добавить HTML перед документом (например, комментарии)"""
        self.custom_prefix = html
        return self

    def add_suffix(self, html: str) -> "Page":
        """Добавить HTML после документа"""
        self.custom_suffix = html
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

    def render(self) -> str:
        """Рендеринг полного HTML документа"""
        parts = []

        # Префикс (если есть)
        if self.custom_prefix:
            parts.append(self.custom_prefix)

        # Doctype
        parts.append(self._get_doctype())

        html_attrs = self.get_attributes_string()  # Если Page наследует HTMLElement
        if html_attrs:
            parts.append(f'<html" {html_attrs}>')
        else:
            parts.append(f'<html">')

        # Head
        parts.append(self.head.render())
        # Body
        parts.append(self.body.render())
        # Закрытие html тега
        parts.append("</html>")
        # Суффикс (если есть)
        if self.custom_suffix:
            parts.append(self.custom_suffix)

        return "\n".join(parts)

    def save(self, filename: str, encoding: str = "utf-8") -> None:
        """Сохранить документ в файл"""
        with open(filename, "w", encoding=encoding) as f:
            f.write(self.render())
        print(f"Документ сохранен в {filename}")

    def get_html(self) -> str:
        """Алиас для render"""
        return self.render()

    def __str__(self) -> str:
        return self.render()

    def __repr__(self) -> str:
        return f'Page(lang="{self.lang}", title="{self.head.title}")'
