import PySimpleGUI as sg
from src.Windows import board
#Abrimos el tablero del juego

def start():
    #Aca se ejecuta la ventana del tablero
    window = loop()
    window.close()

def loop():
    #Loop para captar eventos del tablero, y le damos el/los jugador/es
    window = board.build("jugador 1", "jugador 2")

    while True:
        event, _values = window.read()

        if event in (sg.WINDOW_CLOSED, "Exit", "-exit-"):
            break

        if event.startswith("cell"):
            _perfix, x, y = event.split("-")
            print (f"celda: {x},{y}")

    return window
