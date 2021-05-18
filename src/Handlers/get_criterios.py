from src.Handlers import criterios
from datetime import date
from datetime import datetime
import calendar

def get_criterios():
    dia = date.today()
    hora = datetime.now().hour
    if calendar.day_name[dia.weekday()] == "Monday":
        if hora >= 12 and hora <= 0:
            return criterios.start_1()
        else
            return criterios.start_8()
    elif calendar.day_name[dia.weekday()] == "Tuesday":
        if hora >= 12 and hora <= 0:
            return criterios.start_2()
        else
            return criterios.start_7()
    elif calendar.day_name[dia.weekday()] == "Wednesday":
        if hora >= 12 and hora <= 0:
            return criterios.start_3()
        else
            return criterios.start_6()
    elif calendar.day_name[dia.weekday()] == "Thursday":
        if hora >= 12 and hora <= 0:
            return criterios.start_1()
        else
            return criterios.start_5()
    elif calendar.day_name[dia.weekday()] == "Friday":
        if hora >= 12 and hora <= 0:
            return criterios.start_7()
        else
            return criterios.start_4()
    elif calendar.day_name[dia.weekday()] == "Saturday":
        if hora >= 12 and hora <= 0:
            return criterios.start_6()
        else
            return criterios.start_8()
    else:
        if hora >= 12 and hora <= 0:
            return criterios.start_5()
        else
            return criterios.start_8()


