import PySimpleGUI as sg
from src.Windows import introduzca_texto
from src.Components import edad
from src.Components import genero
from src.Handlers import buscar_jugador
from src.Handlers import crear_jugador
from src.Handlers import set_jugador_actual
from src.Handlers import get_jugador

#Abrimos la ventana para registrarse

def start(oks):

    window, ok= loop(oks)
    window.close()
    return ok
def loop(oks):
    ok = oks
    verifica = True
    encuentra = True
    t = "Register"
    tx = "Introduzca un nick que no se haya registrado"
    b = "Buscar"
    window = introduzca_texto.build(tx, b, t)

    while True:
        event, values = window.read()

        if event in (sg.WINDOW_CLOSED, "-exit-"):
            break

        if event == "-update-":
            nick = values[0]
            encuentra, verifica= buscar_jugador.start(nick)
            if (not encuentra)&(verifica):
                crear_jugador.start(nick)
                set_jugador_actual.start(get_jugador.start(nick))
                sg.popup("Para continuar te sugerimos que configures tu usuario, de lo contrario quedará todo en default")
                ok = True
                break
            else:
                if not verifica:
                    crear_jugador.start(nick)
                    #sg.popup("El archivo que guarda los jugadores no existe")
                else:
                    sg.popup("No se encuetra disponible ese nick, introduce otro")

    return window, ok
