import reflex as rx
import adeviento_web.styles.styles as styles
from adeviento_web.styles.styles import Color, Size
from adeviento_web.components.header_text import header_text


def partners() -> rx.Component:
    return rx.vstack( #7# Vstack principal para cubrir todo el arear con el fondo rojo.
        rx.vstack( #7# Vstack secundario este limitado de tamaño donde pondremos los items.
            header_text( #7# Nuestro costructor de cabezera.
                "star", #7# Argumento icon.
                "Patrocinado por", #7# Argumento text.
                False #7# Tercer argumento opcional en False para que el costructor de cabezera no la pinte roja como teniamos antes.
            ),
            rx.text(
                "Mis perro chispi."
            ),
            rx.text(
                "Mi familia."
            ),
            spacing="2",
            padding_y=Size.VERY_BIG.value, #7# Padding del eje y para que separe a los dos lados.
            style=styles.max_width_style
        ),
        bg=Color.ACCENT.value, #7# Fondo rojo.
        width="100%", #7# Tamaño total del vstack principal.
        align_items="center" #P#7# E añadido esta linea por que en fullscreen salia pegado a la iz.
    )
