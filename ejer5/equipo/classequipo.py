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

    