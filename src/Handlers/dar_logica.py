from src.Handlers import get_criterios
import random

def start(matriz, c):
    _titulo, criterio_actual = get_criterios.start()
    lista = []
    for y in range (c):
        lista.append(criterio_actual[y])
    criterio = 1
    tot = c * 2
    cont = 0
    n = 0
    pal = 2
    tope = c - 1
    x = random.randint(0, 1)
    y = random.randint(0,tope)
    while cont != tot:
        while cont != pal:
            if matriz[x][y][criterio] == "criterio":
                matriz[x][y][criterio] = lista[n]
                cont = cont + 1
                x = random.randint(0, 1)
                y = random.randint(0, tope)
            else :
                x = random.randint(0, 1)
                y = random.randint(0, tope)
        n = n + 1
        pal = pal + 2

    return matriz
