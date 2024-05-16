from enum import Enum # Vamos a importar el enum de python.


# Creamos una clase con Enum para tener los colores accesibles (ejemplo Color.ACCENT.value)
class Color(Enum):
    ACCENT = "#EA5940" # Rojo.# Vamos a definir este color para acentuar/resaltar.
    PRIMARY = "#212529" # Gris oscuro.# Vamos a definir un color primario.
    SECONDARY = "#D3D3D3" # Gris claro.# Color secundario.
    TERTIARY = "#D3D3D3"

# Creamos una clase igual para los colores del texto.
class TextColor(Enum):
    ACCENT = "#EA5940" # Rojo.
    PRIMARY = "#FFFFFF" # Blanco.
    SECONDARY = "#212529" # Gris oscuro.
    TERTIARY = "#D3D3D3" # Gris claro.
