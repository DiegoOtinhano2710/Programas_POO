import datetime
import csv
from classfecha import fecha
class gestorF:
    __listafecha:list

    def __init__(self):
        self.__listafecha=[]

    def agregar(self, nuevafe):
        self.__listafecha.append(nuevafe)

    def leerdatos(self):
        archivo=open('fechasFutbol2024.csv')
        reader=csv.reader(archivo, delimiter=';')
        for fila in reader:
            xfecha=datetime(fila[0])
            idl=int(fila[1])
            idv=int(fila[2])
            goll=int(fila[3])
            golv=int(fila[4])
            nuevo=fecha(xfecha,idl,idv,goll,golv)
            self.agregar(nuevo)

    
 