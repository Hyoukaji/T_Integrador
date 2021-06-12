from src.Handlers import get_criterios
import random

def start(matriz):
    _titulo, criterio_actual = get_criterios.start()
    p1 = criterio_actual[0]
    p2 = criterio_actual[1]
    p3 = criterio_actual[2]
    criterio = 1
    cont = 0
    while cont != 2:
        x = random.randint(0, 1)
        y = random.randint(0, 2)
        if matriz[x][y][criterio] == "criterio":
            matriz[x][y][criterio] = p1
            cont = cont + 1
            x = random.randint(0, 1)
            y = random.randint(0, 2)
        else :
            x = random.randint(0, 1)
            y = random.randint(0, 2)
    while cont != 4:
        x = random.randint(0, 1)
        y = random.randint(0, 2)
        if matriz[x][y][criterio] == "criterio":
            matriz[x][y][criterio] = p2
            cont = cont + 1
            x = random.randint(0, 1)
            y = random.randint(0, 2)
        else :
            x = random.randint(0, 1)
            y = random.randint(0, 2)

    while cont != 6:
        x = random.randint(0, 1)
        y = random.randint(0, 2)
        if matriz[x][y][criterio] == "criterio":
            matriz[x][y][criterio] = p3
            cont = cont + 1
            x = random.randint(0, 1)
            y = random.randint(0, 2)
        else :
            x = random.randint(0, 1)
            y = random.randint(0, 2)

    return matriz
