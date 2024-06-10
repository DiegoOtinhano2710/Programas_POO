class Movimiento:
    __numcuenta:str
    __fecha: str
    __descripcion:str
    __tipo:str
    __importe:float

    def __init__(self,num,fecha,des,tipo,imp):
        self.__numcuenta=num
        self.__fecha=fecha
        self.__descripcion=des
        self.__tipo=tipo
        self.__importe=imp
    
    def __str__(self):
        return f'Numero de cuenta:{self.__numcuenta}. Fecha:{self.__fecha}. Descripción:{self.__descripcion}. Tipo:{self.__tipo}. Importe:{self.__importe}'
    def getnum(self):
        return self.__numcuenta
    def getfecha(self):
        return self.__fecha
    def getdesc(self):
        return self.__descripcion
    def gettipo(self):
        return self.__tipo
    def getimp(self):
        return self.__importe
    def __lt__(self,other):
        return self.__numcuenta < other.__numcuenta