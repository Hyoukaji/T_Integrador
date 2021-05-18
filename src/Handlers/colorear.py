from src.Handlers import get_jugador_actual
from src.Handlers import get_nick_actual
import PySimpleGUI as sg

def start():
    jugador = {}
    jugador = get_jugador_actual.start()
    unNick = get_nick_actual.start()
    if jugador[unNick]["color"] != "ninguno":
        sg.theme(jugador["color"])
