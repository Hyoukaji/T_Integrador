import PySimpleGUI as sg
#Creador de ventana para configurar
def build():
    layout = [
        [sg.Button("Ayudas",size=(50,2), key="-ayudas-")],
        [sg.Button("Tiempo Limite",size=(50,2), key="-timing-")],
        [sg.Button("Casillas x nivel",size=(50,2), key="-casillas-")],
        [sg.Button("Coincidencias",size=(50,2), key="-matchs-")],
        [sg.Button("Texto in game",size=(50,2), key="-text-")],
        [sg.Button("Color",size=(50,2), key="-color-")],
        [sg.Button('Exit',size=(50,2), key="-exit-")]
    ]

    board = sg.Window("Settings").Layout(layout)

    return board
