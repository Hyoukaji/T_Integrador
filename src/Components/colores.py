import PySimpleGUI as sg
from src.Windows import a_b
from src.Handlers import set_color

def start():

    window = loop()
    window.close()

def loop():
    window = a_b.build("Set color 1", "Set color 2","Selección de color")

    while True:
        event, _values = window.read()

        if event in (sg.WINDOW_CLOSED, "-exit-"):
            break

        if event == "-a-":
            color = "DarkPurple2"
            set_color.start(color)
            break
        if event == "-b-":
            color = "DarkBrown4"
            set_color.start(color)
            break

    return window
