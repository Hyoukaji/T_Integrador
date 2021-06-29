import csv
import os
import os.path
import pandas as pd
from matplotlib import pyplot as plt
from pandas.plotting import table 
import dataframe_image as dfi


nom_arch = "registro_de_eventos"
ruta_archivo = os.path.join("src/Archivos/", nom_arch)

def start_1 ():
    try:
        if os.path.exists(ruta_archivo):
            df = pd.read_csv(ruta_archivo)
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
            df_styled = tabla.style.background_gradient()
            nom = 'tabla_de_estadistica.png'
            archivo = os.path.join("src/Archivos/", nom)
            dfi.export(df_styled,archivo)
        else:
            print("Ups! El registro de jugadas no se ha encontrado")

    except FileNotFoundError:
        print("La ruta esta rota")

def start_2():
    #Gráfico que muestre el porcentaje de partidas por estado (terminada, cancelada,abandonadas).
    try:
        if os.path.exists(ruta_archivo):
            df = pd.read_csv(ruta_archivo)
            df['Palabra'].fillna('Sin datos', inplace = True)
            df['Estado'].fillna('Sin datos', inplace = True)
            df = df[((df['Nombre evento']=='fin')|(df['Nombre evento']=="sin terminar"))|(df['Nombre evento']=='"sin terminar"')]
            data = df.groupby(['Partida', 'Nombre evento'])['Partida'].count()

            #Grafico

            etiquetas = data.keys()
            datos = data.values
            plt.pie(datos, labels=etiquetas, autopct='%1.1f%%',
            shadow=True, startangle=90, labeldistance= 1.1)
            plt.axis('equal')
            plt.legend(etiquetas)
            plt.title(f'Porcentaje de partidas por estado')
            nom = "grafico_2.png"
            archivo = os.path.join("src/Archivos/", nom)
            plt.savefig(archivo, format = 'png')
            plt.show()
        else:
            print("Ups! El .png no se ha encontrado")
    except FileNotFoundError:
        print("La ruta esta rota")

def start_3():
    #Gráfico que muestre el porcentaje de partidas finalizadas según género
    try:
        if os.path.exists(ruta_archivo):
            df = pd.read_csv(ruta_archivo)
            df['Palabra'].fillna('Sin datos', inplace = True)
            df['Estado'].fillna('Sin datos', inplace = True)
            df = df[df['Estado']=='finalizada']
            data = df.groupby(['genero', 'Estado'])['genero'].count()

            #Grafico

            etiquetas = data.keys()
            datos = data.values
            plt.pie(datos, labels=etiquetas, autopct='%1.1f%%',
            shadow=True, startangle=90, labeldistance= 1.1)
            plt.axis('equal')
            plt.legend(etiquetas)
            plt.title(f'Porcentaje de partidas finalizadas por genero')
            nom = "grafico_3.png"
            archivo = os.path.join("src/Archivos/", nom)
            plt.savefig(archivo, format = 'png')
            plt.show()
        else:
            print("Ups! El .png no se ha encontrado")
    except FileNotFoundError:
        print("La ruta esta rota")
    
