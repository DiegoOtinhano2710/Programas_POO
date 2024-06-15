from ClassMatRef import materialrefractario as mr
import csv
class Gmaterial:
    __listamat:list

    def __init__(self):
        self.__listamat=[]
    def agregar(self,nuevo):
        self.__listamat.append(nuevo)
    def leerdatos(self):
        with open('C:\\Users\\Arias\\Desktop\\POO\\Unidad 3\\Ejercicio2\materiales.csv') as archivo:
            reader=csv.reader(archivo, delimiter=';')
            band=True
            for fila in reader:
                if band:
                    band=False
                else:
                    xmat=int(fila[0])
                    xcar=fila[1]
                    xcant=float(fila[2])
                    xcostoad=float(fila[3])
                    nuevomat=mr(xmat,xcar,xcant,xcostoad)
                    self.agregar(nuevomat)
            archivo.close()
        
