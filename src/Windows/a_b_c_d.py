import PySimpleGUI as sg

#Ventana comun para elegir entre una opcion a,b,c,d

def build(a,b,c,d,t):
    layout = [
        [sg.Button(a,size=(50,2), key="-a-")],
        [sg.Button(b,size=(50,2), key="-b-")],
        [sg.Button(c,size=(50,2), key="-c-")],
        [sg.Button(d,size=(50,2), key="-d-")],
        [sg.Button('Exit',size=(50,2), key="-exit-")]
    ]

    board = sg.Window(t).Layout(layout)

    return board
