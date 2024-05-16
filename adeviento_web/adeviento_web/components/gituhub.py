import reflex as rx #9# Importamos reflex.
import adeviento_web.constants as constants #9# Importamos las constantes.
from adeviento_web.styles.styles import Size #9# Importamos los tamaños.


def github() -> rx.Component:
    return rx.link(
        rx.vstack(
            rx.vstack(
                rx.text(
                    "Proyecto"
                ),
                rx.text(
                    "en GitHub"
                ),
                align_items="start", #9# Alinea los items.
                class_name="nes-balloon from-right is-dark", #9# Bocadillos nes.css.
                margin_bottom=Size.BIG.value #9# Margen inferior.
            ),
            rx.box(
                rx.text( #T#9# Como no esta en un span no esta funcionando por la hoja de estilos que modifica el rx.text.
                    constants.VERSION, #T#9# 
                    class_name="is-error" #T#9# 
                ),
                class_name="nes-badge" #T#9# 
            )
        ),
        rx.box(
            class_name="nes-octocat animate" #9# El pixel art.
        ),
        href=constants.GITHUB_REPO,
        is_external=True, #9# Abre en pestaña nueva.
        align_items="end", #9# Alinea los items.
        display="flex", #9# 
        margin_top=Size.ZERO.value #9# Margen superior.
    )

#9# Falta el calendario.
