import json
import os
import os.path
import string

nom_Pro = "T_Integrador"
ruta_proyecto = os.path.join(os.getcwd(),nom_Pro)
nom_dir = "src"
ruta_directorio = os.path.join(ruta_proyecto, nom_dir)
nom_dir_2 = "Archivos"
ruta_directorio_2 = os.path.join(ruta_directorio, nom_dir_2)
nom_arch_2= "jugador_actual.json"
ruta_archivo_2 = os.path.join(ruta_directorio_2, nom_arch_2) 

def start(): 
    datos_jugador = {}
    with open(ruta_archivo_2, "r") as archivo_2:
        datos_jugador = json.load(archivo_2)
        for key in datos_jugador:
            return key





