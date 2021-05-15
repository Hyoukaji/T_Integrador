#Datos de cada casilla del tablero
def start(tipo, info, x, y, z):
    casilla = {'1er_click' : [0,0], 'match?' : False, 'cant_click': 0 }
    criterio = {"tipo" : tipo, "info" : info}
    equipo = x
    cant_match = z
    mask = "?"
    board_data = [casilla, criterio, equipo, mask, cant_match]
    matriz = [[board_data] * y for _i in range(y)]

    return matriz
