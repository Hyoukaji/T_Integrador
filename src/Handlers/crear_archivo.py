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
nom_arch = "jugadores.json"
ruta_archivo = os.path.join(ruta_directorio_2, nom_arch)

def start():
    datos_jugadores = {}
    persona = Jugador("tu vieja","hermafrodita",18)
    persona_json = JugadorEncoder().encode(persona)
    datos_jugadores[unNick] = persona_json
    with open(ruta_archivo, 'w') as file:
        json.dump(datos_jugadores, file, indent=4, cls=JugadorEncoder)
