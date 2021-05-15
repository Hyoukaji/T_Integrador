import PySimpleGUI as sg
#Creador de ventana menu
def build():
    layout = [
        [sg.Button("Play",size=(50,2), key="-play-")],
        [sg.Button("Login/Register",size=(50,2), key="-login/register-")],
        [sg.Button("Settings",size=(50,2), key="-settings-")],
        [sg.Button("Score",size=(50,2), key="-score-")],
        [sg.Button("Stats",size=(50,2), key="-stats-")],
        [sg.Button('Exit',size=(50,2), key="-exit-")]
    ]

    board = sg.Window("Juego de la memoria").Layout(layout)

    return board
