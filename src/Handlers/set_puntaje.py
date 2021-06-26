import csv
import os
import os.path

nom_arch = "puntajes"
ruta_archivo = os.path.join("src/Archivos/", nom_arch)


def start(nick = "unNick", nivel = 0, puntaje = 0):
    if nivel == 1:
        nivel = 'facil'
    elif nivel == 2:
        nivel = 'medio'
    else:
        nivel = 'dificil' 
    lista =[nick, puntaje, nivel]      
    try:
        if os.path.exists(ruta_archivo):
            with open(ruta_archivo,"a") as file:
                writer = csv.writer(file)
                writer.writerows(lista)
        else:
            with open(ruta_archivo,"w") as file:
                encabezado =[['Nick', 'Puntaje', 'Nivel']]
                writer = csv.writer(file)
                writer.writerows(encabezado)
                writer.writerows(lista)
    except FileNotFoundError:
        print("La ruta esta rota")