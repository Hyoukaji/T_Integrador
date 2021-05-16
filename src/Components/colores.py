import PySimpleGUI as sg
from src.Windows import a_b
#from src.Handlers import set_color
#Abrimos el la ventana para configurar al jugador

def start():

    window, color = loop()
    window.close()
    #set_color.start(color)
    if (color != "ninguno"):
        sg.theme(color)
def loop():
    color = "ninguno"
    window = a_b.build("Set color 1", "Set color 2","Selección de color")

    while True:
        event, _values = window.read()

        if event in (sg.WINDOW_CLOSED, "-exit-"):
            break

        if event == "-a-":
            color = "DarkPurple2"
            sg.popup('You entered', color)
            break
        if event == "-b-":
            color = "DarkBrown4"
            sg.popup('You entered', color)
            break

    return window, color
