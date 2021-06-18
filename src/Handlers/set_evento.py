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
        nivel = unNivel
        cant_palabras = 5
    tiempo = unTiempo
    evento = unEvento
    estado = unEstado
    palabra = unaPalabra
    partida = unaPartida    
    lista = [tiempo, partida, cant_palabras, evento, nick, genero, edad, estado, palabra, nivel]
    return lista