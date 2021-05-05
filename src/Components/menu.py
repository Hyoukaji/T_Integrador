import PySimpleGUI as sg
from src.Windows import menu
#Menu de components
def start():
    #Aca se ejecuta la ventana del menu
    window = loop()
    window.close()

def loop():
    #Loop para captar eventos
    window = menu.build()

    while True:
        event, values = window.read()

        if event in (sg.WINDOW_CLOSED, "Exit", "-exit-"):
            break
        print (event)
        print (values)
    return window
