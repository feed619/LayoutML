from layoutml.base import BaseElement


class ListElement(BaseElement):
    """
    Базовый класс для списков
    """

    def __init__(self, tag, items=None, object_name=None, style=None, boolean_attributes=[], **kwargs):
        super().__init__(
            tag=tag,
            self_closing=False,
            object_name=object_name,
            style=style,
            boolean_attributes=boolean_attributes,
            **kwargs,
        )
        self.items = items or []

    def add_item(self, item):
        """
        Добавляет элемент в список
        """
        self.items.append(item)

    def get_html(self, content: str = "", tab: int = 0):
        # Формируем элементы списка
        list_items = ""
        for item in self.items:
            if isinstance(item, str):
                list_items += f"{'    '*(tab+1)}<li>{item}</li>\n"
            else:
                list_items += item.get_html(tab=tab + 1) + "\n"

        if list_items:
            content = f"\n{list_items}{'    '*tab}"
        return super().get_html(content=content, tab=tab)
