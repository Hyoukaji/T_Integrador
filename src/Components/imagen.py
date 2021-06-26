

import PySimpleGUI as sg
from src.Windows import  imagen





def start(n):

    window = loop()
    window.close()


def loop():


    window = imagen.build(n)


    while True:

        event,_value = window.read()



        if event in (sg.WINDOW_CLOSED, "-exit-"):
            break



    return window
