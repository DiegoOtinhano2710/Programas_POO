class gestor:
    __ventas=list                       #si se declara tipo list. luego en el init, hay que ponerle los []
    __farm=int
    __dias=7
    def __init__ (self, xf=0):
        self.__farm=xf
        self.__ventas=[]
        for i in range (self.__farm):
            self.__ventas.append([0] * self.__dias)
        pass
    def acumular(self,xdia,xsuc,importe):
        self.__ventas[xsuc][xdia] =+ importe
    def total_sucursal(self, xsuc):
        acum=0
        for i in range (self.__dias):
            acum =+ self.__ventas[xsuc][i]
        return(acum)
    def max_dia(self, xdia):
        max=0
        aux=0
        for i in range (self.__farm):
            if self.__ventas[i][xdia] > max:
                aux=i
                max=self.__ventas[i][xdia]
        return(aux)
    def min_sucursal(self):
        min=10000000
        aux2=0
        for i in range (self.__farm):
            acum=0
            for j in range (self.__dias):
                acum += self.__ventas[i][j]
            if acum < min:
                aux2 = i
                min = self.__ventas[i][j]
        return(aux2)
    def total_total(self):
        acum=0
        for i in range (self.__farm):
            for j in range (self.__dias):
                acum += self.__ventas[i][j]
        return(acum)