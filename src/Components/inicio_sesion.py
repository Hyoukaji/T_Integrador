import PySimpleGUI as sg
from src.Components import login_register
from src.Components import settings
from src.Components import ir_a_settings
from src.Handlers import colorear

#Un primer inicio de sesion antes de ir al menu principal

def start(oks):
    ok = login_register.start(oks)
    if ok:
        colorear.start()
        okp = ir_a_settings.start()
        if okp:
            settings.start()
    return ok
