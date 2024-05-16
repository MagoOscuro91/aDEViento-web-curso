import reflex as rx #8#
import adeviento_web.constants as constants #8# Importamos las constantes.
import adeviento_web.styles.styles as styles #8# Importamos los estilos con el alias styles.
from adeviento_web.components.header_text import header_text #8# Importamos el costructor de cabezeras.
from adeviento_web.components.button import button #8# Importamos nuestro contructor de botones.
from adeviento_web.components.day import day #8# Importamos el componente day que emos creado que recive 3 args.

#8# Componente calendario.
def calendar() -> rx.Component:
    return rx.vstack( #8# Dentro de un vertical stack.
        header_text( #8# Nuestro costrucctor de cabezeras.
            "heart", #8# Icono del corazon nes.css .
            "Calendario de MAGIA OSCURA" #8# Cabezera.
        ),
        rx.vstack( #8# Dentro de un vertical stack.
            rx.hstack( #8# Un horizontal stack.
                rx.text("El evento comienza en"), #8# El texto del contador.
                rx.text(id="countdown"), #8# En esta linea hacemos referencia al scrip js id="" donde se hace el cambio que ejecuta el scrip.
                align_items="start" #8# Alineamos los items al principio.
            ),
            button(
                "Recordar", #8# Un texto.
                constants.DISCORD_URL #8# Moure pone el evento en discord.
            ),
            rx.chakra.span( #8# Un texto.
                "Los regalos son sorpesa, permanecerán ocultos hasta el dia de su publicación."
            ),
            class_name="nes-container is-dark", ## El estido de contenedor nes.css.
            align_items="start", #8# Alineamos los items al principio.
            width="100%" #8# El widht al 100% para que ocupe el maximo siempre.
        ),
        rx.chakra.responsive_grid( #8# Grid responsivo.E tenido que recurrir a chackra por que responsive_gird no estaba ya.
            rx.foreach( #8# Foreach es un for en reflex.Para pintar 24 imagenes que con el paso de los dias cada imagen tenga unos parametros con la funcion day
                list(range(1, 25)), #8# Como todo for necesita un iterable en este caso una lista con el rango del 1 al 25 osea 24
                lambda number: #8# Montamos una pequeña lambda (funcion no definida) con number de momento para day la funcion q recive 3 args.
                day( #8# Day funcion que recive 3 args number url e image, que pinta un componente 
                    number #8# El arg que recive la funcion day
                ),
            ),
            columns=[2, 3, 4, 5, 6], #8# Las columnas maximas que se pintan en movil tablet destock etc.
            spacing="1em", #8# El espacio entre componentes.
            width="100%", #8# Que de ancho ocupe todo lo que pueda al ser responsive.
            padding_top="2em" #8# Padding superior de 2em.
        ),
        rx.script(src="/js/countdown.js"), #8# En esta linea lanzamos el script "countdown.js".
        style=styles.max_width_style #8# Nuestro estilo para todas las vistas.
    )
