import reflex as rx

def waiting() -> rx.Component:
    """ Thank you page after submitting the assessment. """
    return rx.center(
        rx.vstack(
            rx.heading("Thank you!", size="6"),
            rx.text("Please wait as a doctor reviews your information and gets back to you."),
            align="center",
            spacing="5"
        ),
        height="100vh"
    )


app = rx.App()
app.add_page(waiting)

