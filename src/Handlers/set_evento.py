import json
import os
import os.path
from src.Handlers import get_nick_actual

def start(unTiempo = "", unaPartida = 0, unEvento = "", unEstado = "", unaPalabra = "", unNivel = 1):
    lista = []
    nom_arch= "jugador_actual.json"
    ruta_archivo = os.path.join("src/Archivos/", nom_arch)
    with open(ruta_archivo, "r") as file:
        jugador = json.load(file)
        nick = get_nick_actual.start()
        genero = jugador[nick]["genero"]
        edad = jugador[nick]["edad"]
        if unNivel == 1:
            nivel = 'facil'
            cant_palabras = 3
        elif unNivel == 2:
            nivel = 'medio'
            cant_palabras = 4
        else:
            nivel = 'dificil'
            cant_palabras = 6
    tiempo = unTiempo
    evento = unEvento
    estado = unEstado
    palabra = unaPalabra
    partida = unaPartida    
    lista = [tiempo, partida, cant_palabras, evento, nick, genero, edad, estado, palabra, nivel]
    return lista