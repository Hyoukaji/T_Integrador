import PySimpleGUI as sg
from src.Components import loginRegister
from src.Components import settings
#Un primer inicio de sesion antes de ir al menu principal
def start():
    loginRegister.start()
    color = settings.start()
    
