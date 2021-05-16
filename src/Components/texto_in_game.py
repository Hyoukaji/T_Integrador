import PySimpleGUI as sg
from src.Windows import texto_in_game
from src.Components import introduzca_textoG
from src.Handlers import set_text_ganar
from src.Handlers import set_text_perder
from src.Handlers import set_text_pocoT

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
            set_text_ganar.start(text_input)
            sg.popup("Seteaste el texto al ganar en:" + text_input)
        if event == "-perder-":
            text_input = introduzca_textoG.start()
            set_text_perder.start(text_input)
            sg.popup("Seteaste el texto al perder en:" + text_input)
        if event == "-pocoT-":
            text_input = introduzca_textoG.start()
            set_text_pocoT.start(text_input)
            sg.popup("Seteaste el texto al quedar poco tiempo en:" + text_input)

    return window
