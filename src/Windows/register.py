import PySimpleGUI as sg
#Creador de ventana register
def build():
    layout = [[sg.Text('Introduzca un nick para crear un nuevo jugador')],
                 [sg.InputText()],
                 [sg.Button('Buscar',size=(50,2), key="-search-")],
                 [sg.Text("")],
                 [sg.Button('Exit',size=(50,2), key="-exit-")]
    ]

    board = sg.Window("Register").Layout(layout)

    return board
