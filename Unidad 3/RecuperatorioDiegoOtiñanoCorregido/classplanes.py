import abc
from abc import ABC
class planes:
    __nombre_comp:str
    __duracion_plan:int
    __cobertura_geo:str
    __precio_base:float

    def __init__(self,nom,dur,cob,precio):
        self.__nombre_comp=nom
        self.__duracion_plan=int(dur)
        self.__cobertura_geo=cob
        self.__precio_base=float(precio)
    
    def __str__(self):
        return f'''Nombre de la compañía: {self.__nombre_comp}
Duración del plan: {self.__duracion_plan}
Cobertura geográfica: {self.__cobertura_geo}'''

    def getdur(self):
        return self.__duracion_plan
    
    def getcob(self):
        return self.__cobertura_geo
    def getnom(self):
        return self.__nombre_comp
    def getpreciobase(self):
        return self.__precio_base
    @abc.abstractmethod
    def getimporte(self):
        pass

    def datos(self,tipo):
        print(f'Tipo: {tipo}')
        print(self)
        print(f'Importe final:{self.getimporte()}')
        print("=======================================================================================")

    