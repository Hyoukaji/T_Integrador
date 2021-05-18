import PySimpleGUI as sg
from src.Windows import introduzca_texto
from src.Handlers import set_cant_casillas

def start():

    window = loop()
    window.close()

def loop():
    t = "Cantidad de casillas"
    tx = "Introduzca 3 números para elevarlos al cuadrado y crear los tableros"
    b = "Actualizar"
    window = introduzca_texto.build(tx, b, t)

    while True:
        event, values = window.read()

        if event in (sg.WINDOW_CLOSED, "-exit-"):
            break

        if event == "-update-":
            text_input = values[0]
            try:
                x = int(text_input)
                sg.popup("Seteaste la cantidad de casillas del nivel 1 en:", x*x)
                if event == "-update-":
                    text_input = values[0]
                    try:
                        y = int(text_input)
                        sg.popup("Seteaste la cantidad de casillas del nivel 2 en:", y*y)
                        if event == "-update-":
                            text_input = values[0]
                            try:
                                z = int(text_input)
                                sg.popup("Seteaste la cantidad de casillas del nivel 3 en:", z*z)
                                set_cant_casillas.start(x, y, z)
                                break
                            except:
                                sg.popup("Tienes que ingresar un número entero, vuelve a empezar.....")
                    except:
                        sg.popup("Tienes que ingresar un número entero, vuelve a empezar...")
            except:
                sg.popup("Tienes que ingresar un número entero, vuelve a empezar")

    return window
