import reflex as rx
import single_page_CV.styles.styles as styles
from single_page_CV.components.title import title


def cards_buttons() -> rx.Component:
    return rx.vstack(
        rx.flex(
            rx.vstack(
                rx.card(
                    " Pais: Guatemala ",
                    style=styles.text_style
                ),
                rx.card(
                    " Ciudad: Guatemala, Villa Nueva",
                    style=styles.text_style
                ),
                rx.card(
                    " Numero telefonico: +502 3955 9554 ",
                    style=styles.text_style
                ),
                rx.card(
                    " Correo Electronico: cristopherfm21.5@gmail.com",
                    style=styles.text_style
                ),

        ),
        direction="column",
    )
)