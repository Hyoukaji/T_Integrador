import PySimpleGUI as sg
from src.Windows import settings
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

        #if event == "-login-":
            #window.hide()
            #Login.start()
            #window.un_hide()
        #if event == "-login-":

    return window
