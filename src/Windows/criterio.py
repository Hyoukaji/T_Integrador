import PySimpleGUI as sg

def build():
    layout = [
        [sg.Button("Set criterio 1",size=(50,2), key="-criterio 1-")],
        [sg.Button("Set criterio 2",size=(50,2), key="-criterio 2-")],
        [sg.Button('Exit',size=(50,2), key="-exit-")]
    ]

    board = sg.Window("Criterios").Layout(layout)

    return board
