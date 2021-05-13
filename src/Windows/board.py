import PySimpleGUI as sg
#Creador de tableros

def build(player1_name):
    layout = [
        [sg.Text("Jugador1: " + player1_name, key="-P1-", text_color="Red")],
        [sg.Text("Elementos encontrados: " + "x", key="-elem-", text_color="Blue")],
        [sg.Text("Total: " + "x", key="-total-", text_color="White")],
        [sg.Text("")]
    ]
    #Aca las celdas para hacer las coincidencias
    for y in range(3):
        layout += [
            [sg.Button(" ", size=(8, 4), key=f"cell-{x}-{y}") for x in range(3)]
        ]

    board = sg.Window("Tablero del juego").Layout(layout)

    return board
