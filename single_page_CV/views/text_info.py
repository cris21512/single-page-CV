import reflex as rx
from single_page_CV.components.title import title
import single_page_CV.styles.styles as styles


def experience_info() -> rx.Component:
    return rx.vstack(
        title("Experiencia"),
        rx.text(
            """ Al ser tan joven y tan nuevo en el sector, no tengo experiencia laboral como tal...
            Mi experiencia se basa en mis proyectos personales y habilidades para resolver problemas si los hubieran.
            """,
            style=styles.body_styles,
        ),
        style={
            "padding_top": "1rem",
        }
    )
