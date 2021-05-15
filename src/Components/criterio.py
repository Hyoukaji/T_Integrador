import PySimpleGUI as sg
from src.Windows import criterio
#Abrimos el la ventana para configurar al jugador

def start():

    window = loop()
    window.close()

def loop():

    window = criterio.build()

    while True:
        event, _values = window.read()

        if event in (sg.WINDOW_CLOSED, "-exit-"):
            break

        if event == "-criterio1-":
            window.hide()
            #texto_in_game.start()
            window.un_hide()
        if event == "-criterio2-":
            window.hide()
            #texto_in_game.start()
            window.un_hide()

    return window
