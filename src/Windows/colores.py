import PySimpleGUI as sg
#Creador de ventana menu
def build():
    layout = [
        [sg.Button("Set color oscuro",size=(50,2), key="-color1-")],
        [sg.Button("Set color luminoso",size=(50,2), key="-color2-")],
        [sg.Button('Exit',size=(50,2), key="-exit-")]
    ]

    board = sg.Window("Colores").Layout(layout)

    return board
