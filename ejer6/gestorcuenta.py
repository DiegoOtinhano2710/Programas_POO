from clasecuenta import Cuenta
import numpy as np
import csv
class Gcuenta:
    __Lcuenta:np.array

    def __init__(self):
        self.__Lcuenta=np.empty([0],dtype=Cuenta)
    
    def agregar(self,nueva):
        self.__Lcuenta=np.append(self.__Lcuenta, nueva)

    def leerdatos(self):
        archivo=open('cuentasBilletera.csv')
        reader=csv.reader(archivo, delimiter=';')
        band=True
        for fila in reader:
            if band:
                band=False
            else:
                ap=fila[0]
                nom=fila[1]
                dni=fila[2]
                tel=fila[3]
                saldo=float(fila[4])
                cvu=fila[5]
                porc=float(fila[6])
                unacuenta=Cuenta(ap,nom,dni,tel,saldo,cvu,porc)
                self.agregar(unacuenta)
        archivo.close()

    def buscar(self, xdni):
        i=0
        band=True
        while i<len(self.__Lcuenta) and band:
            if xdni == self.__Lcuenta[i].getdni():
                xap=self.__Lcuenta[i].getap()
                xnom=self.__Lcuenta[i].getnom()
                xcvu=self.__Lcuenta[i].getcvu()
                xsaldo=self.__Lcuenta[i].getsaldo()
                band=False
            else: 
                i+=1
        return xap, xnom, xcvu, xsaldo
    
    def actualizarsaldo(self,cvu,saldo):
        i=0
        band=True
        while i<len(self.__Lcuenta) and band:
            if cvu == self.__Lcuenta[i].getcvu():
                self.__Lcuenta[i].setsaldo(saldo)
                band=False
            else:
                i+=1
    
    def actporc(self, xpor):
        self.__Lcuenta[0].setporc(xpor)
    

    