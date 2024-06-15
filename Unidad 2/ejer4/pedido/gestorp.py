from classpedido import pedido
import csv
class gestorpedi:
    __listapedido:list

    def __init__(self):
        self.__listapedido = []
    
    def agregarpedido(self, unpedido):
        self.__listapedido.append(unpedido)

    def leerdatos(self):
        archivo=open('pedidos.csv')
        reader=csv.reader(archivo, delimiter=';')
        bandera=True
        for fila in reader:
            if bandera==True:
                bandera=False
            else:
                patenteasign=fila[0]
                idpedido=fila[1]
                comida=fila[2]
                estimado=fila[3]
                precio=[4]
                unpedido=pedido(patenteasign, idpedido, comida, estimado, precio)
                self.agregarpedido(unpedido)

    def definirtiempo(self, patente, ID, tiempo):
        i=0
        while i < len(self.__listapedido) and self.__listapedido[i].getid()!= ID:
            i+1
        if self.__listapedido[i].getid() == ID:
            self.__listapedido[i].setreal(tiempo)

    def ordenar(self):
        for i in range (len(self.__listapedido)):
            for j in range (len(self.__listapedido-1-i)):
                if self.__listapedido[j].getpat() < self.__listapedido[j+1].getpat():
                    self.__listapedido[j], self.__listapedido[j+1] = self.__listapedido[j+1], self.__listapedido[j]
    
    def promedio(self, pat):
        i=0
        prom=0
        cant=0
        band=False
        while not band and i < len(self.__listapedido[i]):
            if pat == self.__listapedido[i].getasign():
                j=i
                while pat == self.__listapedido[j].getasign():
                    prom += float(self.__listapedido[i].getreal)
                    cant += 1
                    j+=1
                band=True
            else: 
                i+=1
        return(prom/cant)