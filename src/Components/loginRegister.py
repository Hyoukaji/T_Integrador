import PySimpleGUI as sg
from src.Windows import loginRegister
from src.Components import login
from src.Components import register
#Abrimos la ventana para logearse o regristrarse

def start():

    window = loop()
    window.close()

def loop():

    window = loginRegister.build()

    while True:
        event, _values = window.read()

        if event in (sg.WINDOW_CLOSED, "-exit-"):
            break

        if event == "-login-":
            window.hide()
            login.start()
            window.un_hide()
            break
        if event == "-register-":
            window.hide()
            register.start()
            window.un_hide()
            break

    return window
