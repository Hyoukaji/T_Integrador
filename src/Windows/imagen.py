import PySimpleGUI as sg
import os
import os.path


def build(nom):

    nom_arch = nom
    ruta_archivo = os.path.join("src/Archivos/", nom_arch)

    layout = [
        [sg.Button("",image_filename = ruta_archivo,disabled=True,
             key='Exit')]
    ]

    board = sg.Window("Graphic").Layout(layout)

    return board
