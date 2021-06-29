import pandas as pd
import os
import os.path
import matplotlib.pyplot as plt
from pandas.plotting import table 

nom_arch = "puntajes.csv"
ruta_archivo = os.path.join("src/Archivos/", nom_arch)

def start_1():
    # Tabla de usuarios y puntos
    if os.path.exists(ruta_archivo):  
        df = pd.read_csv("puntajes.csv")     
        df_1 = df[['Nick','Puntaje']].sort_values('Puntaje', ascending=False)
        ax = plt.subplot(111, frame_on=False) 
        ax.xaxis.set_visible(False)  
        ax.yaxis.set_visible(False)  
        table(ax, df_1)
        nom = 'tabla_1.png'
        archivo = os.path.join("src/Archivos/", nom)
        plt.savefig(archivo)
    else:
        print("La ruta al archivo esta rota")

def start_2():
    #Tabla de usuarios y puntos nivel facil
    if os.path.exists(ruta_archivo):
        df = pd.read_csv("puntajes.csv")
        df_2 = df[df['Nivel']=='facil'].groupby(['Nick'])['Puntaje'].sum().sort_values(ascending=False)
        ax = plt.subplot(111, frame_on=False) 
        ax.xaxis.set_visible(False)  
        ax.yaxis.set_visible(False)  
        table(ax, df_2) 
        nom = 'tabla_2.png'
        archivo = os.path.join("src/Archivos/", nom)
        plt.savefig(archivo) 
    else:
        print("La ruta al archivo esta rota")

def start_3():
    #Tabla de usuarios y puntos nivel medio
    if os.path.exists(ruta_archivo): 
        df = pd.read_csv("puntajes.csv")
        df_3 = df[df['Nivel']=='medio'].groupby(['Nick'])['Puntaje'].sum().sort_values(ascending=False)
        ax = plt.subplot(111, frame_on=False) 
        ax.xaxis.set_visible(False)  
        ax.yaxis.set_visible(False)  
        table(ax, df_3) 
        nom = 'tabla_3.png'
        archivo = os.path.join("src/Archivos/", nom)
        plt.savefig(archivo) 
    else:
        print("La ruta al archivo esta rota")

def start_4():
    #Tabla de usuarios y puntos nivel dificil
    if os.path.exists(ruta_archivo): 
        df = pd.read_csv("puntajes.csv")
        df_4 = df[df['Nivel']=='dificil'].groupby(['Nick'])['Puntaje'].sum().sort_values(ascending=False)
        ax = plt.subplot(111, frame_on=False) 
        ax.xaxis.set_visible(False)  
        ax.yaxis.set_visible(False)  
        table(ax, df_4) 
        nom = 'tabla_4 .png'
        archivo = os.path.join("src/Archivos/", nom)
        plt.savefig(archivo) 
    else:
        print("La ruta al archivo esta rota")


