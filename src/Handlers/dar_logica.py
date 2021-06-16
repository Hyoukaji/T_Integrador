from src.Handlers import get_criterios
import random

def start(matriz, c,r,g):
    #_titulo, criterio_actual = get_criterios.start()
    criterio_actual = ["Kurt","Mike","Julio","Darius","Eren","Kyle"]
    lista = []
    for y in range (c):
        lista.append(criterio_actual[y])
    criterio = 1
    tot = c * 2
    cont = 0
    n = 0
    pal = 2
    tope = g - 1
    tope1 = r - 1
    x = random.randint(0, tope1)
    y = random.randint(0,tope)
    while cont != tot:
        while cont != pal:
            if matriz[x][y][criterio] == "criterio":
                matriz[x][y][criterio] = lista[n]
                cont = cont + 1
                x = random.randint(0, tope1)
                y = random.randint(0, tope)
            else :
                x = random.randint(0, tope1)
                y = random.randint(0, tope)
        n = n + 1
        pal = pal + 2

    return matriz
