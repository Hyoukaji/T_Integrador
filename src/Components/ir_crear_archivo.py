import PySimpleGUI as sg
from src.Windows import a_b
#Abrimos el la ventana para configurar al jugador

def start():
    window, ok= loop()
    window.close()
    return ok
def loop():
    ok = False

    window = a_b.build("Si","No","¿Quieres crear un archivo?")

    while True:
        event, _values = window.read()

        if event in (sg.WINDOW_CLOSED, "-exit-"):
            break

        if event == "-a-":
            ok = True
            break
        if event == "-b-":
            break

    return window, ok
