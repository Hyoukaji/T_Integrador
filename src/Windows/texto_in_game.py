import PySimpleGUI as sg


def build():
    layout = [
        [sg.Button("Texto al ganar",size=(50,2), key="-ganar-")],
        [sg.Button("Texto al perder",size=(50,2), key="-perder-")],
        [sg.Button("Texto de poco tiempo",size=(50,2), key="-pocoT-")],
        [sg.Button('Exit',size=(50,2), key="-exit-")]
    ]

    board = sg.Window("Texto in game").Layout(layout)

    return board
