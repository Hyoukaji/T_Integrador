from json import JSONEncoder
from datetime import datetime

class Jugador():
    "Define las variables y metodos que instancian a un jugador de Mempy"
    #incluir manejaro para el caso que no se ingresen los datos correctamente
       
    def __init__(self, unNick = "No definido", unGenero = "No indicado", unaEdad = 0):
        self._nick = unNick
        self._genero = unGenero
        self._edad = unaEdad
        self._puntos = 0
        self.tiempo = 180 
        self.tamanio = 4
        self.cantidadCoin = 2
        self.elemento_casilla = 0 #niIdeaQueEsEsto
        self.ayuda = False
        self.color = "ninguno"
        self.text_ganar = "Ganaste"
        self.text_perder ="Perdiste"
        self.text_pocoT = "Te queda poco tiempo D:"
        
    def set_nick(self, unNick):
        self._nick += unNick
        
    def get_nick(self):
        return self._nick
        
    def set_genero(self, unGenero):
        self._genero += unGenero
        
    def get_genero(self):
        return self._genero
        
    def set_edad(self, unaEdad):
        self._edad += unaEdad
        
    def get_edad(self):
        return self._edad
        
    def set_puntos(self, unPunto):
        self._puntos += unPunto
    
    def get_puntos(self):
        return self._puntos
    
    def __str__(self):
        print(f" {self._nick} tiene {self._puntos(self)} puntos")
        
# subclase JSONEncoder
class JugadorEncoder(JSONEncoder):
    """ Metodo para implementar una serialización JSON personalizada"""
    
    def default(self, o):
        return o.__dict__




