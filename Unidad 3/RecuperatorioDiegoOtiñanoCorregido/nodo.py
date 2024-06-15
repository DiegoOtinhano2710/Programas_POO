from classplanes import planes
class Nodo:
    __plan: planes
    __siguiente: object
    def __init__(self, plan):
        self.__plan=plan
        self.__siguiente=None
        
    def setSiguiente(self, siguiente):
        self.__siguiente=siguiente
    def getSiguiente(self):
        return self.__siguiente
    def getDato(self):
        return self.__plan