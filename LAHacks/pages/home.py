import reflex as rx

def home() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.heading("How can I help?", size="9"),
            rx.text("Don’t panic! Everything will be okay. Press the Start Assessment button to begin the remote checkup."),
            rx.button(
                "Start Assessment",
                # on_click=lambda: rx.redirect(docs_url),
                size="4",
            ),
            align="center",
            spacing="7",
            font_size="2em",
        ),
        height="100vh",
    )


app = rx.App()
app.add_page(home)
