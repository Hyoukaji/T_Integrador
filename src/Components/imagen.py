import PySimpleGUI as sg
from src.Windows import  imagen


def start(n):
    window = loop(n)
    window.close()


def loop(n):


    window = imagen.build(n)


    while True:

        event,_value = window.read()



        if event in (sg.WINDOW_CLOSED, "-exit-"):
            break



    return window
