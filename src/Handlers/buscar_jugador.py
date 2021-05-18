import json
import os
import os.path


nom_arch = "jugadores.json"
ruta_archivo = os.path.join("src/Archivos/", nom_arch)

def start(unNick):
    try:
        if os.path.exists(ruta_archivo):
            archivo = open(ruta_archivo, "r")
            datos_jugadores = json.load(archivo)
            if unNick in datos_jugadores:
                return True, True
            else:
                return False, True
            archivo.close()
        else:
            return False, True
    except FileNotFoundError:
        return False, False
