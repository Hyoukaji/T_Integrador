import PySimpleGUI as sg
from src.Windows import board
from src.Handlers import boardData
#Abrimos el tablero del juego

def start():
    #Aca se ejecuta la ventana del tablero
    window = loop()
    window.close()
    #Loop para captar eventos del tablero
def loop():
    #Aca bolcamos la info del jugador
    board_data = boardData.start("tipo", "info", "match", 3 , 4)

    window = board.build("jugador 1", board_data)

    while True:
        event, _values = window.read()

        if event in (sg.WINDOW_CLOSED, "-exit-"):
            break

        if event.startswith("cell"):
            _perfix, x, y = event.split("-")
            print (f"celda: {x},{y}")

    return window
