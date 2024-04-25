import datetime
class fecha:
    __fechapartido:datetime
    __idlocal:int
    __idvisita:int
    __cantgolloc:int
    __cantgolvis:int

    def __init__(self, xfecha, xidl, xidv, xcantl, xcantv):
        self.__fechapartido=xfecha
        self.__idlocal=xidl
        self.__idvisita=xidv
        self.__cantgolloc=xcantl
        self.__cantgolvis=xcantv
    
    def getfecha (self):
        return self.__fechapartido
    def getidl (self):
        return self.__idlocal
    def getidv (self):
        return self.__idvisita
    def getgoll (self):
        return self.__cantgolloc
    def getgolv (self):
        return self.__cantgolvis