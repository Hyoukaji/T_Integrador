#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import json
from json import JSONEncoder
import os
import os.path
import claseJugador

nom_Pro = "T_Integrador"
ruta_proyecto = os.path.join(os.getcwd(),nom_Pro)
nom_dir = "src"
ruta_directorio = os.path.join(ruta_proyecto, nom_dir)
nom_dir_2 = "Archivos"
ruta_directorio_2 = os.path.join(ruta_directorio, nom_dir_2)
nom_arch = "jugadores.json"
ruta_archivo = os.path.join(ruta_directorio_2, nom_arch) 

def buscar_jugador_login(unNick):
    try:
        archivo = open(ruta_archivo, "r")
        datos_jugadores = json.load(archivo)
        if unNick in datos_jugadores:
            return True
        else:
            return False
        archivo.close()    
    except FileNotFoundError:
        print("Archivo de jugadores no encontrado")
        return False
    

def get_jugador(unNick): 
    with open(ruta_archivo, "r") as archivo:
        datos_jugadores = json.load(archivo)
    return datos_jugadores[unNick]

def set_jugador_actual(unJugador):
    gamer = Jugador(unJugador[_nick],unJugador[_genero],unJugador[_edad])

