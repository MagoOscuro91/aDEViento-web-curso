from enum import Enum # Vamos a importar el enum de python.


# Vamos autilizar esta libreria de css # https://nostalgic-css.github.io/NES.css/ 
# https://unpkg.com/nes.css@latest/css/nes.min.css version latest (fichero css alojado en url (podriamos descargarlo y añadirlo pero vamos a usarlo desde donde se encuentra)).

# Creamos una clase con Enum para las fuentes.
class Font(Enum): 
    DEFAULT = "Press Start 2P" # Como estamos usando la libreria nes.css nos dice que por defaul usa esta https://fonts.google.com/specimen/Press+Start+2P .Segun la documentacion via CDN # https://github.com/nostalgic-css/NES.css .
