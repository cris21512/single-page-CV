import reflex as rx
from single_page_CV.components.title import title


def skills_links() -> rx.Component:
    return rx.vstack(
        title("Habilidades"),
        rx.hstack(
            rx.image(
                src="https://pluspng.com/img-png/python-logo-png-open-2000.png",
                style={
                    "width": "50px",
                    "height": "50px",
                    "transition": "opacity 2s, width 1s, height 1s",
                    "_hover": {
                        "filter": f"drop-shadow(0px 0px 10px #c9b977)",
                        "transform": "scale(1.1)",
                    },
                    "@starting-style": {
                        "opacity": 0,
                    }
                }
            ),
            rx.divider(orientation="vertical", size="4"),
            rx.image(
                src="https://i.imgur.com/a0WMXxl.png",
                style={
                    "width": "50px",
                    "height": "50px",
                    "transition": "opacity 2s, width 1s, height 1s",
                    "_hover": {
                        "filter": f"drop-shadow(0px 0px 10px blue)",
                        "transform": "scale(1.1)",
                    },
                    "@starting-style": {
                        "opacity": 0,
                    }
                }
            ),
            rx.divider(orientation="vertical", size="4"),
            rx.image(
                src="https://i.imgur.com/6qcN2WM.png",
                style={
                    "width": "50px",
                    "height": "50px",
                    "transition": "opacity 2s, width 1s, height 1s",
                    "_hover": {
                        "filter": f"drop-shadow(0px 0px 10px yellow)",
                        "transform": "scale(1.1)",
                    },
                    "@starting-style": {
                        "opacity": 0,
                    }
                }
            ),
        ),
        spacing="5",
        style={
            "padding_top": "1rem",
        }
    )