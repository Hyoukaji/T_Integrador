#Calculos que nos daran los numeros necesarios para construir el tablero
def start(x, y):
    x = x * x
    resto = 0
    #CALCULAR EL RESTO PARA VER SI DA PAR O NO
    if (x % y != 0):
        resto = 1
        z = x/y + 1
    else:
        z = x/y
    return z , resto
