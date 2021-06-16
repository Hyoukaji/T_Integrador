import PySimpleGUI as sg
#Creador de tableros

def build(player1_name,n,m):
    N = str(n)
    if n == 6:
        n = 4
    layout = [
        [sg.Text("Jugador1: " + player1_name, key="-P1-", text_color="Red")],
        [sg.Text("Elementos encontrados: 0", key="-elem-", text_color="Black")],
        [sg.Text("Total: " + N, key="-total-", text_color="White")],
        [sg.Text("")]
    ]
    #Aca las celdas para hacer las coincidencias
    for y in range(n):
        layout += [
            [sg.Button("x", size=(8, 4), key=f"cell-{x}-{y}") for x in range(m)]
        ]

    board = sg.Window("Tablero del juego").Layout(layout)

    return board
