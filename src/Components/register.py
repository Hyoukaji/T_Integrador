import PySimpleGUI as sg
from src.Windows import introduzca_texto
from src.Components import edad
from src.Components import genero
from src.Handlers import buscar_jugador
from src.Handlers import crear_jugador
from src.Handlers import set_jugador_actual
from src.Handlers import get_jugador
from src.Archivos import claseJugador
from src.Components import ir_crear_archivo
from src.Handlers import crear_archivo

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
                sg.popup("A continuacion introduzca su edad y genero para terminar de crear el usuario")
                e = edad.start()
                g = genero.start()
                crear_jugador.start(nick, e, g)
                set_jugador_actual.start(get_jugador.start(nick))
                sg.popup("Para continuar te recomendamos que configures tu usuario de lo contrario quedará todo en default")
                break
            else:
                if not verifica:
                    sg.popup("El archivo que guarda los jugadores no existe")
                    k = ir_crear_archivo.start()
                    if k:
                        crear_archivo.start()
                else:
                    sg.popup("No se encuetra disponible ese nick, introduce otro")

    return window, ok
