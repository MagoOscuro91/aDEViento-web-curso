import reflex as rx #5# Importamos reflex y nombramos como rx.


#5# Creamos el componente con el costructor tipando los parametros text y url que seran los que van a variar de los botones.
def button(text: str, url: str) -> rx.Component:
    return rx.link( #5# Devolvemos un link.
        rx.button( #5# Con un boton.
            text, #5# El texto que recive en text.
            class_name="nes-btn is-error" #5# Usamos el boton rojo de error de la libreria nes.css.
        ),
        href=url, #5# La url del link que reciba el parametro url.
        is_external=True, #5# Se abre en una ventana nueva.
        padding_right="20px" #E#6# Vengo del futuro por que los botones de un box necesitan un padding.
    )
