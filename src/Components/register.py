import PySimpleGUI as sg
from src.Windows import introduzca_texto
from src.Components import edad
from src.Components import genero
#from src.Handlers import buscar_jugador
#from src.Handlers import crear_jugador
#from src.Handlers import set_jugador_actual
#from src.Handlers import get_jugador
#from src.Archivos import jugador
#Abrimos la ventana para registrarse

def start(oks):

    window, ok= loop(oks)
    window.close()
    return ok
def loop(oks):
    ok = oks
    #encuentra = True
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
            #encuentra = buscar_jugador.start(text_input)
            #if not encuentra:
                e = edad.start()
                g = genero.start()
                #crear_jugador.start(e,g,text_input)
                #jugador = get_jugador.start(text_input)
                #set_jugador_actual.start(jugador)
                sg.popup("Para continuar te sugerimos que configures tu usuario, de lo contrario quedará todo en default")
                ok = True
                break
            #else:
                sg.popup("No se encuetra disponible ese nick, introduce otro")

    return window, ok
