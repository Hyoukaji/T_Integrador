import PySimpleGUI as sg

def build():
    layout = [
        [sg.Button("Con ayudas",size=(50,2), key="-a-")],
        [sg.Button("Sin ayudas",size=(50,2), key="-b-")],
        [sg.Button('Exit',size=(50,2), key="-exit-")]
    ]

    board = sg.Window("Ayudas").Layout(layout)

    return board
