#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import json
from json import JSONEncoder
import os
import os.path
from src.Archivos import claseJugador

nom_Pro = "T_Integrador"
ruta_proyecto = os.path.join(os.getcwd(),nom_Pro)
nom_dir = "src"
ruta_directorio = os.path.join(ruta_proyecto, nom_dir)
nom_dir_2 = "Archivos"
ruta_directorio_2 = os.path.join(ruta_directorio, nom_dir_2)
nom_arch = "jugadores.json"
ruta_archivo = os.path.join(ruta_directorio_2, nom_arch)


def start(unJugador):
    gamer = Jugador(unJugador[_nick],unJugador[_genero],unJugador[_edad])
