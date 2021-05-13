import PySimpleGUI as sg
from src.Windows import board
#Abrimos el tablero del juego

def start():
    #Aca se ejecuta la ventana del tablero
    window = loop()
    window.close()

def loop():
    #Loop para captar eventos del tablero, y le damos el jugador
    window = board.build("jugador 1")

    while True:
        event, _values = window.read()

        if event in (sg.WINDOW_CLOSED, "-exit-"):
            break

        if event.startswith("cell"):
            _perfix, x, y = event.split("-")
            print (f"celda: {x},{y}")

    return window
