import reflex as rx

def loading() -> rx.Component:
    """ Home page with a button to start the medical assessment. """
    return rx.center(
        rx.vstack(
            rx.image(src="/loading.gif", width="10em", align="center",),
            rx.text(
                "Waiting for ", 
                rx.chakra.span("Clarity ", color="blue", ),
                "to find the right question...",
                size="6",
                align="center",
                width="800px",
            ),
        ),
        height="100vh",
        align="center",
        spacing="7",
    ),

app = rx.App()
app.add_page(loading)

