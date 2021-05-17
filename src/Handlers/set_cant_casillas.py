import json
import os
import os.path

nom_Pro = "T_Integrador"
ruta_proyecto = os.path.join(os.getcwd(),nom_Pro)

nom_dir = "src"
ruta_directorio = os.path.join(ruta_proyecto, nom_dir)

nom_dir_2 = "Archivos"
ruta_directorio_2 = os.path.join(ruta_directorio, nom_dir_2)

nom_arch_2= "jugador_actual.json"
ruta_archivo_2 = os.path.join(ruta_directorio_2, nom_arch_2) 

def start(unNick,valor):
    try:
        dato_jugador_actual = {}
        with open(ruta_archivo_2, "r") as archivo_2:
            dato_jugador_actual = json.load(archivo_2)
            dato_jugador_actual[unNick]["cant_casillas"] = valor
            with open(ruta_archivo_2, "w") as file:
                json.dump(dato_jugador_actual, file, indent=4)                      
    except FileNotFoundError:
        print("Archivo de jugadores no encontrado")
