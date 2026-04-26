<p align="center">
  <img src="ico\full_logo.png" alt="LayoutML"></a>
</p>
<p align="center">
    <em>LayoutML (Layout Markup Library) is a library that allows you to describe the structure of web pages directly in code, turning Python into a markup language for web interfaces.</em>
</p>

## Key Features

- Create HTML elements using Python classes
- Define CSS styles programmatically
- Component-based approach (reusable layout blocks)
- Clean and declarative syntax
- Generate pure HTML/CSS without unnecessary code
- Easy integration with FastAPI, Flask, Django
- Lightweight with no external dependencies

## Who is it for

- Python developers who don’t want to write HTML manually
- Backend developers (FastAPI / Django / Flask)
- Educational projects
- Generating HTML reports and interfaces
- Building custom web frameworks on top of LayoutML

## Contents

### Core Classes

- [CSSBase](docs\en\base\css\CSSBase.md) - Base class for working with CSS styles
- [CSSInline](docs\en\base\css\CSSInline.md) - Class for inline styles
- [CSSSelectors](docs\en\base\css\CSSSelectors.md) - Class for managing CSS selectors

### Base Elements

- [BaseElement](docs\en\base\BaseElement.md) - Base class for all HTML elements
- [HTMLElement](docs\en\base\HTMLElement.md) - Class for handling HTML attributes

### Semantic Elements

- [Header](docs\en\elements\Header.md) - Semantic `<header>` element
- [Main](docs\en\elements\Main.md) - Semantic `<main>` element
- [Footer](docs\en\elements\Footer.md) - Semantic `<footer>` element
- [Nav](docs\en\elements\Nav.md) - Semantic `<nav>` element
- [Section](docs\en\elements\Section.md) - Semantic `<section>` element
- [Article](docs\en\elements\Article.md) - Semantic `<article>` element
- [Aside](docs\en\elements\Aside.md) - Semantic `<aside>` element

### Text Elements

- [Paragraph](docs\en\elements\Paragraph.md) - `<p>` element
- [Span](docs\en\elements\Span.md) - Inline container `<span>`
- [Anchor](docs\en\elements\Anchor.md) - Link `<a>`
- [Heading](docs\en\elements\Heading.md) - Headings `<h1>-<h6>`
- [ListElement](docs\en\elements\list\ListElement.md) - Base class for lists
- [UnorderedList](docs\en\elements\list\UnorderedList.md) - `<ul>`
- [OrderedList](docs\en\elements\list\OrderedList.md) - `<ol>`

### Media Elements

- [Image](docs\en\elements\Image.md) - `<img>`

### Form Elements

- [Form](docs\en\elements\Form.md) - Base form class
- [FormElement](docs\en\elements\FormElement.md) - `<input>`
- [Input](docs\en\elements\Input.md) - Specialized input
- [Label](docs\en\elements\Label.md) - `<label>`
- [Button](docs\en\elements\Button.md) - `<button>`
- [Select](docs\en\elements\Select.md) - `<select>`
- [Textarea](docs\en\elements\Textarea.md) - `<textarea>`

### Layout

- [Layout](docs\en\layout\Layout.md) - Base layout (Flexbox)
- [HorizontalLayout](docs\en\layout\HorizontalLayout.md) - Horizontal layout
- [VerticalLayout](docs\en\layout\VerticalLayout.md) - Vertical layout

### Document Structure

- [Head](docs\en\Head.md) - `<head>`
- [Body](docs\en\Body.md) - `<body>`
- [Page](docs\en\Page.md) - Full HTML document

### Routing

- [Router](docs\en\base\router\Router.md) - URL routing class

### Application

- [LayoutML](docs\en\LayoutML.md) - Main application class

## Quick Start

### Installation

```bash
pip install layoutml
```

## Example Usage

This section provides examples of building web applications using LayoutML. You will learn how to create pages, add elements, and run the server.

