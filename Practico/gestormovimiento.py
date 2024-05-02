from classmovimiento import Movimiento
import numpy as np
import csv
class GestorMovimiento:
    __listaM:np.array

    def __init__(self):
        self.__listaM=np.empty([0],dtype=Movimiento)

    def agregar(self, nuevo):
        self.__listaM=np.append(self.__listaM, nuevo)
    
    def leerdato(self):
        archivo=open("MovimientosAbril2024.csv")
        reader=csv.reader(archivo, delimiter=';')
        band=True
        for fila in reader:
            if band==True:
                band=False
            else:
                num=fila[0]
                fecha=fila[1]
                desc=fila[2]
                tipo=fila[3]
                imp=fila[4]
                nuevomov=Movimiento(num,fecha,desc,tipo,imp)
                self.agregar(nuevomov)
        archivo.close()
    
    def actualizarsaldo(self, saldo,num):
        i=0
        print ('''Fecha     Descrpición     importe     Tipo de movimiento''')
        while i<len(self.__listaM):
            if num==self.__listaM[i].getnum():
                tipo=self.__listaM[i].gettipo()
                fecha=self.__listaM[i].getfecha()
                desc=self.__listaM[i].getdesc()
                imp=float(self.__listaM[i].getimp())
                if tipo=='C':
                    saldo+=imp
                else:
                    saldo-=imp
                print (f'{fecha}    {desc}      {imp}       {tipo}')
            else:
                i+=1
        
    
    def buscarmov(self, num):
        i=0
        band=True
        while i<len(self.__listaM) and band:
            if num == self.__listaM[i].getnum():
                band=False
            else:
                i+=1
        return band
    
    def ordenar(self):
        self.__listaM=np.sort(self.__listaM)
    def mostrar(self):
        for i in range(len(self.__listaM)):
            print(self.__listaM[i])