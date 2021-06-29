import PySimpleGUI as sg
from src.Windows import a_b_c

def start():
    window, n, play= loop()
    window.close()
    return n, play
def loop():
    n = 3
    ok = False
    window = a_b_c.build("Nivel 1","Nivel 2","Nivel 3","¿Que nivel quieres jugar?")

    while True:
        event, _values = window.read()

        if event in (sg.WINDOW_CLOSED, "-exit-"):
            break

        if event == "-a-":
            n = 3
            ok = True
            break
        if event == "-b-":
            n = 4
            ok = True
            break
        if event == "-c-":
            n = 6
            ok = True
            break

    return window, n, ok
