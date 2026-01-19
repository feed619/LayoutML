from LayoutML.base import HTMLElement


class FormElement(HTMLElement):

    def __init__(self, form_type: str = "text", boolean_attributes=[], **kwargs):
        """ """
        super().__init__(boolean_attributes=boolean_attributes, **kwargs)

        self.object_type = "FormElement"
        self.tag = "input"
        self.form_type = form_type

    def get_attributes_string(self):
        """
        Генерирует строку специфических атрибутов формы.

        Returns
        -------
        Строку html атрибутов
        """
        attrs = []
        attrs_str = super().get_attributes_string()

        if self.form_type:
            attrs.append(f'type="{self.form_type}"')
        return " ".join(attrs) + " " + attrs_str

    def render(self) -> str:
        """Рендеринг Label"""
        attrs = self.get_attributes_string()
        if attrs:
            return f"<{self.tag} {attrs}>"
        else:
            return f"<{self.tag}>"
