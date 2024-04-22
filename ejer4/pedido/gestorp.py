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
                real=fila[4]
                precio=[5]
                unpedido=pedido(patenteasign, idpedido, comida, estimado, real, precio)
                self.agregarpedido(unpedido)