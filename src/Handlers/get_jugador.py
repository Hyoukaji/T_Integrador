import json
import os
import os.path

nom_Pro = "T_Integrador"
ruta_proyecto = os.path.join(os.getcwd(),nom_Pro)
nom_dir = "src"
ruta_directorio = os.path.join(ruta_proyecto, nom_dir)
nom_dir_2 = "Archivos"
ruta_directorio_2 = os.path.join(ruta_directorio, nom_dir_2)
nom_arch = "jugadores.json"
ruta_archivo = os.path.join(ruta_directorio_2, nom_arch)


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
