import reflex as rx # Importamos reflex y le damos el alias de rx en este fichero lo vamos a necesitar.
from enum import Enum #2# Importamos el enum de python par usar la clase Size.
from .fonts import Font #1# Importamos clase de nuestro fichero fonts. El punto inicial indica que se está importando desde el mismo directorio o paquete en el que se encuentra el archivo actual.
from .colors import Color, TextColor #1# Importamos la case TextColor y Color de nuestro fichero colors.


MAX_WIDTH = "1000px" #3# Tamaño maximo de la web, suelen ser 1000 pixeles 1200px.Habeces nos encontramos con usuarios que tienen pantallas grandes por eso damos un tamaño maximo.

#1# Creamos una lista para nuestras hojas de estilo.
STYLESHEETS = [
    "https://unpkg.com/nes.css@latest/css/nes.min.css", # Fichero css.
    # Uso de api "https://fonts.googleapis.com/css2?family=" mas nombre de la familia que es el nombre de la fuente "Press Start 2P" una vez en la url tenemos que concatenar la frase sustituyendo los espacios por un +.
    # Y como buena practica le vamos a concatenar &display=swap para permitir que la pagina se carge con una fuente por defecto y cuando este cargado el css aga el cambio para no saturar la carga.
    # Link final : https://fonts.googleapis.com/css2?family= Press+Start+2P &display=swap .
    "https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap" # Fuente (APIlink de la fuente Press Start 2P) # Segun le das a descargar o como usar te da la opcion de la api de google https://developers.google.com/fonts/docs/css2?hl=es-419 (INFOlink).
]

#2# Podriamos crear un fichero para los tamaños pero moure lo hace en este mismo.
#2# Creamos la clase para los tamaños.
class Size(Enum):
    ZERO = "0em ! important" #4# Definimos un tamaño 0.
    DEFAULT = "1em" #2# 1em Medida relativa ejemplo: 16px 1em = 16px, 16px 2em = 32px.Osea 1em es el tamaño original 2em el doble 3em triple etc.
    SMALL = "0.5em" #2# 0.5em Seria la mitad del tamaño original.
    MEDIUM = "0.8em" #3# Añadido capitulo 3 del curso sin mas.
    BIG = "2em"
    BUTTON = "2.75em"
    BIG_BIG = "3em"
    VERY_BIG = "4em"


#1# Creamos hoja de estilo base/local con este dict.Aqui utilizamos casi css desde python con este cambio css : "font-family": Font.DEFAULT.value. a reflex : "font_family": Font.DEFAULT.value.
BASE_STYLE = {
    "font_family": Font.DEFAULT.value, #1# Propiedad css fuente.
    "color": TextColor.PRIMARY.value, #1# Propiedad css color (fuent creo).
    "background": Color.PRIMARY.value, #1# Propiedad css para el color del fondo de la web.
    rx.heading: { #E#3# Lo e solucionado cambiando la primera en minuscula.(Moure crea esta linea q ami no me esta funcionando).
        "font_family": Font.DEFAULT.value, #3# Fuente deseada para la cabezera.
        "color": TextColor.ACCENT.value #3# Color deseado.
    },
    #3# Para todos los rx.link de la web.
    rx.link: { #E#3# Lo e solucionado cambiando la primera en minuscula.linea original rx.Link (Moure crea esta linea q ami no me esta funcionando).
        "text_decoration": "none", #3# El texto le vamos a decir que no lo subraye.
        "_hover": { #3# Propiedad para el raton encima del link css.Creamos como dict.
            "color": TextColor.ACCENT.value, #3# Color de los links.
            "text_decoration": "none" #3# El texto le vamos a decir que no lo subraye otra vez _hover este dict.
        }
    },
    # rx.Span: { #T#3# No funciona por que los rx.span no me funcionan y los span los arregle con rx.text y modificando.
    #     "font_size": Size.MEDIUM.value #3# Tamaño de fuente.
    # }
    #3# Para todos los rx.text de la web.
    rx.text: { #E#3# Provando solucion para la linea de arriba.
        "font_size": Size.DEFAULT.value #3# Tamaño de fuente.
    },
    rx.button: {
        "margin_bottom": Size.DEFAULT.value, #5# Vamos a dar un margen a los botones de toda la web.
        "height": Size.BUTTON.value, #5# Vamos a dar un tamaño de altura.
        "color": f"{TextColor.SECONDARY.value} !important", #5# Vamos a decir que el color por defecto sea este gris.
        "_hover": { #5# Propiedad para el raton encima del link css.Creamos como dict.
            "color": f"{TextColor.PRIMARY.value} !important", #5# Color de los links blanco.
        }
    }
}

#3# Definimos un estilo para este bloque de codigo que se va a repetir mucho.
max_width_style = dict(
    align_items="start",
    padding_x=Size.BIG.value,
    width="100%",
    max_width=MAX_WIDTH
)
