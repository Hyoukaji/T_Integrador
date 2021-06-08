import PySimpleGUI as sg
from src.Windows import introduzca_texto
from src.Handlers import set_cant_casillas
from src.Components import cant_casillas2

def start():

    window = loop()
    window.close()

def loop():
    t = "Cantidad de casillas"
    tx = "Introduzca un número de casillas para el nivel 1"
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
                y, z = cant_casillas2.start()
                set_cant_casillas.start(x, y, z)
                break
            except:
                sg.popup("Tienes que ingresar un número entero")

    return window
