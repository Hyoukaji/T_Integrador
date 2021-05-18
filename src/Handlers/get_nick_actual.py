import json
import os
import os.path
import string

nom_arch_2= "jugador_actual.json"
ruta_archivo_2 = os.path.join("src/Archivos/", nom_arch_2) 

def start(): 
    datos_jugador = {}
    with open(ruta_archivo_2, "r") as archivo_2:
        datos_jugador = json.load(archivo_2)
        for key in datos_jugador:
            return key





