import PySimpleGUI as sg
from src.Windows import introduzca_texto
from src.Handlers import buscar_jugador
from src.Handlers import set_jugador_actual
from src.Handlers import get_jugador
from src.Archivos import claseJugador
#Abrimos la ventana para logearse

def start(oks):

    window, ok= loop(oks)
    window.close()
    return ok
def loop(oks):
    ok = oks
    encuentra = False
    verifica = True
    t = "Login"
    tx = "Introduzca un nick existente"
    b = "Buscar"
    window = introduzca_texto.build(tx, b, t)

    while True:
        event, values = window.read()

        if event in (sg.WINDOW_CLOSED, "-exit-"):
            break

        if event == "-update-":
            nick = values[0]
            encuentra, verifica= buscar_jugador.start(nick)
            if encuentra:
                jugador = get_jugador.start(nick)
                set_jugador_actual.start(jugador)
                sg.popup('Bienvenido:', nick)
                ok = True
                break
            else:
                if not verifica:
                    sg.popup("El archivo que guarda los jugadores no existe")
                else:
                    sg.popup("No se pudo encontrar ese nick")

    return window, ok
