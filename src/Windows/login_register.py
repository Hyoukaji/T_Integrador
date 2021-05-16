import PySimpleGUI as sg
#Creador de ventana login/register
def build():
    layout = [
        [sg.Button("Login",size=(50,2), key="-login-")],[sg.Button("Register",size=(50,2), key="-register-")],
        [sg.Text("")],
        [sg.Button('Exit',size=(50,2), key="-exit-")]

    ]

    board = sg.Window("Login/Register").Layout(layout)

    return board
