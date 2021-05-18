import PySimpleGUI as sg
from src.Windows import introduzca_texto
#Abrimos la ventana para cambiar los textos del juego

def start():

    window, x= loop()
    window.close()
    return x
def loop():
    t = "Genero"
    tx = "Introduzca su género"
    b = "Actualizar"
    window = introduzca_texto.build(tx, b, t)

    while True:
        event, values = window.read()

        if event in (sg.WINDOW_CLOSED, "-exit-"):
            break
        if event == "-update-":
            text_input = values[0]
            sg.popup('Seteaste tu genero en:', text_input)
            break
    return window, text_input
