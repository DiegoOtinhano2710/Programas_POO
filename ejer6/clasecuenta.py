class Cuenta:
    __apellido:str
    __nombre:str
    __dni:str
    __telefono:str
    __saldo:float
    __cvu:str
    __porcanual=0

    def __init__(self,ap,nom,dni,tel,saldo,cvu,porc):
        self.__apellido=ap
        self.__nombre=nom
        self.__dni=dni
        self.__telefono=tel
        self.__saldo=saldo
        self.__cvu=cvu
        self.__porcanual=(porc/100)
    
    def getap(self):
        return self.__apellido
    def getnom(self):
        return self.__nombre 
    def getdni(self):
        return self.__dni 
    def gettel(self):
        return self.__telefono
    def getsaldo(self):
        return self.__saldo 
    def getcvu(self):
        return self.__cvu
    def getporc(self):
        return self.__porcanual
    def setsaldo(self,actualizacion):
        self.__saldo=actualizacion
    def setporc(self,nuevo):
        self.__porcanual=(nuevo/100)