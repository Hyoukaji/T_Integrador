import PySimpleGUI as sg
from src.Windows import menu
from src.Components import board
#Menu de components
def start():
    #Aca se ejecuta la ventana del menu
    window = loop()
    window.close()

def loop():
    #Loop para captar eventos
    window = menu.build()

    while True:
        event, values = window.read()

        if event in (sg.WINDOW_CLOSED, "Exit", "-exit-"):
            break
        print (event)
        print (values)
        if event == "-play-":
            window.hide()
            board.start()
            window.un_hide()
        #if event == "-login/register-":
            #window.hide()
            #window.un_hide()
        #if event == "-settings-":
            #window.hide()
            #window.un_hide()
        #if event == "-score-":
            #window.hide()
            #window.un_hide()
        #if event == "-stats-":
            #window.hide()
            #window.un_hide()
    return window
