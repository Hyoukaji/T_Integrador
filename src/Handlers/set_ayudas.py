<<<<<<< HEAD
#!/usr/bin/env python
# coding: utf-8

# In[19]:


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

def set_ayudas(valor):
    try:
        with open(ruta_archivo_2, "r") as archivo_2:
            dato_jugador_actual = json.load(archivo_2)
            dato_jugador_actual["ayuda"] = valor
            with open(ruta_archivo_2, "w") as file:
                json.dump(dato_jugador_actual, file, indent=4)                      
    except FileNotFoundError:
        print("Archivo de jugadores no encontrado")
        
set_ayudas(True)


# In[ ]:
=======
>>>>>>> 782b3a38d174d88a004eebe1e06bfc1d4a831028




<<<<<<< HEAD
=======
def start(ok):
>>>>>>> 782b3a38d174d88a004eebe1e06bfc1d4a831028