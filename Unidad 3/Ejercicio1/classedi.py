from classdpto import depa
class edificio:
    __Id:int
    __nom:str
    __direc:str
    __nomemp:str
    __cantp:int
    __cantdept:int
    __departamentos:list
    def __init__(self,id,nom,direc,nome,cantp,cantdpt):
        self.__Id=id
        self.__nom=nom
        self.__direc=direc
        self.__nomemp=nome
        self.__cantp=cantp
        self.__cantdept=cantdpt
        self.__departamentos=[]
    
    def agregardpt(self,did,dnya,dnp,dnh,dch,dcb,dsup):
        nuevo=depa(did,dnya,dnp,dnh,dch,dcb,dsup)
        self.__departamentos.append(nuevo)
    
    def __str__(self):
        return f''''''
    def getnom(self):
        return self.__nom
    def dueños(self):
        i=0
        while i<len(self.__departamentos):
            print(self.__departamentos[i])
            i+=1
    def sup(self):
        cont=0
        i=0
        while i<len(self.__departamentos):
            cont+=self.__departamentos[i].getsup()
            i+=1
        return(cont)
    def supxper(self,nom):
        i=0
        sup=0
        while i<len(self.__departamentos):
            if nom==self.__departamentos[i].getnya():
                sup+=self.__departamentos[i].getsup()
            i+=1
        return sup
    def habyba(self,piso):
        cont=0
        i=0
        while i<len(self.__departamentos):
            if self.__departamentos[i].getpiso()==piso:
                if self.__departamentos[i].gethab()==3 and self.__departamentos[i].getba()>1:
                    cont+=1
            i+=1
        return cont