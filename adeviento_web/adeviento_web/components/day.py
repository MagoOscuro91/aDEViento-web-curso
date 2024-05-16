import reflex as rx #8# .
from adeviento_web.styles.styles import Size, TextColor #8# .
from adeviento_web.styles.colors import Color #8# .


#8# Day una funcion que devuelve un componente rx que recibe 3 args el numero la imagen a mostrar y la url.
def day(number: int, image: str = "gift_re.png", url: str = "", finished=False) -> rx.Component:
    return rx.box( #8# Un box con.
        rx.cond( #8# Cound es un condicional en reflex
            url != "", #8# Si la url es distinto de vacio siguiente linea.
            rx.link( #8# En esta linea se llega si la anterior se cumple y se pinta un link con.
                rx.image( #8# Una imagen.
                    src=image, #8# Esta seria el arg image (donde esta ubiada)
                    alt=f"Regalo asociado al dia {number}" #8# Siempre le metemos un alt a cada imagen (Description).
                ),
                href=url, #8# La url (arg) que nos pasan al parametro url.
                is_external=True, #8# Que lo abra en una pestaña nueva.
                position="absolute", #8# Posicion absoluta para que lo pinte todo uno encima de otro.
                margin="5px" #8# Un poco de margen en la imagen.
            )
        ),
        rx.cond( #8# Cound es un condicional en reflex
            url == "", #8# Si la url es de vacio siguiente linea.
            #8# En esta linea se llega si la anterior se cumple y se pinta.
            rx.image( #8# Una imagen.
                src=image, #8# Esta seria el arg image (donde esta ubiada)
                alt=f"Regalo asociado al dia {number}", #8# Siempre le metemos un alt a cada imagen (Description).
                position="absolute", #8# Posicion absoluta para que lo pinte todo uno encima de otro.
                padding="5px"
            )
        ),
        rx.text(
            number, #8# En este texto pintamos el arg number.
            margin="2px", #8# le damos un poco de margin antes era padding "1em".
            position="absolute" #8# Posicion absoluta para que lo pinte todo uno encima de otro.
        ),
        bg=Color.ACCENT.value if finished else Color.TERTIARY.value if url != "" else Color.SECONDARY.value, #8# Color de fondo rojo.
        width="100%", ## Como va a ser responsive que ocupe todo.
        aspect_ratio="1", ## Aspect_ratio para que mantenga relacion de altura en base a el ancho.
        postion="relative" ## Como lo demas era absoluta esta va a ser la relativa.
    )
