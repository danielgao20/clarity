import reflex as rx
from LAHacks.components import audio_capture

def a5() -> rx.Component:
    """ Fourth text input question """
    question = "Can you describe the pain intensity on a scale from 1 to 10?"
    return rx.center(
        rx.vstack(
            rx.image(src="/logo.svg", width="5em", margin_top="50px"),
            rx.text(
                "Can you describe the pain intensity on a scale from 1 to 10?", 
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
                on_click=lambda: rx.redirect("/waiting"),
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
app.add_page(a5)