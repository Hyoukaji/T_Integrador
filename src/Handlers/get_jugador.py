import json
import os
import os.path

nom_Pro = "T_Integrador"
ruta_proyecto = os.path.join(os.getcwd(),nom_Pro)

ruta_archivo = os.path.join(os.getcwd(), "src/Archivos/jugadores.json")


def start(unNick):
    try:
        datos_jugador = {}
        with open(ruta_archivo, "r") as archivo:
            datos_jugadores = json.load(archivo)
            try:
                datos_jugador[unNick] = datos_jugadores[unNick].copy()
                return datos_jugador
            except:
                return None

    except FileNotFoundError:
        print("Archivo de jugadores no encontrado")
def start(unNick):
    with open(ruta_archivo, "r") as archivo:
        datos_jugadores = json.load(archivo)
    return datos_jugadores[unNick]
