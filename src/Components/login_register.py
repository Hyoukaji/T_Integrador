import PySimpleGUI as sg
from src.Windows import login_register
from src.Components import login
from src.Components import register
#from src.Handlers import actualizar_jugador
#Abrimos la ventana para logearse o regristrarse

def start(oks):
    #if oks:
        #actualizar_jugador.start()
    window, ok= loop(oks)
    window.close()
    return ok
def loop(oks):
    ok = oks

    window = login_register.build()

    while True:
        event, _values = window.read()

        if event in (sg.WINDOW_CLOSED, "-exit-"):
            if not ok:
                sg.popup("ATENCION: No se logueo ni registró y consecuentemente no podrá jugar")
            break

        if event == "-login-":
            window.hide()
            ok = login.start(ok)
            window.un_hide()
            break
        if event == "-register-":
            window.hide()
            ok = register.start(ok)
            window.un_hide()
            break

    return window, ok
