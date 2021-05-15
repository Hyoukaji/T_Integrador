import PySimpleGUI as sg
#Creador de ventana register
def build(texto, titulo, boton):
    layout = [[sg.Text(texto)],
                 [sg.InputText()],
                 [sg.Button(boton,size=(50,2), key="-update-")],
                 [sg.Text("")],
                 [sg.Button('Exit',size=(50,2), key="-exit-")]
    ]

    board = sg.Window(titulo).Layout(layout)

    return board
