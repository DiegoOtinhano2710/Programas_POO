from classmoto import moto
import csv
class gestorm:
    __listamoto:list
    def __init__(self):
        self.__listamoto=[]                     #crea la lista vacía

    def agregarmoto(self, unamoto):
        self.__listamoto.append(unamoto)        #agrega una componente a la lista con los datos de la moto
    
    def leerdatos(self):
        archivo = open('datomoto.csv')          #abre el archivo con la lista de datos de las motos
        reader = csv.reader(archivo, delimiter=';')     #se usa esta variable para leer los datos del archivo csv. el delimiter sirve para separar cada dato
        bandera=True
        for fila in reader:                         #fila es el arreglo que trae los datos. cada componente trae un dato que fueron separados por los ';'
            if bandera==True:                       #las filas de los csv son arreglos, el primer arreglo de todos es la cabecera que solo tiene el nombre de los datos. no interesa guardar
                bandera=False                       #se usa esta bandera para que la primera vez que entra solo la cambie salteando la cabecera. las siguentes veces entran por el else
            else:
                patente=fila[0]                     #en el arreglo 'fila' componente 0 se guarda la patente
                marca=fila[1]                       #en el arreglo 'fila' componente 1 se guarda la marca
                NyA=fila[2]                         #en el arreglo 'fila' componente 2 se guarda el name
                kilom=fila[3]                       #en el arreglo 'fila' componente 3 se guarda el kilometraje
                unamoto = moto(patente, marca, NyA, kilom)  #crea una instancia de la clase moto y envía las variables leídas del csv como parametros
                self.agregarmoto(unamoto)           #llama al metodo agregar moto para que guarde ese objeto en la lista
    
    def buscar(self, xpat):
        indice=0
        retorno=None
        bandera=False
        while not bandera and indice < len(self.__listamoto):
            if self.__listamoto[indice].getpat()==xpat:
                bandera=True
            else:
                indice += 1
        return bandera