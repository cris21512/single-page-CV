import reflex as rx
from single_page_CV.components.button_icon import button_icon


def mis_proyectos() -> rx.Component:
    return rx.vstack(
        button_icon(
            "github",
            "Mi Github",
            "Aqui encontraras todos mis proyectos personales", 
            "https://github.com/cris21512"   
        )
    )
