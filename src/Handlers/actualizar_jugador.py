import json
import os
import os.path
from src.Handlers import get_nick_actual
from src.Handlers import get_jugador_actual

nom_arch = "jugadores.json"
ruta_archivo = os.path.join("src/Archivos/", nom_arch)
  
def start():
    try:
        datos_jugadores = {}
        nick_actual = get_nick_actual.start()
        with open(ruta_archivo, "r+") as archivo:
            datos_jugadores = json.load(archivo)
            datos_jugadores[nick_actual] = get_jugador_actual.start()
    except FileNotFoundError:
        print("el path no anda bien ")
