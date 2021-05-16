import PySimpleGUI as sg
from src.Windows import board
from src.Handlers import board_data
from src.Handlers import dame_numeros
#from src.Archivos import claseJugador
#from src.Handlers import get_jugador_actual

#Abrimos el tablero del juego

def start():
    #Aca se ejecuta la ventana del tablero
    window = loop()
    window.close()
    #Loop para captar eventos del tablero
def loop():
    #Aca bolcamos la info del jugador
    jugador = get_jugador_actual.start()
    cant_casillas = jugador.tamanio
    cant_match = jugador.cantidadCoin
    equipos, tam_resto = dame_numeros.start(cant_casillas, cant_match)
    board_data = boardData.start("tipo:palabras/img", "info", equipos, cant_casillas, cant_match)

    window = board.build("jugador 1", board_data)

    while True:
        event, _values = window.read()

        if event in (sg.WINDOW_CLOSED, "-exit-"):
            break

        if event.startswith("cell"):
            _perfix, x, y = event.split("-")
            print (f"celda: {x},{y}")

    return window
