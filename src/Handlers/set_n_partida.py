import csv
import os
import os.path

def start ():
    nom_arch = "registro_de_eventos.csv"
    ruta_archivo = os.path.join("src/Archivos/", nom_arch)
    try:
        if os.path.exists(ruta_archivo):
            with open(ruta_archivo, "r") as file:
                reader = csv.reader(file)
                filas = file.read().splitlines()
                ult_fila = (filas[-2]).split(',')
                if ult_fila[7] == 'finalizada' or ult_fila[7] == 'fin' or ult_fila[7] == 'timeout' :
                    return int(ult_fila[1]) + 1
                else:
                    return int(ult_fila[1])
        else:
            return 1
    except FileNotFoundError:
        print("La ruta esta rota")
