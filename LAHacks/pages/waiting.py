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
            rx.button(
                "Download Report",
                on_click=lambda: rx.redirect("https://drive.google.com/file/d/1obDI32xnVFmkwdviw6wJCGIOTpYBpOY-/view?usp=sharing"),
                size="3",
                font_family="Metropolis",
                background_color="#4CAF50",
            ),
            align="center",
            spacing="5"
        ),
        height="100vh"
    )

app = rx.App()
app.add_page(waiting)
