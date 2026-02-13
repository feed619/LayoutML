from layoutml.base import BaseElement


class Form(BaseElement):

    def __init__(self, form_type: str = "text", object_name=None, style=None, boolean_attributes=[], **kwargs):
        """ """

        super().__init__(
            tag="input",
            self_closing=True,
            object_name=object_name,
            style=style,
            boolean_attributes=boolean_attributes,
            **kwargs,
        )

        self.object_type = "FormElement"
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
