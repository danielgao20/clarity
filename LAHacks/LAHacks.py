"""Welcome to Reflex! This file outlines the steps to create a basic app."""

from rxconfig import config

import reflex as rx
from LAHacks.pages import home
from LAHacks.pages import assessment
from LAHacks.pages import waiting

docs_url = "https://reflex.dev/docs/getting-started/introduction/"
filename = f"{config.app_name}/{config.app_name}.py"

def index() -> rx.Component:
    return rx.center(
        rx.theme_panel(),
        rx.vstack(
            rx.heading("Welcome to Reflex!", size="9"),
            rx.text("Get started by editing ", rx.code(filename)),
            rx.button(
                "Check out our docs!",
                on_click=lambda: rx.redirect(docs_url),
                size="4",
            ),
            rx.logo(),
            align="center",
            spacing="7",
            font_size="2em",
        ),
        height="100vh",
    )


app = rx.App(
    stylesheets=[
        "/fonts/myfont.css",  # This path is relative to assets/
    ],
)
app.add_page(index)
app.add_page(home.home)
app.add_page(assessment.assessment)
app.add_page(waiting.waiting)

