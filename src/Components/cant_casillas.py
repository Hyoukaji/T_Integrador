import PySimpleGUI as sg
from src.Windows import introduzca_texto
#Abrimos la ventana para cambiar los textos del juego

def start():

    window = loop()
    window.close()

def loop():
    t = "Cantidad de casillas"
    tx = "Introduzca un número para elevarlo al cuadrado y crear el tablero"
    window = introduzca_texto.build(tx, t)

    while True:
        event, values = window.read()

        if event in (sg.WINDOW_CLOSED, "-exit-"):
            break

        if event == "-update-":
            text_input = values[0]
            #INTRODUCIR EXCEPCION POR STRING QUE PUEDA ENTRAR, QUEREMOS INTS!!!
            x = int(text_input)
            sg.popup('You entered', text_input)

    return window
