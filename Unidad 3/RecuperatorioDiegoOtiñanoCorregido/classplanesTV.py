from classplanes import planes
class planes_TV(planes):
    __cant_canales_nacionales:int
    __cant_canales_inter:int

    def __init__(self,nom,dur,cob,precio,nac,inter):
        super().__init__(nom,dur,cob,precio)
        self.__cant_canales_nacionales=int(nac)
        self.__cant_canales_inter=int(inter)
    
    def getinter(self):
        return self.__cant_canales_inter
    def getnac(self):
        return self.__cant_canales_nacionales
    
    def getimporte(self):
        base = super().getpreciobase()
        if self.__cant_canales_inter > 10:
            base=base+ base*0.15
        return base
    