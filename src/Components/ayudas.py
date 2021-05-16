import PySimpleGUI as sg
from src.Windows import a_b
from src.Handlers import set_ayudas

#Abrimos el la ventana para configurar al jugador

def start():

    window = loop()
    window.close()

def loop():

    window = a_b.build("Con Ayudas","Sin Ayudas","Ayudas")

    while True:
        event, _values = window.read()

        if event in (sg.WINDOW_CLOSED, "-exit-"):
            break

        if event == "-a-":
            ok = True
            set_ayudas.start(ok)
            sg.popup("Ayudas activadas")
            break
        if event == "-b-":
            ok = False
            set_ayudas.start(ok)
            sg.popup("Ayudas desactivadas")
            break
    return window
