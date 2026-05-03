from layoutml import Page
from layoutml.elements import Header, Paragraph, Anchor, Button
from layoutml.layout import VerticalLayout, HorizontalLayout


def get_404_page():
    page = Page(title="404 - Страница не найдена", object_name="error_page", lang="ru")
    page.body.object_styles.remove_padding_margin()

    container = VerticalLayout(object_name="errorContainer")
    container.object_styles.set_min_height("100vh").set_display("flex").set_justify_content("center").set_align_items("center").set_background(
        "linear-gradient(135deg, #667eea 0%, #764ba2 100%)"
    ).set_margin("0").set_padding("20px")

    error_card = VerticalLayout(object_name="errorCard")
    error_card.object_styles.set_background_color("white").set_border_radius("20px").set_padding("50px 40px").set_box_shadow(
        "0 20px 60px rgba(0,0,0,0.3)"
    ).set_text_align("center").set_max_width("500px").set_width("100%")

    description = Paragraph(text="Unfortunately, the requested page does not exist or has been moved.")
    description.object_styles.set_color("#666").set_margin_bottom("30px")

    home_button = Button(text="🏠 На главную", class_="home-button", onclick="window.location.href='/'")
    home_button.object_styles.set_background_color("#667eea").set_color("white").set_border("none").set_padding("12px 30px").set_border_radius(
        "50px"
    ).set_font_size("16px").set_cursor("pointer").set_transition("transform 0.3s, box-shadow 0.3s")

    home_button.selectors_styles.add_selector(".home-button:hover").set_transform("translateY(-2px)").set_box_shadow(
        "0 5px 20px rgba(102,126,234,0.4)"
    )

    error_card.add_elements(description, home_button)
    container.add_element(error_card)
    page.body.add_element(container)

    return page
