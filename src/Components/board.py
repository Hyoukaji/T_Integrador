import PySimpleGUI as sg
import time
from src.Windows import board
from src.Components import salir_partida
from src.Handlers import crear_board_data
from src.Handlers import get_jugador_actual
from src.Handlers import get_nick_actual
#from src.Handlers import set_puntajes
#from src.Handlers import set_evento
#from src.Handlers import set_n_partida
from src.Handlers import set_evento
from src.Handlers import set_n_partida
from src.Handlers import registro_eventos
from src.Handlers import set_puntos

#Abrimos el tablero del juego


def start(n):
    #n_partida = set_n_partida.start()
    window, okk = loop(n)
    window.close()
    if not okk:
        #set_puntajes.start(get_nick_actual,n,puntos)
        sg.popup("Se te acabo el tiempo D:")
        hora = time.strftime("%H:%M:%S")
        #evento = set_evento.start(hora,n_partida,"fin","timeout","",L)
        #registro_eventos.start(evento)

def loop(n):
    puntos = 0
    k = False
    nick = get_nick_actual.start()
    board_data = crear_board_data.start(n)
    m = 2
    L = 1
    if n == 4:
        L = 2
    if n == 6:
        m = 3
        L = 3
    ok = False
    cont = 0

    #n_partida = set_n_partida.start()
    mask = 2
    criterio = 1
    casilla = 0
    Tout = 0
    window = board.build(nick,n,m)
    #n_partida = set_n_partida.start()
    hora = time.strftime("%H:%M:%S")
    #evento = set_evento.start(hora,n_partida,"inicio_partida","","",L)
    #registro_eventos.start(evento)
    start_time = time.time()
    window = board.build(nick,n,m)
    while True:
        mask = 2
        criterio = 1
        casilla = 0

        event, _values = window.read(timeout=1000)
        if Tout == 180:
            break
        if event in (sg.WINDOW_CLOSED, "-exit-"):
            oks = salir_partida()
            if oks:
                hora = time.strftime("%H:%M:%S")
                #n_partida = set_n_partida.start()
                #evento = set_evento(hora,n_partida,"fin","sin terminar","",L)
                #registro_eventos.start(evento)
                break
            break


        if event.startswith("cell"):
            _perfix, x, y = event.split("-")
            print (f"celda: {x},{y}")
            z = int(x)
            v = int(y)
            if  board_data[z][v][mask] == "x":
                board_data[z][v][mask] = board_data[z][v][criterio]
                window[f"cell-{x}-{y}"].update(board_data[z][v][criterio])
                window[f"cell-{x}-{y}"].update(disabled=True)

                if ok:
                    if board_data[z][v][criterio] == board_data[j][k][criterio]:
                        puntos += 1
                        cont += 1
                        #set_puntajes.start(get_nick_actual,n,puntos)
                        current_time = time.time() - start_time
                        crono = (f"{round(current_time // 60):02d} : {round(current_time % 60):02d}")
                        hora = time.strftime("%H:%M:%S")
                        #n_partida = set_n_partida.start()
                        #evento = set_evento.start(hora,n_partida,"intento","match",board_data[j][k][criterio],L)
                        #registro_eventos.start(evento)
                        ok = False
                        c = str(cont)
                        window["-elem-"].update("Elementos encontrados:" + c )
                        board_data[z][v][casilla] = True
                        board_data[j][k][casilla] = True
                        if cont == n:
                            #set_puntajes.start(get_nick_actual,n,puntos)
                            k = True
                            hora = time.strftime("%H:%M:%S")
                            #n_partida = set_n_partida.start()
                            #evento = set_evento.start(hora,n_partida,"fin","finalizada","",L)
                            #registro_eventos.start(evento)
                            break

                    else:
                        _event,_value = window.read(timeout = 10)
                        time.sleep(2)
                        ok = False
                        current_time = time.time() - start_time
                        crono = (f"{round(current_time // 60):02d} : {round(current_time % 60):02d}")
                        #n_partida = set_n_partida.start()
                        hora = time.strftime("%H:%M:%S")
                        #evento = set_evento.start(hora,n_partida,"intento","fallido",board_data[j][k][criterio],L)
                        #registro_eventos.start(evento)
                        window[f"cell-{x}-{y}"].update(disabled=False)
                        window[f"cell-{g}-{i}"].update(disabled=False)
                        board_data[z][v][mask] = "x"
                        board_data[j][k][mask] = "x"
                        window[f"cell-{x}-{y}"].update(board_data[z][v][mask])
                        window[f"cell-{g}-{i}"].update(board_data[j][k][mask])
                else:
                    ok = True
                    j = z
                    k = v
                    g = str(j)
                    i = str(k)

        Tout += 1
    return window, k
