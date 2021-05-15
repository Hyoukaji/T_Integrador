import PySimpleGUI as sg
from src.Windows import introduzca_texto
#Abrimos la ventana para cambiar los textos del juego

def start():

    window, x = loop()
    window.close()
    return x

def loop():
    t = "Texto in game"
    tx = "Introduzca un texto para actualizar"
    window = introduzca_texto.build(tx, t)

    while True:
        event, values = window.read()

        if event in (sg.WINDOW_CLOSED, "-exit-"):
            break
        if event == "-update-":
            x = values[0]
            break
    return window, x
