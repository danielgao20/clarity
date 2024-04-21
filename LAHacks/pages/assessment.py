import reflex as rx

def assessment() -> rx.Component:
    """ Page for collecting information about symptoms. """
    # Simple text display and a button to proceed. Actual data collection would need more functionality.
    return rx.center(
        rx.vstack(
            rx.heading("Please describe your symptoms"),
            rx.text("Describe your symptoms in detail:"),
            rx.button("Submit", on_click=lambda: rx.redirect("/waiting")),
            align="center",
            spacing="5"
        ),
        height="100vh"
    )


app = rx.App()
app.add_page(assessment)

