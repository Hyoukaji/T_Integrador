import PySimpleGUI as sg
from src.Windows import colores
#Abrimos el la ventana para configurar al jugador

def start():

    window = loop()
    window.close()

def loop():

    window = colores.build()

    while True:
        event, _values = window.read()

        if event in (sg.WINDOW_CLOSED, "-exit-"):
            break

        if event == "-color1-":
            window.hide()
            #texto_in_game.start()
            window.un_hide()
        if event == "-color2-":
            window.hide()
            #texto_in_game.start()
            window.un_hide()

    return window
