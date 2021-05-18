import PySimpleGUI as sg
from src.Handlers import get_criterios



def start():
    titulo, criterio_actual = get_criterios.start()
    titulo_criterio = "Titulo del criterio"

    sg.popup("El criterio usado para esta partida es:", titulo_criterio)
    sg.popup(criterio_actual)
