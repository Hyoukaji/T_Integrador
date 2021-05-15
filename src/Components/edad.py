import PySimpleGUI as sg
from src.Windows import introduzca_texto
#Abrimos la ventana para cambiar los textos del juego

def start():

    window = loop()
    window.close()

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
                sg.popup('You entered', text_input)
                break
            except:
                sg.popup("Tienes que ingresar un número entero")
            
    return window
