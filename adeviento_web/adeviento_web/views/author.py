import reflex as rx #6# Importamos reflex comos siempre.
import datetime #6# Importamos datetime de python.
import adeviento_web.constants as constants #6# Importamos constantes para urls.
import adeviento_web.styles.styles as styles #6# Importamos nuestros estilos.
from adeviento_web.components.header_text import header_text #6# Importamos header text que emos creado.
from adeviento_web.components.button import button #6# Importamos button.
from adeviento_web.styles.styles import Size, Color, TextColor #6# Importamos Size, TextColor y Color.


#6# Creamos un componente para author.
def author() -> rx.Component:
    return rx.vstack( #6# Montamos la estructura basica de un hstack dentro de un vstack.
        header_text( #6# Nuestro componente header_text.
            "like", #6# El parametro icon de nuestro componente header_text.
            "Hola, mi nombre es Jonathan Barbellido" #6# El parametro text de nuestro componente header_text.
        ),
        rx.flex( #E#6# E cambiado este componente a flex por que sale en el codigo de github y e estado provando para el texto triple.
            rx.avatar( #6# Componente reflex para avatares.
                name="MagoOscuro91", #6# Un avatar puede tener diferentes componentes como este el nombre.
                size="7", #E#6# Tamaño de avatar.2xl no funciona.
                src="mago_toon_red_eyes.jpg", #6# La imagen de mi avatar.
                bg=Color.PRIMARY.value, #6# Color del fondo backgraund
                padding="2px", #6# Separacion.
                border="4px", #T#6# No funciona esta linea.Establecer el grosor del borde.
                border_color=Color.SECONDARY.value #T#6# No funciona esta linea.Establecer el color del borde.
            ),
            rx.vstack( #6# Creamos un vstack dentro de este hstack superior.
                rx.text(
                    f"Soy desarrollador de software junior desde hace casi {experience()} año."
                ), #6# Aqui moure pone rx.span().
                rx.text( #T#6# Arreglar que estos 3 textos sean 1.
                    "En 2023 comencé a divulgar contenido sobre programación y desarrollo de software en redes sociales como ", #T#6# Arreglar que estos 3 textos sean 1.
                    rx.text( #T#6# Arreglar que estos 3 textos sean 1.
                        "@MagoOscuro91", #T#6# Arreglar que estos 3 textos sean 1.
                        color=TextColor.ACCENT.value, #T#6# Arreglar que estos 3 textos sean 1.
                        font_size=Size.DEFAULT.value #T#6# Arreglar que estos 3 textos sean 1.
                    )   
                ), #6# Aqui moure pone rx.span().
                author_buttons(), #6# Aqui ponemos nuestro componente box con nuestros botones.
                width="100%", #6# Tamaño.
                align_items="start" #6# Que se aline a la iz.
            ),
            align_items="start", #6# Que se aline a la iz.
            spacing="4", #E#6# 2em no funcionaba.
            flex_direction=["column", "column", "row", "row", "row"] #6# Segun la docu esto se define en formato lista https://reflex.dev/docs/styling/responsive/ .
        ),
        style=styles.max_width_style #6# Bloque de codigo de la hoja de stylos.
    )

#6# Creamos un componente para juntar los botones.
def author_buttons() -> rx.Component:
    return rx.box( #6# Lo vamos a meter en un box.
        button( #6# Boton nuestro que recive dos parametros.
            "YouTube", #6# icon
            constants.MI_YOUTUBE #6# Url.
        ),
        button(
            "Twitch",
            constants.TWITCH_MOURE
        ),
        button(
            "Discord",
            constants.DISCORD_URL
        ),
    )

#6# Vamos a crear una funcion con date time para que calcule y muestre los años que an pasado desde una fecha.
def experience() -> int: #6# Funcion que devuelve un entero.
    return datetime.date.today().year - 2023 #6# Codigo para la operacion.

#T#6# 1:54:14 del video arreglar el texto que sale como 3 que salga en 1 con el color rojo (De momento e quitado el punto y queda bien).
#T#6# 1:49:57 del video arreglar avatar no esta dejando borde (Parece que en esta version al estar con el tema no me toma los argumentos).
#T#6# (Solucionado) Revisar que con el flex el avatar keda arriba en movil y fin por que le da muchas bueltas y cambia el codigo nosecuantas veces.
