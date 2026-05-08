from layoutml.base import BaseElement


class Article(BaseElement):
    """
    Семантический элемент статьи <article>
    """

    def __init__(self, object_name=None, style=None, boolean_attributes=[], **kwargs):
        super().__init__(
            tag="article",
            self_closing=False,
            object_name=object_name,
            style=style,
            boolean_attributes=boolean_attributes,
            **kwargs,
        )
        self.object_type = "ArticleElement"

    def copy(self, copy_element: "Article" = None) -> "Article":
        if not copy_element:
            copy_element = Article(object_name=self.object_name)
        super().copy(copy_element=copy_element)
        return copy_element
