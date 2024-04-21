import threading
import reflex as rx

# def redirect():
#     print("5 seconds")
#     rx.redirect("/home")

def loading4() -> rx.Component:

    js_redirect = """
    <script>
        setTimeout(function() {
            window.location.href = '/a5'; // Adjust the URL as necessary
        }, 1000);
    </script>
    """

    # threading.Timer(5.0, redirect).start()

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
            rx.html(js_redirect),
        ),
        height="100vh",
        align="center",
        spacing="7",
    ),

app = rx.App()
app.add_page(loading4)

