from src.Handlers import get_criterios
import random

def start(matriz):
    _titulo, criterio_actual = get_criterios.start()
    p1 = criterio_actual[0]
    print(p1)
    p2 = criterio_actual[1]
    p3 = criterio_actual[2]
    cont = 0
    print(cont)
    while cont != 6:
        x = random.randint(0, 1)
        print(x)
        y = random.randint(0, 2)
        print(y)
        while cont != 2:
            print(x,y)
            if not matriz[x][y]["set"]:
                print("dentro del if")
                matriz[x][y]["criterio"] = p1
                matriz[x][y]["set"] = True
                cont += 1
                x = random.randint(0, 1)
                y = random.randint(0, 2)
            else :
                print("dentro del else")
                print (cont)
                x = random.randint(0, 1)
                y = random.randint(0, 2)

        while cont != 4:
            if not matriz[x][y]["set"]:
                matriz[x][y]["criterio"] = p2
                matriz[x][y]["set"] = True
                cont += 1
                x = random.randint(0, 1)
                y = random.randint(0, 2)
            else :
                x = random.randint(0, 1)
                y = random.randint(0, 2)

        while cont != 6:
            if not matriz[x][y]["set"]:
                matriz[x][y]["criterio"] = p3
                matriz[x][y]["set"] = True
                cont += 1
                x = random.randint(0, 1)
                y = random.randint(0, 2)
            else :
                x = random.randint(0, 1)
                y = random.randint(0, 2)

    return matriz
