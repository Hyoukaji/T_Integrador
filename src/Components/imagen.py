

import PySimpleGUI as sg
from src.Windows import  imagen



def start():

    window = loop()
    window.close()


def loop():


    window = imagen.build()


    while True:

        event,_value = window.read()



        if event in (sg.WINDOW_CLOSED, "-exit-"):
            break



    return window
