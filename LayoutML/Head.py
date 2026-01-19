from typing import List, Dict, Optional, Any

from .base.css import CSSInput
from .base import HTMLElement


class Head(HTMLElement):
    """
    Класс для HTML head элемента
    """

    object_type: str

    def __init__(self, title: str = "", object_name=None, **kwargs):
        super().__init__(object_name=object_name, **kwargs)

        self.object_type = "Head"
        self.input_styles = CSSInput()

        self.title = title
        self.meta_tags: List[Dict] = []
        self.links: List[Dict] = []
        self.scripts: List[Dict] = []
        self.styles_css: List[str] = []

        self.base_url: Optional[str] = None

        # Стандартные мета-теги по умолчанию
        self.add_meta(charset="UTF-8")
        self.add_meta(name="viewport", content="width=device-width, initial-scale=1.0")

    def set_title(self, title: str) -> "Head":
        """Установить заголовок страницы"""
        self.title = title
        return self

    def add_meta(self, **attributes) -> "Head":
        """
        Добавить мета-тег

        Примеры:
        - add_meta(charset="UTF-8")
        - add_meta(name="description", content="Описание сайта")
        - add_meta(name="keywords", content="ключевые, слова")
        - add_meta(property="og:title", content="Заголовок для соц. сетей")
        """
        self.meta_tags.append(attributes)
        return self

    def add_link(self, rel: str, href: str, **attributes) -> "Head":
        """
        Добавить link тег

        Примеры:
        - add_link(rel="stylesheet", href="style.css")
        - add_link(rel="icon", href="favicon.ico", type="image/x-icon")
        - add_link(rel="canonical", href="https://example.com")
        """
        link_attrs = {"rel": rel, "href": href, **attributes}
        self.links.append(link_attrs)
        return self

    def add_style_css(self, css: str) -> "Head":
        """
        Добавить встроенные стили

        Пример:
        add_style("body { margin: 0; }")
        """
        self.styles_css.append(css)
        return self

    def add_script(self, src: Optional[str] = None, content: Optional[str] = None, **attributes) -> "Head":
        """
        Добавить script тег

        Примеры:
        - add_script(src="app.js", defer=True)
        - add_script(content="console.log('Hello');", type="module")
        """
        script_attrs = attributes
        if src:
            script_attrs["src"] = src
        if content:
            script_attrs["_content"] = content
        self.scripts.append(script_attrs)
        return self

    def set_base(self, url: str, target: str = "_blank") -> "Head":
        """
        Установить базовый URL

        Пример:
        set_base("https://example.com/")
        """
        self.base_url = url
        self.add_base(url, target)
        return self

    def add_base(self, href: str, target: str = "_blank") -> "Head":
        """Добавить base тег"""
        self.base_url = href
        # Base обычно один, но храним в links для унификации
        self.links.append({"rel": "base", "href": href, "target": target})
        return self

    def add_icon(self, href: str, type: str = "image/x-icon") -> "Head":
        """Добавить фавиконку"""
        self.add_link(rel="icon", href=href, type=type)
        return self

    def add_stylesheet(self, href: str, media: str = "all") -> "Head":
        """Добавить CSS файл"""
        self.add_link(rel="stylesheet", href=href, media=media)
        return self

    def add_preconnect(self, url: str) -> "Head":
        """Добавить предварительное подключение к домену"""
        self.add_link(rel="preconnect", href=url)
        return self

    def add_preload(self, href: str, as_type: str, **attributes) -> "Head":
        """Добавить предзагрузку ресурса"""
        self.add_link(rel="preload", href=href, as_=as_type, **attributes)
        return self

    def _render_meta(self) -> str:
        """Рендеринг мета-тегов"""
        meta_tags = []
        for meta in self.meta_tags:
            attrs = " ".join(f'{k}="{v}"' for k, v in meta.items())
            meta_tags.append(f"<meta {attrs}>")
        return "\n    ".join(meta_tags)

    def _render_links(self) -> str:
        """Рендеринг link тегов"""
        links = []
        for link in self.links:
            if link.get("rel") == "base":
                # Base тег рендерится отдельно
                attrs = f'href="{link["href"]}"'
                if "target" in link:
                    attrs += f' target="{link["target"]}"'
                links.append(f"<base {attrs}>")
            else:
                attrs_dict = {k: v for k, v in link.items() if not k.startswith("_")}
                attrs = " ".join(f'{k}="{v}"' for k, v in attrs_dict.items())
                links.append(f"<link {attrs}>")
        return "\n    ".join(links)

    def _render_scripts(self) -> str:
        """Рендеринг script тегов"""
        scripts = []
        for script in self.scripts:
            content = script.pop("_content", None)
            attrs = " ".join(f'{k}="{v}"' for k, v in script.items() if not k.startswith("_"))

            if content:
                scripts.append(f"<script {attrs}>\n{content}\n</script>")
            else:
                scripts.append(f"<script {attrs}></script>")
        return "\n    ".join(scripts)

    def _render_styles(self) -> str:
        """Рендеринг встроенных стилей"""
        if not self.styles_css:
            return ""

        style_content = "\n".join(self.styles_css)
        return f"<style>\n{style_content}\n</style>"

    def render(self) -> str:
        """Рендеринг всего head"""
        parts = []

        # Заголовок
        if self.title:
            parts.append(f"<title>{self.title}</title>")

        # Мета-теги
        meta_tags = self._render_meta()
        if meta_tags:
            parts.append(meta_tags)

        # Link теги (включая base)
        links = self._render_links()
        if links:
            parts.append(links)

        # Встроенные стили
        styles = self._render_styles()
        if styles:
            parts.append(styles)

        # Script теги в head
        scripts = self._render_scripts()
        if scripts:
            parts.append(scripts)
        # Атрибуты самого head
        attrs = self.get_attributes_string()
        if attrs:
            content = "\n    ".join(parts)
            return f"<head {attrs}>{self.input_styles.render()}\n    {content}\n</head>"
        else:
            content = "\n    ".join(parts)
            return f"<head>{self.input_styles.render()}\n    {content}\n</head>"

    def get_html(self) -> str:
        """Алиас для render"""
        return self.render()

    def __str__(self) -> str:
        return self.render()

    def __repr__(self) -> str:
        return f'Head(title="{self.title}", meta_count={len(self.meta_tags)})'
