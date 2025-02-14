import reflex as rx
from single_page_CV.components.icon_link import icon_link


def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(
                src="https://i.imgur.com/BLCc7LM.jpeg",
                radius="full",
                size="8",
            ),
            rx.heading(
                rx.text(
                    "Cristopher Fuentes",
                    size="8",
                    style={
                        "font_family": "Playfair_Display",
                        "font_weight": "bold",
                    }
                ),
                rx.text(
                    "Front-end Developer",
                    size="3",
                    color_scheme="ruby",
                    style={
                        "font_family": "Raleway",
                        "font_weight": "bold",
                    }
                ),
                rx.hstack(
                    icon_link(
                        "github",
                        "https://github.com/cris21512",
                        "#D2B48C"
                    ),
                    icon_link(
                        "mail",
                        "mailto:cristopherfm21.5@gmail.com",
                        "red"
                    ),
                    icon_link(
                        "linkedin",
                        "https://www.linkedin.com/in/cristopher-fuentes-87868534b/",
                        "#109DFA"
                    ),
                    spacing="4"
                ),
                align_items="start",
            ),
        )
    )