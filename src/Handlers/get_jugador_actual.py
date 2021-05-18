import json
import os
import os.path

nom_arch_2= "jugador_actual.json"
ruta_archivo_2 = os.path.join("src/Archivos/", nom_arch_2)

def start():
    try:
        with open(ruta_archivo_2, "r") as archivo_2:
            dato_jugador_actual = json.load(archivo_2)
        return dato_jugador_actual

    except FileNotFoundError:
        print("Archivo de jugadores no encontrado")
