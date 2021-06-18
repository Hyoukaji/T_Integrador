import pandas as pd
import os
import os.path

def start ():
    nom_arch = "registro_de_eventos"
    ruta_archivo = os.path.join("src/Archivos/", nom_arch)
    try:
        if os.path.exists(ruta_archivo):
            data_frame = pd.read_csv(ruta_archivo)
            cant = data_frame.tail(1)['Partida']
            return cant
        else:
            return 1
    except FileNotFoundError:
        print("La ruta esta rota")