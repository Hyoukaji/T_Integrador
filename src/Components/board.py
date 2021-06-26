import PySimpleGUI as sg
import time
from src.Windows import board
from src.Components import salir_partida
from src.Components import selec_nivel
from src.Handlers import crear_board_data
from src.Handlers import get_jugador_actual
from src.Handlers import get_nick_actual
#from src.Handlers import set_puntajes
#from src.Handlers import set_evento
#from src.Handlers import set_n_partida

#Abrimos el tablero del juego

def start():
    #n_partida = set_n_partida()
    window, okk = loop()
    window.close()
    if not okk:
        #set_puntajes.start(get_nick_actual,n,puntos)
        sg.popup("Se te acabo el tiempo D:")
        hora = time.strftime("%H:%M:%S")
        #set_evento(hora,n_partida,"fin","timeout","",L)
def loop():
    puntos = 0
    k = False
    nick = get_nick_actual.start()
    n = selec_nivel.start()
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
    hora = time.strftime("%H:%M:%S")
    #set_evento(hora,n_partida,"inicio_partida","","",L)
    start_time = time.time()
    window = board.build(nick,n,m)
    while True:

        event, _values = window.read(timeout=1000)
        if Tout == 180:
            break
        if event in (sg.WINDOW_CLOSED, "-exit-"):
            #oks = salir_partida()
            #if oks
                #hora = time.strftime("%H:%M:%S")
                #set_evento(hora,n_partida,"fin","sin terminar","",L)
                #break
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
                        current_time = time.time() - start_time
                        crono = (f"{round(current_time // 60):02d} : {round(current_time % 60):02d}")
                        #set_evento(crono,n_partida,"intento","match","board_data[j][k][criterio]",L)
                        ok = False
                        c = str(cont)
                        window["-elem-"].update("Elementos encontrados:" + c )
                        board_data[z][v][casilla] = True
                        board_data[j][k][casilla] = True
                        if cont == n:
                            #set_puntajes.start(get_nick_actual,n,puntos)
                            k = True
                            hora = time.strftime("%H:%M:%S")
                            #set_evento(hora,n_partida,"fin","ganador","",L)
                            break

                    else:
                        time.sleep(1)
                        ok = False
                        current_time = time.time() - start_time
                        crono = (f"{round(current_time // 60):02d} : {round(current_time % 60):02d}")
                        #set_evento(crono,n_partida,"intento","fallido","board_data[j][k][criterio]",L)
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
