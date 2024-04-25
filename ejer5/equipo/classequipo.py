class equipo:
    __id:int
    __nombre:str
    __golesA:int
    __golesC:int
    __difgoles:int
    __puntos:int

    def __init__(self, xid, xnom, xgola, xgolc, xdif, xpun):
        self.__id=xid
        self.__nombre=xnom
        self.__golesA=xgola
        self.__golesC=xgolc
        self.__difgoles=xdif
        self.__puntos=xpun

    def getid (self):
        return self.__id
    def getnom (self):
        return self.__nombre
    def getgola (self):
        return self.__golesA
    def getgolc (self):
        return self.__golesC
    def getdif (self):
        return self.__difgoles
    def getpunto (self):
        return self.__puntos