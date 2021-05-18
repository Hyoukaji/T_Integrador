import json
import os
import os.path
from src.Handlers import get_nick_actual


def start(valor):
    try:
        dato_jugador_actual = {}
        unNick=get_nick_actual.start()
        with open(ruta_archivo_2, "r") as archivo_2:
            dato_jugador_actual = json.load(archivo_2)
            dato_jugador_actual[unNick]["cant_casillas"] = valor
            with open(ruta_archivo_2, "w") as file:
                json.dump(dato_jugador_actual, file, indent=4)
    except FileNotFoundError:
        print("Archivo de jugadores no encontrado")
