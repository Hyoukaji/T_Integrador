import PySimpleGUI as sg
from src.Windows import introduzca_texto
#Abrimos la ventana para logearse

def start():

    window = loop()
    window.close()

def loop():
    t = "Login"
    tx = "Introduzca un nick existente"
    b = "Buscar"
    window = introduzca_texto.build(tx, b, t)

    while True:
        event, values = window.read()

        if event in (sg.WINDOW_CLOSED, "-exit-"):
            break

        if event == "-update-":
            text_input = values[0]
            sg.popup('You entered', text_input)
            break
    return window
