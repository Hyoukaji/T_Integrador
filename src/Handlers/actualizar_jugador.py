#!/usr/bin/env python
# coding: utf-8

# In[13]:


import json
from json import JSONEncoder
import os
import os.path

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

def actualizar_jugador(unNick):
    try:
        with open(ruta_archivo_2, "r") as archivo_2:
            dato_jugador_actual = json.load(archivo_2)
            if unNick not in dato_jugador_actual:    
                with open(ruta_archivo, "r") as archivo:
                    datos_jugadores = json.load(archivo)
                    dato_jugador_actual = datos_jugadores[unNick]
                    with open(ruta_archivo_2, "w") as file:
                        json.dump(dato_jugador_actual, file, indent=4)  
                        
    except FileNotFoundError:
        with open(ruta_archivo, "r") as archivo:
            datos_jugadores = json.load(archivo)
            dato_jugador_actual = datos_jugadores[unNick]
            with open(ruta_archivo_2, "w") as file:
                json.dump(dato_jugador_actual, file, indent=4) 
                



    


# In[ ]:





# In[ ]:




