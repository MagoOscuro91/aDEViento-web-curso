import reflex as rx #6# Importamos reflex comos siempre.
from adeviento_web.styles.styles import Size, TextColor #6# Importamos la clase Size. #7# Importamos tambien el color.


#6# Creamos un componente que recive dos parametros para hacer botones de cabezeras.
def header_text(icon: str, text: str, dark=True) -> rx.Component: #7# Vengo del futuro a añadir un parametro -> dark=True que es opcional por defecto esta en true para cambiarlo es pasando el argumento con False.
    return rx.hstack( #6# Creamos un horizontal stack.
        rx.box( #6# Con un box para el icono.
            class_name=f"nes-icon is-medium {icon}" #6# El icono de nes.css icon es el parametro que recive el nombre para esta linea que cambiara el icono.
        ),
        rx.heading( #6# Una cabezera para el texto.
            text, #6# Parametro texto.
            size="7", #6# Tamaño.
            color=TextColor.ACCENT.value if dark else TextColor.SECONDARY.value, #7# Con esta condicion si el 3 argumento es False pondra secondaro si es true accent.
            padding_top="0.40em" #P#6# Esta linea es personal para alinear el icono con el texto ami gusto.
        ),
        spacing="3", #E#6# 1em no funciona.Vamos a darle un espacio al hstack.
        padding_bottom=Size.DEFAULT.value #6# Vamos a darle margen inferior al hstack.
    )
