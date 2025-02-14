import reflex as rx


def icon_link(icon: str, url: str, hover_color: str) -> rx.Component:
    return rx.link(
        rx.vstack(
            rx.hstack(
                rx.icon(
                    icon,
                    stroke_width="2",
                ),
                color="white",
                style={
                    "padding_top": "0.65rem",
                    "transition": "0.3s",
                    "_hover": {
                        "color": hover_color, 
                        "filter": f"drop-shadow(0px 0px 10px {hover_color})",
                        "transform": "scale(1.1)",
                    },
                }
            )
        ),
        href=url,
        is_external=True,
    )