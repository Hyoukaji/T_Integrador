import json
import os
import os.path
from src.Handlers import get_nick_actual

nom_arch_2= "jugador_actual.json"
ruta_archivo_2 = os.path.join("src/Archivos/", nom_arch_2)


def start():
    try:
        if os.path.exists(ruta_archivo_2):
            unNick = get_nick_actual.start()
            dato_jugador_actual = {}
            with open(ruta_archivo_2, "r") as archivo_2:
                dato_jugador_actual = json.load(archivo_2)
                puntos = dato_jugador_actual[unNick]["puntos"]
                dato_jugador_actual[unNick]["puntos"] = puntos + 1
                with open(ruta_archivo_2, "w") as file:
                    json.dump(dato_jugador_actual, file, indent=4)
        else:
            print("Archivo jugador actual no ha sido creado aun")
    except FileNotFoundError:
        print("Archivo de jugadores no encontrado")