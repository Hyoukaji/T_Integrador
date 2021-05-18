import PySimpleGUI as sg
from src.Windows import introduzca_texto

def start():

    window, x= loop()
    window.close()
    return x
def loop():
    t = "Edad"
    tx = "Introduzca su edad"
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
                sg.popup('Seteaste tu edad en:', text_input)
                break
            except:
                sg.popup("Tienes que ingresar un número entero")

    return window, x
