import PySimpleGUI as sg
from src.Windows import introduzca_texto
from src.Handlers import set_matchs


def start():

    window = loop()
    window.close()

def loop():
    t = "Matchs"
    tx = "Introduzca un número de coincidencias"
    b = "Actualizar"
    window = introduzca_texto.build(tx, b, t)

    while True:
        event, values = window.read()

        if event in (sg.WINDOW_CLOSED, "-exit-"):
            break

        if event == "-update-":
            text_input = values[0]
            try:
                x = int(text_input)
                set_matchs.start(x)
                break
            except:
                sg.popup("Tienes que ingresar un número entero")

    return window
