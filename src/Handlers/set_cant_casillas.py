import json
import os
import os.path
from src.Handlers import get_nick_actual
nom_arch_2= "jugador_actual.json"
ruta_archivo_2 = os.path.join("src/Archivos/", nom_arch_2)

def start(valor1=2,valor2=4,valor3=6):
    try:
        dato_jugador_actual = {}
        unNick=get_nick_actual.start()
        with open(ruta_archivo_2, "r") as archivo_2:
            dato_jugador_actual = json.load(archivo_2)
            dato_jugador_actual[unNick]["cant_casillas"][0]=valor1
            dato_jugador_actual[unNick]["cant_casillas"][1]=valor2
            dato_jugador_actual[unNick]["cant_casillas"][2]=valor3
            with open(ruta_archivo_2, "w") as file:
                json.dump(dato_jugador_actual, file, indent=4)
    except FileNotFoundError:
        print("Archivo de jugadores no encontrado")
