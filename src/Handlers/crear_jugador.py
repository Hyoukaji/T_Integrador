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
        datos_jugadores = {}
        if os.path.exists(ruta_archivo):
            with open(ruta_archivo, "r") as archivo:
                datos_jugadores = json.load(archivo)
                datos_jugadores[unNick] = {"genero": "Sin indicar","edad" : 0,"puntos" : 0,"tiempo" : 180, "cant_casillas" : 4, "matchs" : 2,"elemento_casilla" : 0,"ayuda" : False,"color" : "ninguno", "text_ganar"  : "Ganaste", "text_perder" :"Perdiste","text_pocoT " : "Te queda poco tiempo D:"}
                with open(ruta_archivo, 'w') as file:
                    json.dump(datos_jugadores, file, indent=4)
        else:
            datos_jugadores[unNick] = {"genero": "Sin indicar","edad" : 0,"puntos" : 0,"tiempo" : 180, "cant_casillas" : 4,"matchs" : 2,"elemento_casilla" : 0, "ayuda ": False,"color" : "ninguno","text_ganar"  : "Ganaste","text_perder" :"Perdiste","text_pocoT " : "Te queda poco tiempo D:"}
            with open(ruta_archivo, 'w') as file:
                json.dump(datos_jugadores, file, indent=4)
    except FileNotFoundError:
        print("Archivo de jugadores no encontrado")

