import pandas as pd
import os
import os.path
import matplotlib as plt
from os import remove
import dataframe_image as dfi


nom_arch = "puntajes.csv"
ruta_archivo = os.path.join("src/Archivos/", nom_arch)

def start_1():
    # Tabla de usuarios y puntos
    if os.path.exists(ruta_archivo):  
        df = pd.read_csv(ruta_archivo)     
        df_1 = df[['Nick','Puntaje']].sort_values('Puntaje', ascending=False)
        nom = 'tabla_1.png'
        archivo = os.path.join("src/Archivos/", nom)
        if os.path.exists(archivo): 
            remove(archivo)
        df_styled = df_1.style.background_gradient()
        dfi.export(df_styled,archivo)
    else:
        print("La ruta al archivo esta rota")

def start_2():
    #Tabla de usuarios y puntos nivel facil
    if os.path.exists(ruta_archivo):
        df = pd.read_csv(ruta_archivo)
        df_2 = df[df['Nivel']=='facil'].groupby(['Nick'])['Puntaje'].sum().sort_values(ascending=False)
        data = pd.DataFrame(df_2)
        nom = 'tabla_2.png'
        archivo = os.path.join("src/Archivos/", nom)
        if os.path.exists(archivo): 
            remove(archivo)
        df_styled = data.style.background_gradient()
        dfi.export(df_styled,archivo)
    else:
        print("La ruta al archivo esta rota")

def start_3():
    #Tabla de usuarios y puntos nivel medio
    if os.path.exists(ruta_archivo): 
        df = pd.read_csv(ruta_archivo)
        df_3 = df[df['Nivel']=='medio'].groupby(['Nick'])['Puntaje'].sum().sort_values(ascending=False)
        data = pd.DataFrame(df_3)
        nom = 'tabla_3.png'
        archivo = os.path.join("src/Archivos/", nom)
        if os.path.exists(archivo): 
            remove(archivo)
        df_styled = data.style.background_gradient()
        dfi.export(df_styled,archivo)
    else:
        print("La ruta al archivo esta rota")

def start_4():
    #Tabla de usuarios y puntos nivel dificil
    if os.path.exists(ruta_archivo): 
        df = pd.read_csv(ruta_archivo)
        df_4 = df[df['Nivel']=='dificil'].groupby(['Nick'])['Puntaje'].sum().sort_values(ascending=False)
        data = pd.DataFrame(df_4)
        nom = 'tabla_4.png'
        archivo = os.path.join("src/Archivos/", nom)
        if os.path.exists(archivo): 
            remove(archivo)
        df_styled = data.style.background_gradient()
        dfi.export(df_styled,archivo)
    else:
        print("La ruta al archivo esta rota")


