import reflex as rx #4# Importamos reflex y nombramos como rx.
import adeviento_web.styles.styles as styles #4# Importamos los estilos (yo creo que se puede concatenar a la importacion de size).
import adeviento_web.constants as constants #4# Importamos las constantes.
from adeviento_web.styles.styles import Size, TextColor #4# Importamos la clase Size y TextColor.


def footer() -> rx.Component:
    return rx.hstack( #4# Vamos a hacer un stack horizontal que contenga un stack vertical.
        rx.vstack( #4# Stack vertical.
            rx.text( #4# Texto.
                "Magia Oscura 2024",
                font_size=Size.DEFAULT.value, #4# Vamos a estilar directamente aqui el texto, tamaño de fuente.
                margin_bottom=Size.ZERO.value #4# Vamos a darle un margen inferior.
            ),
            rx.link( #4# Link.
                "Creado con magia y ",
                rx.box(class_name="nes-icon is-small heart"), #4# Para meter de nes.css el corazón en medio del texto metemos un box con el class-name sin mas.
                " por MagoOscuro91",
                href=constants.MAGO_OSCURO91_URL, #4# Linkeamos la url deseada en este caso seria a nuestra pagina personal.
                is_external=True, #4# La abrimos en una nueva pestaña.
                margin_bottom=Size.SMALL.value, #4# Vamos a darle un margen inferior.
                font_size=Size.DEFAULT.value, #4# Vamos a estilar directamente aqui el texto, tamaño de fuente.
                color=TextColor.TERTIARY.value #4# Vamos a estilar el color.
            ),
            align_items="start", #4# Que pegue los items a la iz.
            spacing="2" #E#4# Damos un espacio medio con 8em no funcionava deja entre 0 y 9.
        ),
        rx.spacer(), #4# Vamos a dar un spacer al propio hstack para que cubra el espacio vacio entonces lo que ponemos acontinuacion lo va a empujar al otro lado.
        rx.image( #4# Vamos a poner la imagen que ira a la derecha del todo por que estamos en un horizontal stack y el espacio se lo coge spacer.
            src="bola_amuleto.png", #4# Nuestra imagen de assets el nombre.
            alt="La bola de los amuletos legendarios de yugioh.", #4# Descripcion para que sea accesible(buenas practicas de desarollo web).
            class_name="nes-avatar is-large", #4# Vamos a heredar tamaños con esta linea de nuestra libreria nes.css avatars en el parametro class_name.
            padding_bottom="3px" #E#6# Vengo del futuro a darle un padding inferior a la imagen de la bola que estaba muy pegada y no me gustaba.
        ),
        padding_bottom=Size.DEFAULT.value, #4# Vamos a separarlo de la parte de abajo.
        style=styles.max_width_style, #4# Vamos a utilizar el bloque de codigo para este componente (align_items="start",padding_x=Size.BIG.value,width="100%",max_width=MAX_WIDTH).
        align_items="center" #4# Vamos a alinearlos al centro con este parametro css, en nuestro style tenemos start asique despues de esa linea va esta y termina centrando.
        #N#4# Con la herramienta para desarolladores en la web en la pestaña layout podemos ver que se a centrado y que esta pasando en general con los stacks box etc.
    )

#N#4# La declaración  !important  en CSS se utiliza para dar prioridad a una regla específica sobre otras reglas que podrían estar aplicadas al mismo elemento.
#N#4# Cuando se añade  !important  al final de una propiedad, se asegura de que esa propiedad tenga la máxima prioridad y no sea sobrescrita por reglas con menor especificidad.
