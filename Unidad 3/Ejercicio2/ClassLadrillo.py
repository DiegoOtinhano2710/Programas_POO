class ladrillo:
    __alto=7
    __largo=25
    __ancho=15
    __cant:int
    __id:int
    __kgMatprimUti:float
    __costo:float
    __listaMR:list

    def __init__(self,cant,id,kg,costo):
        self.__cant=cant
        self.__id=id
        self.__kgMatprimUti=kg
        self.__costo=costo
        self.__listaMR=[]
    
