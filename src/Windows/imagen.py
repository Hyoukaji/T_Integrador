import PySimpleGUI as sg
import os
import os.path

nom_arch = "prueba.png"
ruta_archivo = os.path.join("src/Archivos/", nom_arch)

def build():
    #button_color=(sg.theme_background_color(),sg.theme_background_color()),border_width=0,

    layout = [
        [sg.Button("",image_filename = ruta_archivo,disabled=True
             key='Exit')]
    ]



    board = sg.Window("Prueba imagen").Layout(layout)

    return board
