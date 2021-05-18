import json
import os
import os.path
from src.Handlers import get_jugador_actual

nom_arch = "jugadores.json"
ruta_archivo = os.path.join("src/Archivos/", nom_arch)

def start():
    try:
        with open(ruta_archivo, "r") as archivo:
            datos_jugadores = json.load(archivo)
            datos_jugadores.update(get_jugador_actual.start())
            with open(ruta_archivo, "w") as archivo:
                json.dump(datos_jugadores, archivo, indent=4)
    except FileNotFoundError:
        print("el path no anda bien ")
