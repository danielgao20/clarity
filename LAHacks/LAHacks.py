from rxconfig import config

import reflex as rx
from LAHacks.pages import home, a2, a3, a4, a5
from LAHacks.pages import assessment, waiting, loading
from LAHacks.pages import loading2, loading3, loading4, loading5

docs_url = "https://reflex.dev/docs/getting-started/introduction/"
filename = f"{config.app_name}/{config.app_name}.py"

def index() -> rx.Component:
    # Attempt to redirect to the home page automatically
    rx.redirect("/home")
    return rx.center(
        rx.vstack(
            rx.heading("Redirecting...", size="9"),
            rx.text("You are being automatically redirected to the home page. If not redirected, click below.", size="4"),
            rx.button(
                "Go to Home",
                on_click=lambda: rx.redirect("/home"),
                size="4",
                font_family="Metropolis",
                background_color="#4CAF50",
                font_weight="bold",
            ),
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

