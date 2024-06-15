class pedido:
    __patenteasignado: str
    __idpedido: str
    __comida: str
    __testimado: str
    __treal: str
    __precio: float

    def __init__(self, xpat, xid, xcom, xtesti, xp):
        self.__patenteasignado=xpat
        self.__idpedido=xid
        self.__comida=xcom
        self.__testimado=xtesti
        self.__treal=0
        self.__precio=xp
    
    def getasign(self):
        return self.__patenteasignado
    def getid(self):
        return self.__idpedido
    def getcom(self):
        return self.__comida
    def getest(self):
        return self.__testimado
    def getreal(self):
        return self.__treal
    def getprecio(self):
        return self.__precio
    
    def setreal(self, tiempo):
        self.__treal=tiempo

    def __lt__(self, otro):
        return True