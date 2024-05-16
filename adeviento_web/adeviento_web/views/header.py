import reflex as rx #3# Importamos reflex y nombramos como rx.
import adeviento_web.constants as constants #3# Importamos las constantes.
import adeviento_web.styles.styles as styles #3# Importamos nuestra hoja de estilos.
from adeviento_web.styles.styles import Size, TextColor #3# Importamos los tamaños de nuestra hoja de estilos y textcolor.


#3# Creamos nuestro componente header (cabezera).
def header() -> rx.Component:
    return rx.vstack( #3# Creamos un vstack para meter cosas una debajo de otra.
        rx.heading( #3# La cabezera ya la tenemos en reflex y la pintamos de esta manera.
            "Magia Oscura 2024",
            size="7", #E#3# "Lg no funciona" Parametro size=lg tamaños que ai predefinidos para rx.heading lg large.
            padding_botton=Size.DEFAULT.value #3# Parametro para dar un margen a la parte de abajo.
        ),
        rx.flex( #3# Layaut flex responsive layout (Layout responsivo) queremos poner una imagen y cuando se haga responsive tendremos que moverlo.
            rx.image( #3# Pintamos la imagen de esta manera.
                src="paladin.png", #3# Donde se encuentra como la tenemos en assets solo su nombre.
                alt="Paladin oscuro yugioh png", #3# Descripcion para que este accesible.
                width="17em", #3# No usamos nuestra clase de tamaños por que este es muy estandar usamos los que mas repitamos.
                height="16em", #3# Altura.
                margin_right=Size.BIG.value #3# Propiedad css
            ),
            rx.vstack( #3# Pintamos un vstack dentro para ordenar el contenido en vertical.
                rx.box( #3# Vamos a meter dos textos dentro de un box(imagino que para que esten y se muevan juntos).
                    rx.text("24 dias. 24 magias."), #3# Pintamos un texto.
                    rx.text("Del 1 al 24 de diciembre."), #3# Pintamos otro texto.
                    class_name="nes-balloon from-left is-dark" #3# Parametro css para usar el bocadillo de la libreria css.
                ),
                #E#3# rx.span(), #E#3# En esta version de reflex esto no funciona e rebisado la documentacion y vamos a salir del paso con esto.
                rx.text( #3# El componente rx.span era para cambiar luego el color y modificar linkearlo o algo.
                    "Por cuarto año, ¡aqui está el calendario de magias sorpresa de nuestra ",
                    rx.hstack(
                    rx.text(
                        "comunidad de developers",
                        color=TextColor.ACCENT.value,
                        font_size=Size.DEFAULT.value #3# Como este rx.text esta dentro de un rx.text en la hoja de estilos BASE esto se reduce a la mitad lo solucionamos definiendo un valor independiente.
                    ),
                    rx.text("!")
                    )
                ),
                rx.text(
                    "Una actividad en la que cada dia sortearé una magia relacionada con programación y desarollo software (virus, jutsus, cartas trampa, etc)."
                ),
                rx.text(
                    "Su finalidad es ayudar a compartir conocimiento y fomentar el aprendizaje en comunidad."
                ),
                rx.link(
                    "#Magia Oscura 2024", #3# Link name.
                    href=constants.ADEVIENTO_HASHTAG_URL, #3# Parametro para dar la url.
                    is_external=True, #3# En pestaña externa.
                    color=TextColor.TERTIARY.value, #3# Parametro css de color.
                    padding_top=Size.SMALL.value, #3# Le damos un margen a la parte de arriba.
                    font_size=Size.MEDIUM.value #3# Parametro css tamaño de fuente.
                ),
                align_items="start" #3# Vamos a alinear los elementos a la derecha dice moure.Esto son estilos.
            ),
            #3# Si trabajamos con un flex podemos definir la direccion de como se va modificando la pantalla. De iz a d en la lista ace referencia a las distintas pantallas de pequeña a grande.
            flex_direction=["column", "column", "row", "row", "row"] #3# Segun la docu esto se define en formato lista https://reflex.dev/docs/styling/responsive/ .
        ),
        padding_top=Size.BIG.value, #3# Le damos un margen a la parte de arriba.
        #3# style=styles.max_width_style #3# Moure reemplaza con esta linea las 4 siguientes que es un bloque que se repite pero como ejemplo dejare este asi.
        align_items="start", #3# Vamos a alinear los elementos a la derecha.
        padding_x=Size.BIG.value, #3# Vamos a darle en el eje x (latera) un margen.
        width="100%", #3# Definimos un tamaño.
        max_width=styles.MAX_WIDTH #3# Definimos el tamaño maximo con nuestra hoja de estilos.Esto es para que en pantallas mas grandes no quede mal.
    )
