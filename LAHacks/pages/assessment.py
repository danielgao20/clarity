import reflex as rx

from LAHacks.components import audio_capture, video_capture

def assessment() -> rx.Component:
    """ Page for collecting information about symptoms. """
    # Simple text display and a button to proceed. Actual data collection would need more functionality.
    return rx.center(
        rx.vstack(
            rx.text(
                "Please describe your symptoms", 
                size="8", 
                font_family="Metropolis", 
                font_weight="bold",
                margin_top="40px"),
            rx.text(
                "Describe your symptoms in detail:",
                align="center", 
                size="6",
                width="800px",),
            # Audio Recording
            audio_capture.index(),
            #Video Recording
            # video_capture.index(),
            rx.button(
                "Submit",
                on_click=lambda: rx.redirect("/a2"),
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
app.add_page(assessment)

