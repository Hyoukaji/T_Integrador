import PySimpleGUI as sg
#Creador de ventana login
def build():
    layout = [[sg.Text('Introduzca un nick existente')],
                 [sg.InputText()],
                 [sg.Button('Buscar',size=(50,2), key="-search-")],
                 [sg.Text("")],
                 [sg.Button('Exit',size=(50,2), key="-exit-")]
    ]

    board = sg.Window("Login").Layout(layout)

    return board
