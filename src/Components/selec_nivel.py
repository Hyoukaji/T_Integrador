import PySimpleGUI as sg
from src.Windows import a_b_c

def start():
    window, n= loop()
    window.close()
    return n
def loop():
    n = 3
    window = a_b_c.build("Nivel 1","Nivel 2","Nivel 3","¿Que nivel quieres jugar?")

    while True:
        event, _values = window.read()

        if event in (sg.WINDOW_CLOSED, "-exit-"):
            break

        if event == "-a-":
            n = 3
            break
        if event == "-b-":
            n = 4
            break
        if event == "-c-":
            n = 5
            break

    return window, n
