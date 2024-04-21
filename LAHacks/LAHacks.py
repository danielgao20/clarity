"""Welcome to Reflex! This file outlines the steps to create a basic app."""

from rxconfig import config

import reflex as rx
from LAHacks.pages import a2, a3, a4, a5

from LAHacks.pages import home, assessment, waiting, loading

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
app.add_page(a2.a2)
app.add_page(a3.a3)
app.add_page(a4.a4)
app.add_page(a5.a5)
app.add_page(assessment.assessment)
app.add_page(waiting.waiting)
app.add_page(loading.loading)

