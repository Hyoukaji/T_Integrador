from src.Handlers import get_jugador_actual
<<<<<<< HEAD
from src.Archivos import claseJugador

=======
>>>>>>> 66ac02e11473b9389d1bfdc3ca3d4c68810b61cf

def start():
    jugador = get_jugador_actual.start()
    if jugador["color"] != "ninguno":
        sg.theme(jugador["color"])
