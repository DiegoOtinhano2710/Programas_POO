class moto:
    __patente: str
    __marca: str
    __NyAconductor: str
    __kilometraje: float

    def __init__(self, xpat, xmar, xnom, xkilom):               #recibe del metodo 'leerdatos' los parametros para construir el objeto con esos datos
        self.__patente = xpat
        self.__marca = xmar
        self.__NyAconductor = xnom
        self.__kilometraje = xkilom