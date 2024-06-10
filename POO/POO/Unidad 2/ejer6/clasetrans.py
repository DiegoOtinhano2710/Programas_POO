class Transaccion:
    __cvu:str
    __numtrans:str
    __importe:float
    __tipotrans:str

    def __init__(self,cvu,num,imp,tipo):
        self.__cvu=cvu
        self.__numtrans=num
        self.__importe=imp
        self.__tipotrans=tipo
    
    def getcvu(self):
        return self.__cvu
    def getnum(self):
        return self.__numtrans
    def getimp(self):
        return self.__importe
    def gettipo(self):
        return self.__tipotrans