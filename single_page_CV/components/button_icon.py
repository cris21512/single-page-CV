import reflex as rx
import single_page_CV.styles.styles as styles


def button_icon(icon: str,title: str, body: str, url: str) -> rx.Component:
    return rx.link(
        rx.card(
            rx.hstack(
                rx.icon(
                    icon,
                    stroke_width="2",
                    size=50,
                ),
                rx.text(title, style=styles.body_styles),
                rx.text(body, style=styles.body_styles)
            )
        ),
        href=url,
        is_external=True,
        style={
            "margin": "1.5rem",
        }
    )
