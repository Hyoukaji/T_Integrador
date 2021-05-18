from src.Handlers import get_criterio


def start():
    criterio_actual = get_criterio.start()
    print(criterio_actual.split("-"))
