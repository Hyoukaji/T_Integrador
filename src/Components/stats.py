import PySimpleGUI as sg
from src.Windows import a_b_c
from src.Handlers import estadisticas
from src.Components import imagen


def start():

    window = loop()
    window.close()

def loop():

    window = a_b_c.build("Top 10","Grafico por estado","Grafico por género","Estadisticas de partidas")

    while True:
        event, _values = window.read()

        if event in (sg.WINDOW_CLOSED, "-exit-"):
            break

        if event == "-a-":
            window.hide()
            estadisticas.start_1()
            imagen.start("tabla_de_estadistica.png")
            window.un_hide()
        if event == "-b-":
            window.hide()
            estadisticas.start_2()
            imagen.start("grafico_2.png")
            window.un_hide()
        if event == "-c-":
            window.hide()
            estadisticas.start_3()
            imagen.start("grafico_3.png")
            window.un_hide()
    return window
