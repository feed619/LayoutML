from layoutml.base import BaseElement


class Image(BaseElement):
    """
    Элемент изображения <img>
    """

    def __init__(self, src, alt="", object_name=None, style=None, boolean_attributes=[], **kwargs):
        super().__init__(
            tag="img",
            self_closing=True,
            object_name=object_name,
            style=style,
            boolean_attributes=boolean_attributes,
            **kwargs,
        )
        self.object_type = "ImageElement"
        self.src = src
        self.alt = alt

    def get_attributes_string(self):
        attrs = []
        attrs_str = super().get_attributes_string()

        attrs.append(f'src="{self.src}"')
        attrs.append(f'alt="{self.alt}"')
        return " ".join(attrs) + " " + attrs_str
