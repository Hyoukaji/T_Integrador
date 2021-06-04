import json
import os
import os.path
from src.Handlers import get_nick_actual

nom_arch_2= "jugador_actual.json"
ruta_archivo_2 = os.path.join("src/Archivos/", nom_arch_2)

def start(dato_jugador):
    dato_jugador_actual = {}
    dato_jugador_actual = dato_jugador
    try:
        with open(ruta_archivo_2, "r") as file:
            fjson = json.load(file)
            with open(ruta_archivo_2, "w") as file:
                json.dump(dato_jugador_actual, file, indent=4)
    except:
         with open(ruta_archivo_2, "x") as file:
             json.dump(dato_jugador_actual, file, indent=4)
             
        
