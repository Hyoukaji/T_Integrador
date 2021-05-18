import PySimpleGUI as sg
from src.Windows import introduzca_texto
from src.Handlers import set_timing
#Abrimos la ventana para cambiar los textos del juego

def start():

    window = loop()
    window.close()

def loop():
    t = "Tiempo de Juego"
    tx = "Introduzca un número para actualizar el tiempo de partida"
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
                set_timing.start(x)
                sg.popup("Seteaste el tiempo en:", x)
                break
            except:
                sg.popup("Tienes que ingresar un número entero")

    return window
