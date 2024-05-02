from gestorcliente import Gestorcliente
from gestormovimiento import GestorMovimiento
if __name__=='__main__':
    gc=Gestorcliente()
    gm=GestorMovimiento()
    gc.leerdatos()
    gm.leerdato()
    band=True
    while band==True:
        opcion=input("Seleccionar una opción:\na) Actualizar saldo.\nb) Cliente sin movimientos en abril del 2024.\nc) Ordenar Movimientos.\nd) Salir del menú.\n")
        if opcion=='a':
            band2=True
            xdni=str(input("Ingresar DNI: "))
            nom, ap,num,saldo = gc.buscarsaldo(xdni)
            print ('''Cliente: {}{}                      Numero de Cuenta: {}
            Saldo anterior: {}
            Movimientos'''.format(nom, ap, num, saldo))
            gm.actualizarsaldo(saldo,num)
        elif opcion=='b':
            dni=input("Ingresar DNI: ")
            xnum, xap, xnom = gc.buscarnum(dni)
            band3=gm.buscarmov(num)
            if band3==True:
                print("Apellido y Nombre del cliente sin movimientos con DNI {}:{} {}".format(dni,xap,xnom))
        elif opcion=='c':
            gm.ordenar
        elif opcion=='d':
            band=False
            