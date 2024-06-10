import datetime
import csv
from classfecha import fecha
class gestorF:
    __listafecha:list

    def __init__(self):
        self.__listafecha=[]

    def agregar(self, nuevafe):
        self.__listafecha.append(nuevafe)

    def getlista(self):
        return self.__listafecha

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

    def buscarfecha(self, id):
        i=0
        while i<len(self.__listafecha[i]):
            if self.__listafecha[i].getidl() == id:
                xfe=self.__listafecha[i].getfecha()
                golesaf=self.__listafecha[i].getgoll()
                golescon=self.__listafecha[i].getgolv()
                puntos=self.getpuntos(golesaf,golescon)
            elif self.__listafecha[i].getidv()==id:
                xfe=self.__listafecha[i].getfecha()
                golesaf=self.__listafecha[i].getgolv()
                golescon=self.__listafecha[i].getgoll()
                puntos=self.getpuntos(golesaf,golescon)
            else:
                i+1
        return xfe, golesaf, golescon, puntos
    
    def getpuntos(self, afavor, contra):
        puntos=1
        if afavor > contra:
            puntos=3
        elif contra > afavor:
            puntos=0
        return puntos