import PySimpleGUI as sg
from src.Windows import introduzca_texto
from src.Handlers import set_matchs

#Abrimos la ventana para cambiar los textos del juego

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
                sg.popup("Seteaste la cantidad de coincidencias en :", x)
                break
            except:
                sg.popup("Tienes que ingresar un número entero")

    return window
