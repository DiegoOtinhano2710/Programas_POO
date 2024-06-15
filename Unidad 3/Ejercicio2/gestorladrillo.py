from ClassLadrillo import ladrillo
import csv
class Gladrillo:
    __listaladrillo:list

    def __init__(self):
        self.__listaladrillo=[]
    def agregar(self,nuevo):
        self.__listaladrillo.append(nuevo)
    def leerdatos(self):
        with open('C:\\Users\\Arias\\Desktop\\POO\\Unidad 3\\Ejercicio2\ladrillos.csv') as archivo:
            reader=csv.reader(archivo, delimiter=';')
            band=True
            for fila in reader:
                if band:
                    band=False
                else:
                    xcant=int(fila[0])
                    xid=int(fila[1])
                    xkg=float(fila[2])
                    xcosto=float(fila[3])
                    nuevoladri=ladrillo(xcant,xid,xkg,xcosto)
                    self.agregar(nuevoladri)
            archivo.close()

