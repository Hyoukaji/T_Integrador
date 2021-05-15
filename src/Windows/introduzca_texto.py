import PySimpleGUI as sg
#Creador de ventana register
def build(texto, titulo):
    layout = [[sg.Text(texto)],
                 [sg.InputText()],
                 [sg.Button('Actualizar',size=(50,2), key="-update-")],
                 [sg.Text("")],
                 [sg.Button('Exit',size=(50,2), key="-exit-")]
    ]

    board = sg.Window(titulo).Layout(layout)

    return board
