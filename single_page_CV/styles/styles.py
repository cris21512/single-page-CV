import enum as Enum
import reflex as rx






BASE_STYLE={
    "background_color": "hsla(198, 14%, 16%, 1)",
    "background_image": "radial-gradient(circle at 98% 98%, hsla(55.58823529411776, 0%, 100%, 0.86) 2%, transparent 78.72573401919361%), radial-gradient(circle at 98% 91%, hsla(284.55882352941177, 85%, 73%, 0.42) 2%, transparent 78.72573401919361%), radial-gradient(circle at 16% 87%, hsla(181.00000000000003, 85%, 73%, 0.42) 2%, transparent 61.288600779667334%), radial-gradient(circle at 52% 79%, hsla(177.3529411764706, 0%, 0%, 0.37) 2%, transparent 61.288600779667334%), radial-gradient(circle at 90% 52%, hsla(2.647058823529447, 4%, 0%, 0.42) 2%, transparent 61.288600779667334%)",
    "background_blend_mode": "overlay, normal, normal, normal, normal",
    rx.card: {
        "width": "100%",
        "height": "100%",
        "padding": "0.5rem",
        "display": "block",
        "color": "#8c8c8c",
        "border": "2px solid  #020202",
        "background_color": "#rgba(0, 0, 0, 0.3)",
        "transition" : "0.4s",
        "_hover": {
            "color": "white",
            "transform": "scale(1.1)",
            "background": "#23BAC4"
        },
        "max_width": "26rem",
        "margin_top": "0.65rem",
    },
}


text_style={
    "font_family": "Lora",
    "font_size": "1.5em",
}

title_style= {
    "font_family": "Playfair_Display",
    "font_size": "2em",
    "color": "#DAA060",
}

body_styles={
    "max_width": "26rem",
    "font_family": "Alegreya",
    "font_size": "1.2em",
    "color": "#f0ebd7",
}
