import PySimpleGUI as sg
from src.Windows import settings
from src.Components import texto_in_game
from src.Components import colores
from src.Components import matchs
from src.Components import cant_casillas
from src.Components import ayudas
from src.Components import timing

#Abrimos el la ventana para configurar al jugador

def start():
    window = loop()
    window.close()

def loop():

    window = settings.build()

    while True:
        event, _values = window.read()

        if event in (sg.WINDOW_CLOSED, "-exit-"):
            break

        if event == "-ayudas-":
            window.hide()
            ayudas.start()
            window.un_hide()
        if event == "-timing-":
            window.hide()
            timing.start()
            window.un_hide()
        if event == "-casillas-":
            window.hide()
            cant_casillas.start()
            window.un_hide()
        if event == "-matchs-":
            window.hide()
            matchs.start()
            window.un_hide()
        if event == "-text-":
            window.hide()
            texto_in_game.start()
            window.un_hide()
        if event == "-color-":
            window.hide()
            colores.start()
            window.un_hide()

    return window
