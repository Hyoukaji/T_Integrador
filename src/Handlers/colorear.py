from src.Handlers import get_jugador_actual
from src.Archivos import claseJugador


def start():
    jugador = get_jugador_actual.start()
    if jugador["color"] != "ninguno":
        sg.theme(jugador["color"])
