import reflex as rx

def waiting() -> rx.Component:
    """ Thank you page after submitting the assessment. """
    return rx.center(
        rx.vstack(
            rx.text(
                "Thank you!", 
                size="8", 
                font_family="Metropolis", 
                font_weight="bold",),
            rx.text(
                "Please wait as a doctor reviews your information and gets back to you.",
                align="center", 
                size="6",
                width="800px",),
            align="center",
            spacing="5"
        ),
        height="100vh"
    )


app = rx.App()
app.add_page(waiting)

