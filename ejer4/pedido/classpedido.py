class pedido:
    __patenteasignado: str
    __idpedido: str
    __comida: str
    __testimado: str
    __treal: str
    __precio: float

    def __init__(self, xpat, xid, xcom, xtesti, xtreal, xp):
        self.__patenteasignado=xpat
        self.__idpedido=xid
        self.__comida=xcom
        self.__testimado=xtesti
        self.__treal=xtreal
        self.__precio=xp