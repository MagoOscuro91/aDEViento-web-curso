import reflex as rx # Importamos reflex y lo nombramos como rx.
import adeviento_web.styles.styles as styles #1# Importamos del fichero de estilos styles y nombramos como tal.
from adeviento_web.styles.styles import Size #3# Importamos la clase de tamaños.
from adeviento_web.views.navbar import navbar #2# Importamos el navbar de nuestra carpeta de views.
from adeviento_web.views.header import header #3# Importamos el header de nuestra carpeta de views.
from adeviento_web.views.footer import footer #4# Importamos el footer de nuestra carpeta de views.
from adeviento_web.views.instructions import instructions #5# Importamos el instructions de nuestra carpeta de views.
from adeviento_web.views.calendar import calendar #8# Importamos el calendar.
from adeviento_web.views.partners import partners #7# Importamos partners.
from adeviento_web.views.author import author #6# Importamos el author de nuestra carpeta de views.
from adeviento_web.components.gituhub import github #9# Importamos el github de components.


#1# En reflex par definir una pagina lo aremos con una funcion que devuelva un componente.
def index() -> rx.Component: # pagina principal -> componente 
    return rx.box( #1# tiene que devolver lo que sea en este caso pues un box.
        rx.script(src="/js/snow.js"), #T#10# Para que no nieve en el navbar sacarlo de este box. rx.scrypt(src=ruta) para usar un scryp que este en nuestra carpeta js de la carpeta assets.
        rx.script("document.documentElement.lang='es'"), #11# Indicamos a la pagina el idima con este script.
        navbar(), #2# Pintamos nuestro componente navbar de esta manera dentro de esta box.
        rx.center( #3# Pintamos un vstack dentro de un rx.center para que lo centre.
            rx.vstack( #3# Dentro de este rx.vstack pintamos el header().
                header(), #3# Header.
                instructions(), #5# instructions.
                calendar(), #8# Calendario.
                github(), #9# Muñeco github pixel art.
                author(), #6# Author.
                partners(), #7# Partners.
                footer(), #4# Footer.
                width="100%", #3# Queremos que ocupe el 100%.
                spacing="4", #E#3# No funciona 4em. Queremos que tenga espacio entre elementos.
                align_items="center" #P#3# E tenido que añadir esta linea por que rx.center no me centraba.
            )
        )
    )

#1# Creamos la app de reflex de esta manera.
app = rx.App(
    stylesheets=styles.STYLESHEETS, #1# Con el parametro stylesheets= cargamos en la app nuestras hojas de estilo.
    style=styles.BASE_STYLE #1# Parametro para cargar la hoja de estilo local.
    #E# theme=rx.theme(appearance="dark") #1#E# Esta linea es experimental por que en el tuto usa otra version de reflex y me pone tema light por defecto (soluciona esto).
)

#1# Le vamos a añadir una pagina.
app.add_page(
    index,
    title="Magia Oscura 2024", # Le daremos un titulo de esta manera.
    description="Por cuarto año, ¡aqui está el calendario de adviento sorpresa de nuestra comunidad de developers! Del 1 al 24 de diciembre." # Le daremos tambien una descripcion de esta manera.
)

#1# Y lo compilamos.
#1# app.compile() # Lo comento por que en la version actual esto esta obsoleto y no es necesario.

#5# En este capitulo al final moure cambia la version de reflex yo llevo solucionando desde el primero cosas para la version mia y no quiero cambiarla por si la lio.
#5# Para cambiar la version de reflex se mete en el fichero "requeriments" mira la version y cambia la version por la que el quiere usar.
#5# Para usar una version de reflex especifica en la terminal comando: pip install --upgrade reflex==0.3.2 la 0.3.2 es la que pone moure, el tenia la 0.3.4 yo tengo la reflex==0.4.7 .
#5# reflex --version .Para ver que version tenemos de reflex.

#1# ESTRUCTURA DEL PROYECTO
#1# Esto es como lo estructura moure pero puede ser como queramos.dir ADEVIENTO_WEB/adeviento_web (este seria el nombre de nuestro proyecto (my_app_name)).
#1# 1 1 dir para "components"
#1# 2 1 dir para "styles" con 1 fichero.py para estilar la pagina "styles", 1 para los colores "colors" 1 para fuentes "fonts".
#1# 3 1 dir para "views" (componentes visuales grandes)
#1# 4 (opcional demomento) 1 fichero README.md y 1 fichero LICENSE en el dir principal ADEVIENTO_WEB yo me e descargado los de moure como ejemplo.
#1# 5 Favicon en assets sustituimos favicon.ico por el nuevo con el mismo nombre y extension de 48x48 pagina para redimensionar imagenes https://www.resizepixel.com/es/resize-image/ (si no tienes programa).

                        ### Como leer mis comentarios ###

#P# Personal, #N# Notas, #T# Tarea, #1# Capitulo 1 en adelante, #E# Linea de codigo experimental.

                                    ### NOTAS ###

#N# Un vstack de reflex es para poner cosas de arriba para abajo.
#N# Un hstack de reflex es para poner cosas de izquierda a derecha.
#N# Moure cuando no le cojia el color rojo añadio "! important" asi ACCENT = "#EA5940" | ACCENT = "#EA5940 ! important".

                                    ### TAREAS ###

#T# Cargarme el tema o configurarlo.
#T# Probar a desactivar el tema con theme=False en rx.App y cambiar la description= en add_page.
#T# Corregir linea 9 experimental del tamaño del heading .Video = 52:57 me e quedado.
#T# min 1:05:43
