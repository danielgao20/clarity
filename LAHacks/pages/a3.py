import reflex as rx
from LAHacks.components import audio_capture

def a3() -> rx.Component:
    """ Second text input question """
    question = "How long have you been experiencing these symptoms?"
    return rx.center(
        rx.vstack(
            rx.image(src="/logo.svg", width="5em", margin_top="50px"),
            rx.text(
                "How long have you been experiencing these symptoms?", 
                size="8", 
                font_family="Metropolis", 
                font_weight="bold",
                margin_top="20px"),  # Maintain margin_top for space between logo and text
            rx.text(
                "Describe your symptoms in detail:",
                align="center", 
                size="6",
                width="800px",),
            audio_capture.index(),  # Audio Recording
            rx.button(
                "Submit",
                on_click=lambda: rx.redirect("/loading3"),
                size="3",
                font_family="Metropolis",
                background_color="#1B3EF3",
            ),
            align="center",
            spacing="5"
        ),
        align="center",
        spacing="7",
        overflow="auto",
    )


app = rx.App()
app.add_page(a3)