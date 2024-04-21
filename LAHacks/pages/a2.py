import reflex as rx
from LAHacks.components import video_capture

def a2() -> rx.Component:
    """ Video capture """
    return rx.center(
        rx.vstack(
            rx.image(src="/logo.svg", width="5em", margin_top="50px"), 
            rx.text("Please record a video of your injuries, show as many angles as you can.", size="8", font_family="Metropolis", font_weight="bold", margin_top="40px"),
            video_capture.index(),  # Adjust this part as needed
            rx.button("Next", on_click=lambda: rx.redirect("/a3")),
            align="center",
            spacing="5"
        ),
        align="center",
        spacing="7",
        overflow="auto",
    )


app = rx.App()
app.add_page(a2)

