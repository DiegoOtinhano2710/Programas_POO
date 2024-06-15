from nodo import Nodo
from classplanestel import planes_telefonia
from classplanesTV import planes_TV
import csv

class gestorplanes:
    __tope:int
    __comienzo:Nodo
    __actual:Nodo
    __indice:int

    def __init__(self):
        self.__tope=0
        self.__indice=0
        self.__comienzo=None
        self.__actual=None

    def get_tope(self):
        return self.__tope

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.__indice==self.__tope:
            self.__actual=self.__comienzo
            self.__indice=0
            raise StopIteration
        else:
            self.__indice+=1
            dato= self.__actual.getDato()
            self.__actual=self.__actual.getSiguiente()
            return dato
    
    def agregar_publicacion(self, plan):
        nodo = Nodo(plan)
        nodo.setSiguiente(self.__comienzo)
        self.__comienzo = nodo
        self.__actual = nodo
        self.__tope += 1
    
    def leerdatos(self):
        try:
            archivo=open('planes.csv')
            reader=csv.reader(archivo, delimiter=';')
            band=False
            for fila in reader:
                if band==False:
                    band=True
                else:
                    tipo=fila[0]
                    comp=fila[1]
                    dur=fila[2]
                    cob=fila[3]
                    precio=fila[4]
                    a=fila[5]
                    b=fila[6]
                    if tipo.lower()=='m':
                        plan=planes_telefonia(comp,dur,cob,precio,a,b)
                    elif tipo.lower()=='t':
                        plan=planes_TV(comp,dur,cob,precio,a,b)
                    self.agregar_publicacion(plan)
            archivo.close()
        except FileNotFoundError:
            print('Archivo no encontrado')

    def mostrar_tipo_plan(self, pos):
            try: 
                if pos < 0 or pos >= self.__tope:
                    raise IndexError('Indice fuera de rango')
                nodo = self.__comienzo
                indice = 0
                while nodo is not None and indice < pos:
                    nodo = nodo.getSiguiente()
                    indice += 1
                if nodo is not None:
                    plan = nodo.getDato()  
                    if isinstance(plan,planes_telefonia):
                        print(f'El plan que se encuentra en la posición {pos} es de telefonía')
                    elif isinstance(plan,planes_TV):
                        print(f'El plan que se encuentra en la posición {pos} es de Televisión') 
            except IndexError:
                return IndexError


    def tipoplan(self):
        pos=int(input("Ingresar posición que desee conocer: "))
        e=self.mostrar_tipo_plan(pos)
        if e is IndexError:
            print("Índice fuera de rango")
            self.tipoplan()
        

    def planesxcob(self):
        cob=input('Ingresar cobertura geográfica: ').lower()
        cont=0
        nodo = self.__comienzo
        indice = 0
        while nodo is not None and indice <= self.__tope:
            plan=nodo.getDato()
            cobertura=plan.getcob().lower()
            if cobertura == cob:
                cont+=1
            if cobertura == 'nacional e internacional':
                if cob == 'nacional':
                    cont+=1
                elif cob=='internacional':
                    cont+=1
            nodo = nodo.getSiguiente()
            indice += 1
        print(f'La cantidad de planes que corresponden a la coberertura geografica {cob} es: {cont}')
    
    def canalesinter(self):
        cantidad=int(input('Ingresar cantidad de canales internacionales: '))
        nodo = self.__comienzo
        indice = 0
        control=0
        while nodo is not None and indice <= self.__tope:
            plan=nodo.getDato()
            if isinstance(plan, planes_TV):
                cant=plan.getinter()
                if  cant >= cantidad:
                    print(f'Compañía con una cantidad igual o mayor a la ingresada: {plan.getnom()}')
                    control+=1
            nodo = nodo.getSiguiente()
            indice += 1
        if control==0:
            print("No hay compañías que ofrezcan una cantidad de canales internacionales igual o mayor a la solicitada")

    def datosplanes(self):
        nodo = self.__comienzo
        indice = 0
        while nodo is not None and indice <= self.__tope:
            plan=nodo.getDato()
            if isinstance(plan, planes_telefonia):
                tipo='Telefonía'
            if isinstance(plan,planes_TV):
                tipo='Televisión'
            plan.datos(tipo)
            nodo = nodo.getSiguiente()
            indice += 1