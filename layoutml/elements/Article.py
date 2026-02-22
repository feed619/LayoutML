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
