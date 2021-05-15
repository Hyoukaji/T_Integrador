import PySimpleGUI as sg
from src.Windows import texto_in_game
from src.Components import introduzca_textoG
#Abrimos la ventana para cambiar los textos del juego

def start():

    window = loop()
    window.close()

def loop():

    window = texto_in_game.build()

    while True:
        event, values = window.read()

        if event in (sg.WINDOW_CLOSED, "-exit-"):
            break

        if event == "-ganar-":
            text_input = introduzca_textoG.start()
            sg.popup('You entered', text_input)
        if event == "-perder-":
            text_input = introduzca_textoG.start()
            sg.popup('You entered', text_input)
        if event == "-pocoT-":
            text_input = introduzca_textoG.start()
            sg.popup('You entered', text_input)

    return window
