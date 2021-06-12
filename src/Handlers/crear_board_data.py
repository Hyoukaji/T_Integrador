from src.Handlers import dar_logica
import random

#Datos de cada casilla del tablero

def start(c):
    criterio = "criterio"
    mask = "x"
    matriz = []
    for i in range(2):
        a = []
        for y in range (c):
            a.append([False,criterio,mask])
        matriz.append(a)

    matriz = dar_logica.start(matriz,c)
    return matriz
