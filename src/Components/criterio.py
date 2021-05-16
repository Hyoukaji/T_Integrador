import PySimpleGUI as sg
from src.Windows import a_b
#from src.Handlers import set_criterio
#from src.Handlers import get_nom_criterios
#Abrimos el la ventana para configurar al jugador

def start():

    window = loop()
    window.close()

def loop():
    #ca, cb = get_nom_criterios.start()
    window = a_b.build("Set criterio 1","Set criterio 2", "Selección de Criterios")

    while True:
        event, _values = window.read()

        if event in (sg.WINDOW_CLOSED, "-exit-"):
            break

        if event == "-a-":
            #set_criterio.start(ca)
            sg.popup("Seteaste el criterio 1")
            break
        if event == "-b-":
            #set_criterio.start(cb)
            sg.popup("Seteaste el criterio 2")
            break
    return window
