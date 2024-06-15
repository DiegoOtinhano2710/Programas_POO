from classedi import edificio
import csv
class gestor:
    __listadoedi:list
    def __init__(self):
        self.__listadoedi=[]
    def agregaredif(self,nuevoedi):
        self.__listadoedi.append(nuevoedi)

    def leerdatos(self):
        archivo=open('EdificioNorte.csv')
        reader=csv.reader(archivo,delimiter=';')
        xedi=None       #si se declara dentro del for, se pone en None siempre que itera
        for fila in reader:
            if len(fila)==6:
                xedi=edificio(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5])
                self.agregaredif(xedi)
            else:
                xid=fila[1]
                xnya=fila[2]
                xnp=fila[3]
                xnd=fila[4]
                xch=int(fila[5])
                xcb=int(fila[6])
                xsup=float(fila[7])
                xedi.agregardpt(xid,xnya,xnp,xnd,xch,xcb,xsup)
    
    def mostrar(self):
        i=0
        while i<len(self.__listadoedi):
            print(self.__listadoedi[i])
            self.__listadoedi[i].mostrardpt()
            i+=1
    
    def propietarios(self):
        nomedi=input("Ingresar nombre del edificio: ")
        i=0
        band=True
        while i<len(self.__listadoedi) and band:
            if nomedi==self.__listadoedi[i].getnom():
                self.__listadoedi[i].dueños()
                band=False
            else:
                i+=1
    
    def superficie(self):
        nomedi=input("Ingresar nombre del edificio: ")
        i=0
        band=True
        while i<len(self.__listadoedi) and band:
            if nomedi==self.__listadoedi[i].getnom():
                total=self.__listadoedi[i].sup()
                band=False
            else:
                i+=1
        if band==False:
            print("La superficie cubierta por el edificio {} es: {}".format(nomedi,total))
    
    def superficiexdueño(self):
        nom=input("Ingresar nombre y apellido del propietario: ")
        i=0
        while i < len(self.__listadoedi):
            totalxdepa=self.__listadoedi[i].supxper(nom)
            totaledi=self.__listadoedi[i].sup()
            porcentaje=round((totalxdepa*100)/totaledi , 2)
            name=self.__listadoedi[i].getnom()
            print("La superficie total de el/los departamento/s del propietarios{} es {} y representa el {}'%' de todo el {}".format(nom,totalxdepa,porcentaje,name))
            i+=1
    
    def depa4(self):
        piso=input("Ingresar número de piso: ")
        i=0
        while i<len(self.__listadoedi):
            cant=self.__listadoedi[i].habyba(piso)
            nom=self.__listadoedi[i].getnom()
            if cant==0:
                print("No hay departamentos en {} que tengan tres habitaciones y más de un baño en el piso".format(nom,piso))
            elif cant==1:
                print("En {} hay un solo departamento con tres habitaciones y más de un baño en el piso {}".format(nom,piso))
            else:
                print("En {} hay {} departamentos que tienen tres habitaciones y más de un baño en el piso {}".format(nom,cant,piso))
            i+=1