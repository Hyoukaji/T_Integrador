import PySimpleGUI as sg
from src.Windows import menu
from src.Components import board
from src.Components import loginRegister
from src.Components import settings
from src.Components import inicio_sesion
#Menu de components
def start():
    inicio_sesion.start()
    #Aca se ejecuta la ventana del menu
    window = loop()
    window.close()

def loop():
    okp = True
    #Loop para captar eventos
    window = menu.build()

    while True:
        event, values = window.read()

        if event in (sg.WINDOW_CLOSED, "-exit-"):
            break
        print (event)
        print (values)
        if event == "-play-":
            if okp :
                window.hide()
                board.start()
                window.un_hide()
            else:
                sg.popup("Tienes que estar logueado para jugar")
        if event == "-login/register-":
            window.hide()
            loginRegister.start()
            window.un_hide()
        if event == "-settings-":
            window.hide()
            settings.start()
            window.un_hide()
        #if event == "-score-":
            #window.hide()
            #window.un_hide()
        #if event == "-stats-":
            #window.hide()
            #window.un_hide()
    return window
