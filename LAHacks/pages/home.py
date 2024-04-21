import reflex as rx

def home() -> rx.Component:
    """ Home page with a button to start the medical assessment. """
    return rx.center(
        rx.vstack(
            rx.heading("How can I help?", size="9"),
            rx.text("Don’t panic! Everything will be okay. Press the Start Assessment button to begin the remote checkup."),
            rx.button("Start Assessment", on_click=lambda: rx.redirect("/assessment")),
            align="center",
            spacing="7",
            font_size="2em",
        ),
        height="100vh"
    )

app = rx.App()
app.add_page(home)

