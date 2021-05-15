import PySimpleGUI as sg
from src.Windows import introduzca_texto
from src.Components import edad
from src.Components import genero
#Abrimos la ventana para registrarse

def start():

    window = loop()
    window.close()

def loop():
    ok = False
    t = "Register"
    tx = "Introduzca un nick que no se haya registrado"
    b = "Buscar"
    window = introduzca_texto.build(tx, b, t)

    while True:
        event, values = window.read()

        if event in (sg.WINDOW_CLOSED, "-exit-"):
            break

        if event == "-update-":
            text_input = values[0]
            sg.popup('You entered', text_input)
            ok = True
            if ok:
                edad.start()
                genero.start()
                sg.popup("Para continuar te sugerimos que configures tu usuario, de lo contrario quedara todo en default")
            break
    return window