### Basic Run

The simplest way to run a LayoutML application:

```python
from layoutml import LayoutML, Page
from layoutml.elements import Header, Paragraph, Button

class BasePage(Page):
    def __init__(self, doctype="html", title="LayoutML", lang="en", object_name=None, **kwargs):
        super().__init__(doctype, title, lang, object_name, **kwargs)
        self.head.set_icon("ico/logo.ico")


# Create the application
app = LayoutML()

# Define a route
@app._router.route("/")
def home():
    page = BasePage(title="Home")

    # Create elements
    header = Header()
    header.get_html(content="<h1>Welcome!</h1>")

    paragraph = Paragraph(text="This is an example of using LayoutML")

    button = Button(text="Click me", onclick="alert('Hello!')")

    # Add elements to the page
    page.body.add_element(header)
    page.body.add_element(paragraph)
    page.body.add_element(button)

    return page

# Run the application
if __name__ == "__main__":
    app.start(host="localhost", port=3700)
```

### Running via Uvicorn from the Command Line

You can run the application using Uvicorn from the terminal:

```bash
uvicorn test:app --host localhost --port 3700 --reload
```

Where `test` is the name of your Python file, and `app` is the name of your LayoutML application instance.

### Running via Uvicorn from Python Code

You can also run Uvicorn directly from a Python script:

```python
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

### Creating Multiple Routes

Example of an application with multiple pages:

```python
from layoutml import LayoutML, Page
from layoutml.elements import Header, Paragraph, Button, Anchor

app = LayoutML()

@app.route("/")
def home():
    page = Page(title="Home")

    header = Header()
    header.get_html(content="<h1>Home Page</h1>")

    paragraph = Paragraph(text="Welcome to our website!")

    link = Anchor(href="/about", text="About Us")

    page.body.add_element(header)
    page.body.add_element(paragraph)
    page.body.add_element(link)

    return page

@app.route("/about")
def about():
    page = Page(title="About")

    header = Header()
    header.get_html(content="<h1>About Our Company</h1>")

    paragraph = Paragraph(text="We build web applications using LayoutML")

    back_link = Anchor(href="/", text="Back to Home")

    page.body.add_element(header)
    page.body.add_element(paragraph)
    page.body.add_element(back_link)

    return page

if __name__ == "__main__":
    app.start()
```

### Using Route Parameters

You can create dynamic pages with parameters in the URL:

```python
from layoutml import LayoutML, Page
from layoutml.elements import Header, Paragraph

app = LayoutML()

@app._router.route("/user/<username>")
def user_profile(username: str):
    page = Page(title=f"Profile {username}")

    header = Header()
    header.get_html(content=f"<h1>User Profile: {username}</h1>")

    paragraph = Paragraph(text=f"Welcome, {username}!")

    page.body.add_element(header)
    page.body.add_element(paragraph)

    return page

if __name__ == "__main__":
    app.start()
```

### Adding CSS Styles

Example of a page with custom styles:

```python
from layoutml import LayoutML, Page
from layoutml.elements import Header, Paragraph, Button

app = LayoutML()

@app.route("/")
def styled_page():
    page = Page(title="Styled Page")

    # Create an element with CSS classes
    header = Header(class_="main-header")
    header.get_html(content="<h1>Styled Page</h1>")

    paragraph = Paragraph(
        text="This text is styled using CSS",
        class_="highlight-text"
    )

    button = Button(
        text="Styled Button",
        class_="custom-button",
        style="padding: 10px 20px; background: #007bff; color: white; border: none; border-radius: 5px;"
    )

    # Add CSS styles via the head object
    page.head.selectors_styles.add_selector(".main-header")\
        .set_background_color("#f8f9fa")\
        .set_padding("20px")\
        .set_text_align("center")

    page.head.selectors_styles.add_selector(".highlight-text")\
        .set_color("#007bff")\
        .set_font_size("18px")\
        .set_font_weight("bold")

    page.head.selectors_styles.add_selector(".custom-button:hover")\
        .set_background_color("#0056b3")\
        .set_transform("scale(1.05)")

    page.body.add_element(header)
    page.body.add_element(paragraph)
    page.body.add_element(button)

    return page

