#!/usr/bin/env python
# coding: utf-8

<<<<<<< HEAD
# In[4]:
=======
# In[ ]:
>>>>>>> 782b3a38d174d88a004eebe1e06bfc1d4a831028


import json
from json import JSONEncoder
import os
import os.path
<<<<<<< HEAD
get_ipython().run_line_magic('run', './claseJugador.ipynb')

nom_Pro = "T_Integrador"
ruta_proyecto = os.path.join(os.getcwd(),nom_Pro)

nom_dir = "src"
ruta_directorio = os.path.join(ruta_proyecto, nom_dir)

nom_dir_2 = "Archivos"
ruta_directorio_2 = os.path.join(ruta_directorio, nom_dir_2)

nom_arch_2= "jugador_actual.json"
ruta_archivo_2 = os.path.join(ruta_directorio_2, nom_arch_2) 

nom_arch = "jugadores.json"
ruta_archivo = os.path.join(ruta_directorio_2, nom_arch) 

def set_jugador_actual(unNick,unGenero,unaEdad):
    dato_jugador_actual = Jugador(unNick,unGenero,unaEdad)
    persona_json = JugadorEncoder().encode(dato_jugador_actual)
    print(persona_json)
    with open(ruta_archivo_2, "w") as file:
        json.dump(persona_json, file, indent=4)  
                        


# In[ ]:




=======
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
>>>>>>> 782b3a38d174d88a004eebe1e06bfc1d4a831028
