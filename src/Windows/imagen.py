import PySimpleGUI as sg
import os
import os.path


<<<<<<< HEAD

def build(nom):
    #button_color=(sg.theme_background_color(),sg.theme_background_color()),border_width=0,
=======
def build():
    #button_color = (sg.theme_background_color(), sg.theme_background_color()), border_width=0,
>>>>>>> refs/remotes/origin/main

    nom_arch = nom
    ruta_archivo = os.path.join("src/Archivos/", nom_arch)

    layout = [
<<<<<<< HEAD
        [sg.Button("",image_filename = ruta_archivo,disabled=True,
             key='Exit')]
=======
        [sg.Button("", image_filename = ruta_archivo, disabled=True, key='Exit')]
>>>>>>> refs/remotes/origin/main
    ]

    board = sg.Window("Prueba imagen").Layout(layout)

    return board
