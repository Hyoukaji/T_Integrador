import PySimpleGUI as sg
from src.Windows import menu
from src.Components import board
from src.Components import login_register
from src.Components import settings
from src.Components import inicio_sesion
#from src.Archivos import get_jugador_actual
#from src.Handlers import actualizar_jugador

def start():
    ok = False
    oks = inicio_sesion.start(ok)
    if oks:
        jugador = get_jugador_actual.start()
        if jugador.color != "ninguno":
            sg.theme(jugador.color)
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
                #actualizar_jugador.start()
            break
        
        if event == "-play-":
            if okp :
                window.hide()
                board.start()
                window.un_hide()
            else:
                sg.popup("Tienes que estar logueado para jugar")
        if event == "-login/register-":
            window.hide()
            okp = login_register.start(okp)
            if okp:
                jugador = get_jugador_actual.start()
                if jugador.color != "ninguno":
                    sg.theme(jugador.color)
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
