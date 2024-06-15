class depa:
    __Id:str
    __nya:str
    __numpiso:str
    __numdepa:str
    __canth:int
    __cantb:int
    __sup:float
    def __init__(self,id,nya,np,nd,canth,cantb,sup):
        self.__Id=id
        self.__nya=nya
        self.__numpiso=np
        self.__numdepa=nd
        self.__canth=canth
        self.__cantb=cantb
        self.__sup=sup

    def __str__(self):
        return f'''Nombre del propietario del departamento {self.__numdepa} del piso {self.__numpiso}: {self.__nya}'''
    def getsup(self):
        return(self.__sup)
    def getnya(self):
        return(self.__nya)
    def gethab(self):
        return(self.__canth)
    def getba(self):
        return(self.__cantb)
    def getpiso(self):
        return(self.__numpiso)
        