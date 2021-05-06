import PySimpleGUI as sg
#Creador de ventanas
def build():
    layout = [
        [sg.Button("play",size=(50,2), key="-play-")],
        [sg.Button("settings",size=(50,2), key="-settings-")],
        [sg.Button("score",size=(50,2), key="-score-")],
        [sg.Button('Exit',size=(50,2), key="-exit-")]
    ]

    board = sg.Window("Juego de la memoria").Layout(layout)

    return board
