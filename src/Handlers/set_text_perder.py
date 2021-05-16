<<<<<<< HEAD
#!/usr/bin/env python
# coding: utf-8

# In[ ]:


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

def set_text_perder(valor):
    try:
        with open(ruta_archivo_2, "r") as archivo_2:
            dato_jugador_actual = json.load(archivo_2)
            dato_jugador_actual["text_perder"] = valor
            with open(ruta_archivo_2, "w") as file:
                json.dump(dato_jugador_actual, file, indent=4)                      
    except FileNotFoundError:
        print("Archivo de jugadores no encontrado")

=======




def start(text):
>>>>>>> 782b3a38d174d88a004eebe1e06bfc1d4a831028
