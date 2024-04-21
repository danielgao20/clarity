import reflex as rx

def home() -> rx.Component:
    """ Home page with a button to start the medical assessment. """
    return rx.center(
        rx.vstack(
            rx.image(src="/logo.svg", width="5em"),  # Logo centered at the top of the stack
            rx.text(
                "How can I help?", 
                size="8", 
                font_family="Metropolis", 
                font_weight="bold",
            ),
            rx.text(
                "Don’t panic! Everything will be okay. Press the ", 
                rx.chakra.span("Start Assessment ", color="blue", font_style="italic"),
                "button to begin the remote checkup.",
                align="center", 
                size="6",
                width="800px",
            ),
            rx.button(
                "Start Assessment",
                on_click=lambda: rx.redirect("/assessment"),
                size="3",
                font_family="Metropolis",
                background_color="#1B3EF3",
            ),
            align="center",
            spacing="7",
            font_family="Metropolis",
        ),
        rx.image(src="/logo.svg", width="5em", position="absolute", top="100px", right="100px"),

        height="100vh",
    )

app = rx.App()
app.add_page(home)

