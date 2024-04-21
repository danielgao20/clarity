import reflex as rx
from LAHacks.components import video_capture

def a3() -> rx.Component:
    """ Second text input question """
    question = "How long have you been experiencing these symptoms?"
    return rx.center(
        rx.vstack(
            rx.text(question, size="8", font_family="Metropolis", font_weight="bold", margin_top="40px"),
            rx.input(  # Adding the textbox for detailed symptom description
                placeholder="Type your symptoms here...",
                multiline=True,  # Allows for multi-line text input
                width="800px",   # Ensures the textbox aligns with the text above
                height="100px"   # Provides adequate space for detailed input
            ),
            rx.button("Next", on_click=lambda: rx.redirect("/a4")),
            align="center",
            spacing="5"
        ),
        align="center",
        spacing="7",
        overflow="auto",
    )


app = rx.App()
app.add_page(a3)