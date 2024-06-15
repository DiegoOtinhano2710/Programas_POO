class moto:
    __patente: str
    __marca: str
    __NyAconductor: str
    __kilometraje: float

    def __init__(self, xpat, xmar, xnom, xkilom):               #recibe del metodo 'leerdatos' los parametros para construir el objeto con esos datos
        self.__patente = xpat                                   #pruebaxd
        self.__marca = xmar
        self.__NyAconductor = xnom
        self.__kilometraje = xkilom
    
    def getpat(self):
        return self.__patente
    def getmarca(self):
        return self.__marca
    def getNyA(self):
        return self.__NyAconductor
    def getk(self):
        return self.__kilometraje