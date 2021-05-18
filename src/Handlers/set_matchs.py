import json
import os
import os.path
from src.Handlers import get_nick_actual

nom_arch_2= "jugador_actual.json"
ruta_archivo_2 = os.path.join("src/Archivos/", nom_arch_2)

def start(valor):
    try:
        unNick = get_nick_actual.start
        dato_jugador_actual = {}
        with open(ruta_archivo_2, "r") as archivo_2:
            dato_jugador_actual = json.load(archivo_2)
            dato_jugador_actual[unNick]["matchs"] = valor
            with open(ruta_archivo_2, "w") as file:
                json.dump(dato_jugador_actual, file, indent=4)
    except FileNotFoundError:
        print("Archivo de jugadores no encontrado")
