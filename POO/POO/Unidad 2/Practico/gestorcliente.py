from classcliente import Cliente
import csv
class Gestorcliente:
    __listaC=list

    def __init__(self):
        self.__listaC=[]
    
    def agregar(self, nuevo):
        self.__listaC.append(nuevo)
    
    def leerdatos(self):
        archivo=open('C:/Users/Arias/Desktop/POO/Unidad 2/Practico\\ClientesFarmaCiudad.csv')
        reader=csv.reader(archivo,delimiter=';')
        band=True
        for fila in reader:
            if band==True:
                band=False
            else:
                nom=fila[0]
                ap=fila[1]
                dni=fila[2]
                num=fila[3]
                saldo=float(fila[4])
                nuevocliente=Cliente(nom,ap,dni,num,saldo)
                self.agregar(nuevocliente)
        archivo.close()
    
    def buscarsaldo(self,dni):
        i=0
        band=True
        while i<len(self.__listaC) and band==True:
            if self.__listaC[i].getdni() == dni:
                nom=self.__listaC[i].getnom()
                ap=self.__listaC[i].getap()
                num=self.__listaC[i].getnum()
                saldoant=self.__listaC[i].getsaldo()
                band=False
            else:
                i+=1
        return nom,ap,num,saldoant
    
    def buscarnum(self, dni):
        i=0
        band=True
        while i<len(self.__listaC) and band==True:
            if dni == self.__listaC[i].getdni():
                num=self.__listaC[i].getnum()
                nom=self.__listaC[i].getnom()
                ap=self.__listaC[i].getap()                
                band=False
            else:
                i+=1
        return num,ap,nom