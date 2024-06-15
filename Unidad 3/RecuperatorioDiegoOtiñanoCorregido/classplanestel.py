from classplanes import planes
class planes_telefonia(planes):
    __tipo_llamada:str
    __cant_min:int

    def __init__(self,nom,dur,cob,precio,tipo,cant):
        super().__init__(nom,dur,cob,precio)
        self.__tipo_llamada=tipo
        self.__cant_min=int(cant)
    
    def getimporte(self):
        base=super().getpreciobase()
        if self.__tipo_llamada=='internacional':
            base=base+ base*0.2
        elif self.__tipo_llamada=='locales':
            base=base- base*0.075
        return base