from datetime import datetime
class Jugador:
    __Nombre:str
    __Fecha:datetime
    __Hora:datetime
    __Puntaje:int

    def __init__(self,Jugador,Fecha,Hora,Puntaje):
        self.__Nombre=Jugador
        self.__Fecha=Fecha
        self.__Hora=Hora
        self.__Puntaje=Puntaje
    
    def __str__(self):
        return (f'{self.__Nombre:<14}'
                f'{self.__Fecha:<14} '
                f'{self.__Hora:<12}'
                f'{self.__Puntaje:>5}')
    
    def getnombre(self):
        return self.__Nombre
    def getfecha(self):
        return self.__Fecha
    def gethora(self):
        return self.__Hora
    def getpuntaje(self):
        return self.__Puntaje
    def __gt__(self, other):
        return self.__Puntaje > other.__Puntaje