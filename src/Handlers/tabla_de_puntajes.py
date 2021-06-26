import json
import pandas as pd
import os
import os.path

archivo = "jugadores.json"
ruta_archivo = os.path.join("src/Archivos", archivo)

def start():
    if os.path.exists(ruta_archivo):
        dicci = {}
        with open(ruta_archivo, "r") as archivo:
            dicci = json.load(archivo)
            df = pd.DataFrame([[key, dicci[key]['puntos']] for key in dicci.keys()], columns=['Nick', 'Puntaje', 'Nivel'])
            df = df.sort_values(['Puntaje'], ascending = False)
            df.to_csv("src/Archivos/Tabla_Puntajes") #podria arrojar error porque no lo probe
    else:
        print("La ruta al archivo esta rota")