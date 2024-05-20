class demartamento:
    __Id: int
    __NomyAp: str
    __NroPiso: int
    __NroDepa: int
    __CanDor: int
    __CantBaños: int
    __Sup: float
    ## Inicializamos la clase con
    def __init__ (self, xid, xnom, xnroP, xnroD, xcantD, xCantB, xSup):
        self.__Id = xid
        self.__NomyAp = xnom
        self.__CanDor = xcantD
        self.__NroPiso = xnroP
        self.__NroPiso = xnroD
        self.__CantBaños = xCantB
        self.__Sup = xSup
    def getNyA (self):
        return self.__NomyAp
    def getSup (self):
        return self.__Sup
    def getNroPiso (self):
        return self.__NroPiso
    
    ## Metodo encargado de indicar si tiene 3 dormitorios y mas de un baño
    def suit (self):
        retorna = 0
        if self.__CanDor == 3 and self.__CantBaños > 1:
            retorna = 1
        return retorna
    
        