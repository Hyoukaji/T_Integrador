import PySimpleGUI as sg
from src.Windows import login
#Abrimos la ventana para logearse

def start():

    window = loop()
    window.close()

def loop():

    window = login.build()

    while True:
        event, values = window.read()

        if event in (sg.WINDOW_CLOSED, "-exit-"):
            break

        if event == "-search-":
            text_input = values[0]
            sg.popup('You entered', text_input)

    return window
