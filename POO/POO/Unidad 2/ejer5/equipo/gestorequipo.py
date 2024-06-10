import csv
from classequipo import equipo
class gestorE:
    __listaequipo:list

    def __init__(self):
        self.__listaequipo=[]

    def agregar(self, nuevoequi):
        self.__listaequipo.append(nuevoequi)

    def leerdatos(self):
        archivo=open('equipos2024.csv')
        reader=csv.reader(archivo, delimiter=';')
        bandera= True
        for fila in reader:
            if bandera:
                 bandera= False
            else:
                id=int(fila[0])
                nom=fila[1]
                gola=int(fila[2])
                golc=int(fila[3])
                dif=int(fila[4])
                puntos=int(fila[5])
                nuevo=equipo(id,nom,gola,golc,dif,puntos)
                self.agregar(nuevo)
    
    def buscarid(self, xnom):
        i=0
        while i<len(self.__listaequipo) and xnom == self.__listaequipo[i].getid():
                i+1
        if xnom == self.__listaequipo[i].getid():
             id=self.__listaequipo[i].getid()
        return id