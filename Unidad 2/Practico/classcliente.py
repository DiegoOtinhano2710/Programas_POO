class Cliente:
    __nombre:str
    __apellido:str
    __dni:str
    __num_cuenta:str
    __saldo_anterior:float

    def __init__(self,nom,ap,xdni,num,saldo):
        self.__nombre=nom
        self.__apellido=ap
        self.__dni=xdni
        self.__num_cuenta=num
        self.__saldo_anterior=saldo
    
    def getnom(self):
        return self.__nombre
    def getap(self):
        return self.__apellido
    def getdni(self):
        return self.__dni
    def getnum(self):
        return self.__num_cuenta
    def getsaldo(self):
        return self.__saldo_anterior