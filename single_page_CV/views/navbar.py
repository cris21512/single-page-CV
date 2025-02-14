import reflex as rx


def navbar() -> rx.Component:
    return rx.center(
        rx.avatar(
            src="https://i.imgur.com/BLCc7LM.jpeg",
            radius="full",
            size="8",
        )
    )