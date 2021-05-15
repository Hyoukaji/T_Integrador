import PySimpleGUI as sg

def build(a,b,t):
    layout = [
        [sg.Button(a,size=(50,2), key="-a-")],
        [sg.Button(b,size=(50,2), key="-b-")],
        [sg.Button('Exit',size=(50,2), key="-exit-")]
    ]

    board = sg.Window(t).Layout(layout)

    return board
