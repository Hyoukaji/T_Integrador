import PySimpleGUI as sg
from src.Windows import menu
from src.Components import board
from src.Components import login_register
from src.Components import settings
from src.Components import inicio_sesion
from src.Components import selec_nivel
from src.Components import score
from src.Components import stats
from src.Handlers import colorear
from src.Handlers import actualizar_jugador
from src.Handlers import print_criterio

import random

def start():
    ok = False
    oks = inicio_sesion.start(ok)
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
                n, play = selec_nivel.start()
                if play:
                    board.start(n)
                else:
                    sg.popup("Tienes que seleccionar un nivel para poder jugar")
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
        if event == "-score-":
            window.hide()
            score.start()
            window.un_hide()
        if event == "-stats-":
            window.hide()
            stats.start()
            window.un_hide()
    return window
