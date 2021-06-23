import csv
import os
import os.path
import pandas as pd
from matplotlib import pyplot as plt
#%matplotlib inline

def star_1 ():
    nom_arch = "registro_de_eventos"
    ruta_archivo = os.path.join("src/Archivos/", nom_arch)
    try:
        if os.path.exists(ruta_archivo):
            df = pd.read_csv("datos de prueba.csv")
            df['Palabra'].fillna('Sin datos', inplace = True)
            df['Estado'].fillna('Sin datos', inplace = True)

            #Creo un diccionario cuyas claves son las partidas jugadas y su valor es false
            partidas = df['Partida'].unique()
            dicci = {}
            for i in partidas:
                dicci[i] = False
    
            #filtro el data frame
            df_intentos=df[df['Estado']=='match']

            #Creo una tabla con las primeras palabras halladas por partida
            tabla = pd.DataFrame(columns=['Partida', 'Palabra'])
            for i in df_intentos.index:
                num = df_intentos["Partida"][i] 
                if dicci[num] == False:
                    tabla.loc[i] = [num] + [df_intentos['Palabra'][i]]
                    dicci[num] = True
            print(tabla)
        else:
            print("Ups! El registro de jugadas no se ha encontrado")

    except FileNotFoundError:
        print("La ruta esta rota")
