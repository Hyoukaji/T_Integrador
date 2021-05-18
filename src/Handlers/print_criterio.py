import PySimpleGUI as sg
from src.Handlers import get_criterio



def start():
    criterio_actual = get_criterio.start()
    titulo_criterio = "Titulo del criterio"
    print(criterio_actual.split("-"))
    sg.popup("El criterio usado para esta partida es:" + titulo_criterio)
