import pandas as pd
import os
import os.path

nom_arch = "puntajes"
ruta_archivo = os.path.join("src/Archivos/", nom_arch)

def start():
    if os.path.exists(ruta_archivo):
        df = pd.read_csv("puntajes")
        data = df.groupby(['Nick', 'Nivel'])['Puntaje'].sum()
        data.to_csv("src/Archivos/Tabla_Puntajes") #podria arrojar error porque no lo probe
    else:
        print("La ruta al archivo esta rota")