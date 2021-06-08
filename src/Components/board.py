import PySimpleGUI as sg
import time
from src.Windows import board
from src.Components import salir_partida
from src.Handlers import crear_board_data
from src.Handlers import get_jugador_actual
from src.Handlers import get_nick_actual
#from src.Handlers import set_evento
#from src.Handlers import set_n_partida

#Abrimos el tablero del juego

def start():
    #n_partida = set_n_partida()
    hora = time.strftime("%H:%M:%S")
    #set_evento(hora,n_partida,"inicio_partida","","",1)
    window = loop()
    window.close()
def loop():
    nick = get_nick_actual.start()
    jugador = get_jugador_actual.start()
    #t_limite = jugador[nick]["tiempo"]
    nick = get_nick_actual.start()
    #board_data = crear_board_data.start()

    window = board.build(nick)

    while True:
        #n_partida = set_n_partida()

        event, _values = window.read()

        if event in (sg.WINDOW_CLOSED, "-exit-"):
            #oks = salir_partida()
            #if oks
                #hora = time.strftime("%H:%M:%S")
                #set_evento(hora,n_partida,"fin","sin terminar","",1)
                #break
            break

        if event.startswith("cell"):
            _perfix, x, y = event.split("-")
            print (f"celda: {x},{y}")
            z = int(x)
            v = int(y)

    return window
