import reflex as rx #2# Importamos reflex y nombramos como rx.


#2# Creamos el componente con el costructor tipando los parametros icon y url que seran los que van a variar de los botones.
def link_icon(icon: str, url: str) -> rx.Component:
    return rx.link(
        "", #2# Aqui pondriamos un texto al link si quisieramos.
        class_name=f"nes-icon {icon} is-medium", #2# Como vamos a usar la libresia nes.css comento la linea de abajo por que la manera en este caso es esta.
        # icon=icon, #2# Aqui le pasamos la imagen que va a ser el parametro icon para el icono.
        href=url, #2# Aqui vamos a asignarle al boton la url que reciva el parametro url.
        is_external=True #2# Para que lo abra en una ventana nueva(van a ser enlaces a otras paginas(por eso)).
    )
