import reflex as rx
from single_page_CV.cards.cards import cards_buttons
from single_page_CV.header.header import header
import single_page_CV.styles.styles as styles
from single_page_CV.components.skills import skills_links
from single_page_CV.views.text_info import experience_info
from single_page_CV.views.educacion_info import educacion_info
from single_page_CV.views.mi_github import mis_proyectos



def index() -> rx.Component:
    return rx.center(
        rx.vstack(
            header(),
            rx.hstack(
                cards_buttons(),
            ),
            skills_links(),
            educacion_info(),
            experience_info(),
            mis_proyectos(),
        ),
        padding_top="1rem",
        width="100%"
    )

app = rx.App(
    style=styles.BASE_STYLE
)
app.add_page(index)
