import PySimpleGUI as sg
from src.Windows import menu
from src.Components import board
from src.Components import login_register
from src.Components import settings
from src.Components import inicio_sesion
from src.Handlers import colorear
from src.Handlers import actualizar_jugador
#from src.Handlers import print_criterio

def start():
    ok = False
    oks = inicio_sesion.start(ok)
    if oks:
        colorear.start()
    #Aca se ejecuta la ventana del menu principal
    window = loop(oks)
    window.close()

def loop(okp):
    #Loop para captar eventos
    window = menu.build()

    while True:
        event, values = window.read()

        if event in (sg.WINDOW_CLOSED, "-exit-"):
            if okp:
                actualizar_jugador.start()
            break

        if event == "-play-":
            if okp :
                #print_criterio.start()
                window.hide()
                board.start()
                window.un_hide()
            else:
                sg.popup("Tienes que estar logueado para jugar")
        if event == "-login/register-":
            window.hide()
            okp = login_register.start(okp)
            if okp:
                colorear.start()
            window.un_hide()
        if event == "-settings-":
            if okp:
                window.hide()
                settings.start()
                window.un_hide()
            else:
                sg.popup("Tienes que estar logueado para configurar")
        #if event == "-score-":
            #window.hide()
            #window.un_hide()
        #if event == "-stats-":
            #window.hide()
            #window.un_hide()
    return window
