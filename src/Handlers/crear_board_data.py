from src.Handlers import dar_logica
import random

#Datos de cada casilla del tablero

def start(c):
    criterio = "criterio"
    mask = "x"
    matriz = []
    r = 2
    g = c
    if c == 6:
        r = 3
        g = 4
    for i in range(r):
        a = []
        for y in range (g):
            a.append([False,criterio,mask])
        matriz.append(a)

    matriz = dar_logica.start(matriz,c,r,g)
    return matriz
