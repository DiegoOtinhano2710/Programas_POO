## Esta clase resulta estar compuesta de departamentos, por tanto funcionara tambien como manejador de los departamento
from ClaseDepartamento import demartamento
class edificio:
    __Id: int
    __Nombre: str
    __Direccion: str
    __NomEmpre: str
    __CantPisos: int
    __Departamentos: list
    def __init__(self, xID, xENOM, XEDIR, XENOME, XECANT):
        self.__Id = xID
        self.__Nombre= xENOM
        self.__Direccion=XEDIR
        self.__NomEmpre= XENOME
        self.__CantPisos= XECANT
        self.__Departamentos = []
    def agregarDepartamento (self, yid, ynom, ynroP, ynroD, ycantD, ycantB, ysup):
        xdemartamento = demartamento(yid, ynom, ynroP, ynroD, ycantD, ycantB, ysup)
        self.__Departamentos.append(xdemartamento)

    def getNombre (self):
        return self.__Nombre
    
    ## Mostrar Los inquilinos de un edificio
    def mostrarNyA (self):
        for depa in self.__Departamentos:
            print (f"Nombre Y Apellido: {depa.getNyA()}")
    
    ## Calcular la superficie de un edificio
    def calcularSup(self):
        acum = 0
        for depa in self.__Departamentos:
            acum = acum + depa.getSup()
        return acum
    
    def devolverDepartamentos (self):
        return self.__Departamentos
    

        