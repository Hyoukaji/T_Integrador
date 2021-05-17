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
