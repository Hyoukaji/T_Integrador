from src.Handlers import dar_logica
import random

#Datos de cada casilla del tablero

def start():
    criterio = "criterio"
    mask = "x"
    matriz = []
    for i in range(2):
        a = []
        for y in range (3):
            a.append([False,criterio,mask])
        matriz.append(a)

    matriz = dar_logica.start(matriz)
    return matriz
