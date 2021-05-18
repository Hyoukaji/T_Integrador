import json
import os
import os.path

nom_arch_2= "jugador_actual.json"
ruta_archivo_2 = os.path.join("src/Archivos/", nom_arch_2)

nom_arch = "jugadores.json"
ruta_archivo = os.path.join("src/Archivos/", nom_arch)

def start(unNick):
    try:
        dato_jugador_actual={}
        if os.path.exists(ruta_archivo):
            with open(ruta_archivo_2, "r") as archivo_2:
                dato_jugador_actual = json.load(archivo_2)
                if unNick not in dato_jugador_actual:
                    with open(ruta_archivo, "r") as archivo:
                        datos_jugadores = json.load(archivo)
                        dato_jugador_actual[unNick] = datos_jugadores[unNick].copy()
                        with open(ruta_archivo_2, "w") as file:
                            json.dump(dato_jugador_actual, file, indent=4)
        else:
            with open(ruta_archivo, "r") as archivo:
                datos_jugadores = json.load(archivo)
                dato_jugador_actual[unNick] = datos_jugadores[unNick].copy()
                with open(ruta_archivo_2, "w+") as file:
                    json.dump(dato_jugador_actual, file, indent=4)
    except FileNotFoundError:
        with open(ruta_archivo, "r") as archivo:
            datos_jugadores = json.load(archivo)
            dato_jugador_actual[unNick] = datos_jugadores[unNick].copy()
            with open(ruta_archivo_2, "w+") as file:
                json.dump(dato_jugador_actual, file, indent=4)
