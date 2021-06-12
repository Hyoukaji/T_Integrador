import PySimpleGUI as sg

#Ventana comun para elegir entre una opcion a y una opcion b

def build(a,b,c,t):
    layout = [
        [sg.Button(a,size=(50,2), key="-a-")],
        [sg.Button(b,size=(50,2), key="-b-")],
        [sg.Button(c,size=(50,2), key="-c-")],
        [sg.Button('Exit',size=(50,2), key="-exit-")]
    ]

    board = sg.Window(t).Layout(layout)

    return board
