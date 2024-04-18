class CajaDeAhorro:
    __nroCuenta: str
    __cuit: str
    __apellido: str
    __nombre: str
    __saldo: float
    def __init__(self, xnro='', xcuit='', xapellido='', xnombre='', xsaldo=0):
        self.__nroCuenta = xnro
        self.__cuit = xcuit
        self.__apellido =xapellido
        self.__nombre = xnombre
        self.__saldo = xsaldo
    def mostrardatos(self):
        print("Nombre y apellido: {} {} ",self.__nombre,' ',self.__apellido,"")
        print("CUIT: {} ",self.__cuit,"")
        print("Número de cuenta: {} ",self.__nroCuenta,"")
        print("Saldo: {} ",self.__saldo,"")
    def extraer(self, x):
        if x >= self.__saldo:
            aux = self.__saldo - x
        else:
            aux = -1
        return aux
    def depositar(self, y):
        if y > 0:
            aux = self.__saldo += y
            return aux
    def validarCUIL(self, c):
        xc = c.split('-')
        if len(xc[0]) != 2:
            print("ERROR")
        elif  xc[0] != '27' or xc[0] != '20' or xc[0] != '30':
            print("ERROR")
        if len(xc[1]) != 8:
            print("ERROR")
        aux = xc[0] + xc[1]
        acum = 0
        acum += int(aux[0]) * 5
        acum += int(aux[1]) * 4
        acum += int(aux[2]) * 3
        acum += int(aux[3]) * 2
        acum += int(aux[4]) * 7
        acum += int(aux[5]) * 6
        acum += int(aux[6]) * 5
        acum += int(aux[7]) * 4
        acum += int(aux[8]) * 3
        acum += int(aux[9]) * 2
        resto = acum % 11
        if resto == 0:
            verif = 0
