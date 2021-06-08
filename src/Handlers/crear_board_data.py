from src.Handlers import dar_logica

#Datos de cada casilla del tablero

def start():
    casilla = False
    board_data = {"casilla" : casilla, "criterio" : "criterio", "mask" : "x", "set" : False}
    matriz = [[board_data] * 3 ] * 2
    matriz = dar_logica.start(matriz)

    return matriz
