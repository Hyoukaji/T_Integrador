import PySimpleGUI as sg
from src.Windows import introduzca_texto
from src.Components import cant_casillas3

def start():

    window,x ,z = loop()
    window.close()
    return x, z
def loop():
    t = "Cantidad de casillas"
    tx = "Introduzca un número de casillas para el nivel 2"
    b = "Actualizar"
    window = introduzca_texto.build(tx, b, t)

    while True:
        event, values = window.read()



        if event == "-update-":
            text_input = values[0]
            try:
                x = int(text_input)
                z = cant_casillas3.start()
                break
            except:
                sg.popup("Tienes que ingresar un número entero")

    return window, x, z
