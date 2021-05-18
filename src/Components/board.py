import PySimpleGUI as sg
from src.Windows import board
from src.Handlers import crear_board_data
from src.Handlers import dame_numeros
from src.Handlers import get_jugador_actual
from src.Handlers import get_nick_actual

#Abrimos el tablero del juego

def start():
    window = loop()
    window.close()
def loop():

    jugador = get_jugador_actual.start()
    nick = get_nick_actual.start()
    cant_casillas1 = jugador[nick]["cant_casillas"][0]
    cant_match = jugador[nick]["matchs"]
    nick = get_nick_actual.start()
    equipos, tam_resto = dame_numeros.start(cant_casillas1, cant_match)
    board_data = crear_board_data.start("tipo:palabras/img", "info", equipos, cant_casillas1, cant_match)

    window = board.build(nick, cant_casillas1)

    while True:
        event, _values = window.read()

        if event in (sg.WINDOW_CLOSED, "-exit-"):
            break

        if event.startswith("cell"):
            _perfix, x, y = event.split("-")
            z = int(x)
            v = int(y)
            if board_data[z][v]["mask"] == "x":
                board_data[z][v]["mask"] = "?"
                window[event].update("?")
            else:
                board_data[z][v]["mask"] = "x"
                window[event].update("x")
            print (f"celda: {x},{y}")

    return window
