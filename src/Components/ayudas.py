import PySimpleGUI as sg
from src.Windows import a_b
#Abrimos el la ventana para configurar al jugador

def start():

    window = loop()
    window.close()

def loop():

    window = a_b.build("Con Ayudas","Sin Ayudas","Ayudas")

    while True:
        event, _values = window.read()

        if event in (sg.WINDOW_CLOSED, "-exit-"):
            break

        if event == "-a-":
            window.hide()
            #texto_in_game.start()
            window.un_hide()
        if event == "-b-":
            window.hide()
            #texto_in_game.start()
            window.un_hide()

    return window
