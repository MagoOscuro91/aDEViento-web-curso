import reflex as rx #5# Importamos reflex y nombramos como rx.
import adeviento_web.styles.styles as styles #5# Importamos styles y nombramos como styles.
import adeviento_web.constants as constants #5# Importamos las constantes.
from adeviento_web.components.button import button #5# Importamos el boton que emos creado para usarlo.
from adeviento_web.styles.styles import TextColor #5# Importamos la clase TextColor que emos creado para usarlo.


#5# Creamos el componente con el costructor.
def instructions() -> rx.Component:
    return rx.box( #5# Creamos un box con un vertical stack para que el vstack tenga relieve gracias a estar dentro del box.
        rx.vstack(
            rx.text(
                "¿Cómo funciona el evento?", #5# El texto del titulo.
                class_name="title", #5# Segun la docu de nes.css para usar este container el titulo se asigna asi ("title").
                color=TextColor.ACCENT.value #5# Lo pintamos rojo.
            ), #5# Un texto.
            rx.text("* Del 1 al 24 de diciembre descubriré cada dia un nuevo regalo en el calendario."), #E#5# Aqui moure pone rx.span().
            rx.text("* Puedes participar desde cualquier parte del mundo."), #E#5# Aqui moure pone rx.span().
            rx.text("* Sólo tendrás que hacer Retweet a la publicación que enlazaré desde esta web. Tu cuenta de Twitter/X tiene que ser pública."), #E#5# Aqui moure pone rx.span().
            button(#5# Este boton de nes.css rojo que emos creado recive dos parametros texto y url.
                "Twitter", #5# Primer parametro que recibe nuestro boton css es el "nombre".
                constants.TWITTER_URL #5# Segundo parametro "url" de twitter de nuestras constantes.
            ), #5# Un boton que emos creado.
            rx.text("* Al dia siguiente realizaré el sorteo de forma pública en directo desde Twitch y compartiré el ganador en la web y en Twitter/X. En caso de que no pueda hacer directo, publicaré un video con el resultado del sorteo."), #E#5# Aqui moure pone rx.span().
            button(
                "Twitch", #5# Primer parametro que recibe nuestro boton css es el "nombre".
                constants.TWITCH_URL #5# Segundo parametro "url" de twitch de nuestras constantes.
            ), #5# Un boton que emos creado.
            rx.text("* ¡Vuelta a empezar! Publicaré un nuevo regalo y comenzará de nuevo el proceso."), #E#5# Aqui moure pone rx.span().
            class_name="nes-container is-dark with-title", #5# Vamos a darle al box el estilo container de nes.css para el relieve.
            align_items="start", #5# Vamos a alinear todo a la iquierda por que es un stack vertical si fuera horizontal se alinearian arriba.
            width="100%"
        ),
        style=styles.max_width_style #5# Reutilizamos nuestro bloque de codigo.
    )

#N#5# Cuando se define  align-items: start; , se está indicando que los elementos hijos se alinearán en la parte superior del contenedor en el eje transversal.
#N#5# Esto significa que los elementos se alinearán en la parte superior si el eje principal es horizontal, o en el extremo izquierdo si el eje principal es vertical.
