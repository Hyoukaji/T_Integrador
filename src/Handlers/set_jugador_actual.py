import json
from json import JSONEncoder
import os
import os.path
from src.Archivos import claseJugador

nom_Pro = "T_Integrador"
ruta_proyecto = os.path.join(os.getcwd(),nom_Pro)

nom_dir = "src"
ruta_directorio = os.path.join(ruta_proyecto, nom_dir)

nom_dir_2 = "Archivos"
ruta_directorio_2 = os.path.join(ruta_directorio, nom_dir_2)

nom_arch_2= "jugador_actual.json"
ruta_archivo_2 = os.path.join(ruta_directorio_2, nom_arch_2)

nom_arch = "jugadores.json"
ruta_archivo = os.path.join(ruta_directorio_2, nom_arch)

def start(unJugador):
    dato_jugador_actual = unJugador
    persona_json = JugadorEncoder().encode(dato_jugador_actual)
    with open(ruta_archivo_2, "w") as file:
        json.dump(persona_json, file, indent=4)