if __name__ == "__main__":
    app.start()
```

### Using Layouts

Creating a page using horizontal and vertical layouts:

```python
from layoutml import LayoutML, Page
from layoutml.elements import Header, Paragraph, Button
from layoutml.layout import HorizontalLayout, VerticalLayout

app = LayoutML()

@app.route("/")
def layout_example():
    page = Page(title="Layout Example")

    # Vertical layout for the entire page
    main_layout = VerticalLayout(object_name="mainLayout")
    main_layout.object_styles.set_gap("20px").set_padding("20px")

    # Horizontal layout for navigation
    nav_layout = HorizontalLayout(object_name="navLayout")
    nav_layout.object_styles.set_justify_content("space-between")

    nav_layout.add_element(Button(text="Home"))
    nav_layout.add_element(Button(text="About"))
    nav_layout.add_element(Button(text="Contacts"))

    # Horizontal layout for cards
    cards_layout = HorizontalLayout(object_name="cardsLayout")
    cards_layout.object_styles.set_gap("20px").set_justify_content("center")

    for i in range(3):
        card = VerticalLayout(object_name=f"card{i}")
        card.object_styles.set_border("1px solid #ddd")\
                          .set_padding("15px")\
                          .set_border_radius("8px")\
                          .set_width("200px")

        card.add_element(Paragraph(text=f"Card {i+1}"))
        card.add_element(Button(text="Learn More"))
        cards_layout.add_element(card)

    main_layout.add_elements(nav_layout, cards_layout)
    page.body.add_element(main_layout)

    return page

if __name__ == "__main__":
    app.start()
```

### Handling Forms

Example of creating a page with a form and handling data:

```python
from layoutml import LayoutML, Page
from layoutml.elements import Input, Button, Label, Paragraph

app = LayoutML()

@app.route("/contact", methods=["GET", "POST"])
def contact_page():
    page = Page(title="Contacts")

    page.body.add_element(Paragraph(text="Get in touch with us"))

    # Create a form
    form = BaseElement(tag="form", method="post", action="/submit")

    # Name field
    form.add_element(Label(for_id="name", text="Name:"))
    form.add_element(Input(id="name", name="name", required=True))

    # Email field
    form.add_element(Label(for_id="email", text="Email:"))
    form.add_element(Input(type="email", id="email", name="email", required=True))

    # Submit button
    form.add_element(Button(text="Submit", type="submit"))

    page.body.add_element(form)

    return page

if __name__ == "__main__":
    app.start()
```

## Development Tips

1. **Development mode:** Use the `--reload` flag when running via Uvicorn for automatic server reload on code changes.

2. **Debugging:** You can print route information using the `print_routes()` method:

```python
app.print_routes()
```

3. **Code organization:** For larger applications, it is recommended to split routes into modules:

```python
# routes.py
from layoutml import LayoutML

app = LayoutML()

# Import routes from other modules
from .home_routes import home_router
from .api_routes import api_router

app.include_router(home_router)
app.include_router(api_router, prefix="/api")
```

4. **Asynchronous handlers:** LayoutML supports async functions for route handling:

```python
@app.route("/async-data")
async def async_data():
    data = await fetch_data_from_db()
    page = Page(title="Data")
    page.body.add_element(Paragraph(text=str(data)))
    return page
```

---

))())()()()
After запуск the server will be available at http://localhost:3700

## Project Status

LayoutML is under active development.

## 📄 License

[MIT License](LICENSE)

## Feedback

I am always happy to receive your feedback and suggestions for improving LayoutML. Please leave your comments.

- [Email](mailto:feed619pro@gmail.com)
