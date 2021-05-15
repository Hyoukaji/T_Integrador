import PySimpleGUI as sg
from src.Components import loginRegister
from src.Components import settings
from src.Components import ir_a_settings
#Un primer inicio de sesion antes de ir al menu principal
def start():
    loginRegister.start()
    ok = ir_a_settings.start()
    if ok:
        settings.start()
