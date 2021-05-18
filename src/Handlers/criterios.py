import os
import os.path
import csv

def start_1():
    nom_arch = "anime.csv"
    ruta_archivo= os.path.join("src/Archivos/", nom_arch)
    with open(ruta_archivo, "r", encoding = "utf-8") as anime_arch:
        csvreader = csv.reader(anime_arch, delimiter=',') 
        encabezado = next(csvreader)
        lista = list(map(lambda x: x[1],list(filter(lambda x: x[3]=='TV',csvreader))))
    return "Titulo de series de anime de la TV", lista

def start_2():    
    nom_arch = "persona_comiendo.csv"
    ruta_archivo= os.path.join("src/Archivos/", nom_arch)
    with open(ruta_archivo, "r", encoding = "utf-8") as persona_arch:
        csvreader = csv.reader(persona_arch, delimiter=',') 
        encabezado = next(csvreader)
        lista = list(map(lambda row: row[10], csvreader))
    return "Personas cominedo", lista

def start_3():    
    nom_arch = "art.csv"
    ruta_archivo= os.path.join("src/Archivos/", nom_arch)
    with open(ruta_archivo, "r", encoding = "utf-8") as art_arch:
        csvreader = csv.reader(art_arch, delimiter=',') 
        encabezado = next(csvreader)
        lista = list(map(lambda row:{row[8]:row[5]}, csvreader))
    return "Titulos de obras de Arte", lista

def start_4():
    nom_arch = "Countries.csv"
    ruta_archivo= os.path.join("src/Archivos/", nom_arch)
    with open(ruta_archivo, "r", encoding = "utf-8") as paises_arch:
        csvreader = csv.reader(paises_arch, delimiter=',') 
        encabezado = next(csvreader)
        lista = list(map(lambda row:{row[0]:row[5]}, csvreader))
    return "Banderas de todos los paises del mundo", lista

def start_5():
    nom_arch = "disney-characters.csv"
    ruta_archivo= os.path.join("src/Archivos/", nom_arch)
    with open(ruta_archivo, "r") as disney_arch:
        csvreader = csv.reader(disney_arch, delimiter=',') 
        encabezado = next(csvreader)
        lista = list(map(lambda row:row[2], csvreader))
    return "Heroes de las peliculas de Disney", lista

def start_6():
    nom_arch = "disney-characters.csv"
    ruta_archivo= os.path.join("src/Archivos/", nom_arch)
    with open(ruta_archivo, "r") as disney_arch:
        csvreader = csv.reader(disney_arch, delimiter=',') 
        encabezado = next(csvreader)
        lista = list(map(lambda row:row[3], csvreader))
    return "Villanos de las peliculas de Disney", lista

def start_7():
    nom_arch = "battles.csv"
    ruta_archivo= os.path.join("src/Archivos/", nom_arch)
    with open(ruta_archivo, "r") as batallas_arch:
        csvreader = csv.reader(batallas_arch, delimiter=',') 
        encabezado = next(csvreader)
        lista = list(map(lambda row:row[0], csvreader))
    return "Batallas libradas de Game of throne", lista


def start_8():
    nom_arch = "character-deaths.csv"
    ruta_archivo= os.path.join("src/Archivos/", nom_arch)
    with open(ruta_archivo, "r") as pergot_arch:
        csvreader = csv.reader(pergot_arch, delimiter=',') 
        encabezado = next(csvreader)
        lista = list(map(lambda row:row[0], csvreader))
    return "Personajes fallecidos de Game of throne", lista

