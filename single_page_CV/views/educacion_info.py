import reflex as rx
from single_page_CV.components.title import title
import single_page_CV.styles.styles as styles


def educacion_info() -> rx.Component:
    return rx.vstack(
        title("Educacion"),
        rx.blockquote(
            "Soy autodidacta, mis conocimientos los adquiri de cursos online, y de las documentaciones.",
            style=styles.body_styles,
        ),
        rx.blockquote(
            "En la parte Front-end tengo conocimiento en CSS, en Back-end tengo conocimiento en python, y dockerfile, y actualmente estoy aprendiendo JavaScript.",
            style=styles.body_styles,
        ),
        style={
            "padding_top": "1rem",
        }
    )