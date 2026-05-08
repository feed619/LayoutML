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
        attrs = []
        attrs_str = super().get_attributes_string()

        if self.form_type:
            attrs.append(f'type="{self.form_type}"')
        return " ".join(attrs) + " " + attrs_str

    def copy(self, copy_element: "Form" = None) -> "Form":
        if copy_element is None:
            copy_element = Form(object_name=self.object_name)
        super().copy(copy_element=copy_element)
        copy_element.form_type = self.form_type
        return copy_element
