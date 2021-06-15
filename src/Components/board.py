import PySimpleGUI as sg
import time
from src.Windows import board
from src.Components import salir_partida
from src.Components import selec_nivel
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
    n = selec_nivel.start()
    board_data = crear_board_data.start(n)

    window = board.build(nick,n)
    ok = False
    cont = 0

    while True:
        #n_partida = set_n_partida()
        mask = 2
        criterio = 1
        casilla = 0


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
            if  board_data[z][v][mask] == "x":
                board_data[z][v][mask] = board_data[z][v][criterio]
                window[f"cell-{x}-{y}"].update(board_data[z][v][criterio])
                window[f"cell-{x}-{y}"].update(disabled=True)

                if ok:
                    print("entrando al if ok")
                    if board_data[z][v][criterio] == board_data[j][k][criterio]:
                        print("entrando a comparar casillas")
                        cont += 1
                        sg.popup("Hiciste un punto!!!")
                        ok = False
                        c = str(cont)
                        window["-elem-"].update("Elementos encontrados:" + c )
                        board_data[z][v][casilla] = True
                        board_data[j][k][casilla] = True
                        if cont == n:
                            sg.popup("GANASTEEE!!")
                            break

                    else:
                        print("no son iguales")
                        ok = False
                        sg.popup("intenta denuevo")
                        window[f"cell-{x}-{y}"].update(disabled=False)
                        window[f"cell-{g}-{i}"].update(disabled=False)
                        board_data[z][v][mask] = "x"
                        board_data[j][k][mask] = "x"
                        window[f"cell-{x}-{y}"].update(board_data[z][v][mask])
                        window[f"cell-{g}-{i}"].update(board_data[j][k][mask])
                else:
                    print("no habia una casilla previamente selecc")
                    ok = True
                    j = z
                    k = v
                    g = str(j)
                    i = str(k)


    return window
