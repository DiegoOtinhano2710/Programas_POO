## Manejador de Edificios
from ClaseEdificio import edificio
from ClaseDepartamento import demartamento
import csv
class GestorEdi:
    __edificios: list
    def __init__(self):
        self.__edificios = []
    def agregar (self, edifi):
        self.__edificios.append(edifi)
    ## Metodo encargado de la carga desde el archivo

    def carga (self):
        archivo = open("EdificioNorte.csv")
        reader = csv.reader (archivo, delimiter=';')
        xedificio = None
        for fila in reader:
            if len(fila) == 6:
                xedificio = edificio (int(fila[0]), fila[1], fila[2], fila[3], int(fila[4]))
                self.agregar(xedificio)
            else:
                yid = int(fila[1])
                ynom = fila[2]
                ynroP = int(fila[3])
                ynroD = int (fila[4])
                ycantD = int (fila[5])
                ycantB = int (fila[6])
                ysup = float (fila[7])
                xedificio.agregarDepartamento(yid, ynom, ynroP, ynroD, ycantD, ycantB, ysup)
        archivo.close()

    ## Dado un nombre de edificio mostrar el nombre y apellido de cada uno de los edificios
    def mostrar_inquilinos (self, xnom):
        retorno = None
        i = 0
        while self.__edificios[i].getNombre() != xnom and i <len (self.__edificios):
            i += 1
        if i == len (self.__edificios):
            retorno = -1
        else:
            self.__edificios[i].mostrarNyA()
            retorno = 1
        return retorno
    
    ## Mostrar superfice total de un edificio
    def mostrarSup (self, xnom):
        retorno = None
        i = 0
        while self.__edificios[i].getNombre() != xnom and i <len (self.__edificios):
            i += 1
        if i == len (self.__edificios):
            retorno = -1
        else:
            retorno = self.__edificios[i].calcularSup()
        return retorno
    
    def SuperficieInquilino (self, xnom):
        for edificio in self.__edificios:
            listaDepartamentos = edificio.devolverDepartamentos()
            for departamento in listaDepartamentos:
                if departamento.getNyA() == xnom:
                    print (f"Superficie de su departamento: {departamento.getSup()}")
                    porce = (departamento.getSup() / edificio.calcularSup()) * 100         
                    print (f"Porcentaje de superficie: {porce}")
        
    ## Mostrar la cantidad de departamentos con 3 dormitorios y mas de un baño
    def mostrarsuit(self, nropiso):
        for edificio in self.__edificios:
            cont = 0
            listaDepartamentos = edificio.devolverDepartamentos()
            for departamento in listaDepartamentos:
                if departamento.getNroPiso() == nropiso:
                    cont = cont + departamento.suit()
            print (f" Edificio: {edificio.getNombre()}\n Nro Piso: {nropiso}\n Departamentos que Cumplen: {cont}")
    