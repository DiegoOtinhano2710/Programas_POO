from classjugador import Jugador
import json
from datetime import datetime
class gestor_jugadores:
    __lista_jugadores:list
    def __init__(self):
        self.__lista_jugadores=[]
    
    def getlista(self):
        return self.__lista_jugadores
    
    def agregar_jugador(self, nuevo_jugador):
        self.__lista_jugadores.append(nuevo_jugador)
        
    def ordenar_puntaje(self):
        with open('psymonpuntajes.json', 'r',encoding='utf-8') as archivo:          #al usar 'with' el archivo se cierra al terminar el bloque
            datos_jugadores=json.load(archivo)
            for dato in datos_jugadores:
                un_jugador=Jugador(dato['Jugador'], dato['Fecha'], dato['Hora'], dato['Puntaje'])
                self.agregar_jugador(un_jugador)
            self.ordenar()

    def ordenar(self):
        self.__lista_jugadores.sort(reverse=True)
    