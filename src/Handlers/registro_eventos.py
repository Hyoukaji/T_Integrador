import csv
import os
import os.path
from src.Handlers import set_evento

def start (fila):
    nom_arch = "registro_de_eventos"
    ruta_archivo = os.path.join("src/Archivos/", nom_arch)
    try:
        if os.path.exists(ruta_archivo):
            with open(ruta_archivo,"a") as file:
                writer = csv.writer(file)
                writer.writerows(fila)
        else:
            with open(ruta_archivo,"w") as file:
                encabezado = ['Tiempo', 'Partida', 'Cantidad de palabras', 'Nombre evento', 'nick', 'genero', 'edad', 'Estado ', 'Palabra', 'nivel']
                writer = csv.writer(file)
                writer.writerows(encabezado)
                writer.writerows(fila)
    except FileNotFoundError:
        print("La ruta esta rota")