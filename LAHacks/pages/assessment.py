import reflex as rx

def assessment() -> rx.Component:
    """ Page for collecting information about symptoms. """
    # Simple text display and a button to proceed. Actual data collection would need more functionality.
    return rx.center(
        rx.vstack(
            rx.text(
                "Please describe your symptoms", 
                size="8", 
                font_family="Metropolis", 
                font_weight="bold",),
            rx.text(
                "Describe your symptoms in detail:",
                align="center", 
                size="6",
                width="800px",),
            rx.button(
                "Submit",
                on_click=lambda: rx.redirect("/waiting"),
                size="3",
                font_family="Metropolis",
                background_color="#1B3EF3",
            ),
            align="center",
            spacing="5"
        ),
        align="center",
        spacing="7",
        height="100vh"
    )


app = rx.App()
app.add_page(assessment)

