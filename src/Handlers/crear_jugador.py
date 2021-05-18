import json
import os
import os.path

nom_arch = "jugadores.json"
ruta_archivo = os.path.join("src/Archivos/", nom_arch)

def start(unNick, edad, genero):
    try:
        datos_jugadores = {}
        if os.path.exists(ruta_archivo):
            with open(ruta_archivo, "r") as archivo:
                datos_jugadores = json.load(archivo)
<<<<<<< HEAD
                datos_jugadores[unNick] = {"genero": genero,"edad" : edad,"puntos" : 0,"tiempo" : 180, "cant_casillas" : [2,4,6], "matchs" : 2,"elemento_casilla" : 0,"ayuda" : False,"color" : "ninguno", "text_ganar"  : "Ganaste", "text_perder" :"Perdiste","text_pocoT " : "Te queda poco tiempo D:"}
=======
                datos_jugadores[unNick] = {"genero": genero,"edad" : edad,"puntos" : 0,"tiempo" : 180, "cant_casillas" : 2, "matchs" : 2,"elemento_casilla" : 0,"ayuda" : False,"color" : "ninguno", "text_ganar"  : "Ganaste", "text_perder" :"Perdiste","text_pocoT " : "Te queda poco tiempo D:"}
>>>>>>> refs/remotes/origin/main
                with open(ruta_archivo, 'w') as file:
                    json.dump(datos_jugadores, file, indent=4)
        else:
            datos_jugadores[unNick] = {"genero": genero,"edad" : edad,"puntos" : 0,"tiempo" : 180, "cant_casillas" : [2,4,6],"matchs" : 2,"elemento_casilla" : 0, "ayuda ": False,"color" : "ninguno","text_ganar"  : "Ganaste","text_perder" :"Perdiste","text_pocoT " : "Te queda poco tiempo D:"}
            with open(ruta_archivo, 'w+') as file:
                json.dump(datos_jugadores, file, indent=4)
                json.dump(datos_jugadores, file, indent=4, cls=JugadorEncoder)
    except FileNotFoundError:
        print("Archivo de jugadores no encontrado")
