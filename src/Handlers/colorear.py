from src.Handlers import get_jugador_actual
from src.Archivo import claseJugador


def start():
    jugador = get_jugador_actual.start()
    if jugador.color != "ninguno":
        sg.theme(jugador.color)
