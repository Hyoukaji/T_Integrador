import PySimpleGUI as sg
from src.Windows import a_b_c_d
from src.Handlers import tabla_de_puntajes
from src.Components import imagen


def start():

    window = loop()
    window.close()

def loop():

    window = a_b_c_d.build("Tabla completa","Tabla facil","Tabla media","Tabla dificil","Tablas de puntuaciones")

    while True:
        event, _values = window.read()

        if event in (sg.WINDOW_CLOSED, "-exit-"):
            break

        if event == "-a-":
            window.hide()
            tabla_de_puntajes.start_1()
            imagen.start("tabla_1.png")
            window.un_hide()
        if event == "-b-":
            window.hide()
            tabla_de_puntajes.start_2()
            imagen.start("tabla_2.png")
            window.un_hide()
        if event == "-c-":
            window.hide()
            tabla_de_puntajes.start_3()
            imagen.start("tabla_3.png")
            window.un_hide()
        if event == "-d-":
            window.hide()
            tabla_de_puntajes.start_4()
            imagen.start("tabla_4.png")
            window.un_hide()
    return window
