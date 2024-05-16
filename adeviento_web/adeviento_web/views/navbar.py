import reflex as rx #2# Importamos reflex y nombramos como rx.
import adeviento_web.constants as constants #2# Importamos el fichero constants con nuestras constantes(en este caso urls).
from adeviento_web.styles.styles import Size, Color #2# Importamos la clase Size y Color creadas para trabajar.
from adeviento_web.components.link_icon import link_icon #2# Importamos link_icon que emos creado para los botones de link.


#2# IMPORTANTE! Emos cambiado en el dir assets la imagen "favicon" que es la que se muestra en la pestaña del navegador 
#2# por otra y la emos nombrado como tal para no cambiar el codigo sin mas.

#2# Creamos el componente con el nombre de navbar ("navigation bar"(barra superior de la pagina))
def navbar() -> rx.Component: #2# Lo vamos a meter en un horizontal stack dentro de un vertical stack para pintar la linea.
    return rx.vstack(
        rx.hstack(
            rx.image(
                src="circulo.png", #2# Lo primero es definir el src (source image) : URL o ruta(si esta en assets solo pongo el nombre).
                alt="Imagen de circulo oscuro yugioh", #2# La vamos a hacer accesible con este parametro y imformacion.
                width=Size.BIG_BIG.value, #2# Ancho.Vamos a darle un tamaño.
                height=Size.BIG_BIG.value #2# Altura.
            ), #2# Vamos a pintar una imagen.
            rx.text(
                "Magia Oscura 2024",
                padding_y="0.75em", #2#E# Vertical. Esta linea es experimental por que el texto no estaba ami gusto.
                padding_x="0.2em" #2#E# Horizontal. Esta linea es experimental "".
            ), #2# Vamos a pintar un texto.
            rx.spacer(), #2# Queremos que empuje todo a la iz para esp usamos spacer.
            link_icon( #2# Vamos a pintar un link_icon con nuestra funcion que crea botones de la libreria nes.css
                "youtube", #2# Recive dos parametros el nombre del icono a pintar.
                constants.MI_YOUTUBE #2# Y la url que le queremos asignar.Las url las vamos a anotar todas en un fichero que se llama constantes (en la raiz del proyecto dice moure(adeviento_web(la mayusculas no))) para tenerlas accesibles.
            ),
            link_icon( #2# Vamos a montar otro boton simplemente copiando y cambiando los parametros.
                "twitch", #2# Tenemos uno que se llama twitch para TWITCH.
                constants.TWITCH_MOURE #2# Tenemos una url de twitch en nuestro fichero constantes.
            ),
            link_icon(
                "github", #2# Icono de la libreria nes.css.
                constants.REPO_WEB #2# Url.
            ),
            width="100%" #2# Vamos a darle un tamaño al vstack como es un tamaño estandar lo escribimos sin mas.
        ),
        bg=Color.PRIMARY.value, #2# Vamos a darle un color al fondo (background).
        position="sticky", #2# Vamos a dar una propiedad css sticky (que este siempre arriba).
        border_bottom=f"0.25em solid {Color.SECONDARY.value}", #2# Vamos a pintar la linea el pinte con esta propiedad.
        padding_x=Size.DEFAULT.value, #2# Vamos a darle padding (margen) en el eje x con esta propiedad.
        padding_y=Size.DEFAULT.value, #2# Vamos a darle padding (margen) en el eje y.
        z_index="999", #2# Vamos a darle un z_index para decirle que las cosas pasen pero esta no con el indice maximo propiedad css.
        top="0", #2# Ahora vamos a decirle que se pege a la parte superior con esta propiedad.
        width="100" #2# Ahora vamos a decirle que ocupe la totalidad.
    )

#2# El navbar es una abreviatura de "navigation bar" en inglés, que se refiere a la barra de navegación en una página web.
#2# Es una sección de la interfaz de usuario que contiene enlaces o botones para facilitar la navegación del usuario por el sitio web.
