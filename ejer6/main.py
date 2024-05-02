from gestorcuenta import Gcuenta
from gestortrans import Gtrans
if __name__=="__main__":
    gc=Gcuenta
    gt=Gtrans
    opcion=input("Seleccionar opción:\na. Datos del cliente.\nb. Modificar porcentaje anual.\nc. Actualizar saldo.\nd. Informar saldo.\ne. Guardar datos actualizados\n")
    if opcion=='a':
        dni=input("Ingresar DNI: ")
        ap, nom, cvu, saldo = gc.buscar(dni)
        print("Apellido: {}\nNombre: {}\nCVU: {}\nSaldo: {}".format(ap,nom,cvu,saldo))
    elif opcion=='b':
        nuevoporc=float(input("Ingresar nuevo porcentaje anual del rendimiento: "))
        gc.actporc(nuevoporc)
    elif opcion=='c':


    elif opcion=='d':
        cvu=input("Ingresar cvu: ")
        total=gt.calcular(cvu)