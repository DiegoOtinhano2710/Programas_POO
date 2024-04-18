from Claseejer3 import gestor          #desde el nombre del archivo importa el nombre de la clase
if __name__ == '__main__':
    xsuc=int(input("ingresar cantidad de sucursales: "))
    Gestorvent = gestor(xsuc)
    confirmar = str(input("¿Acceder a una funcionalidad? si/no: "))
    while (confirmar == 'si'):
        opcion = str(input("'1'- ingresar importe del día de una sucursal.\n '2'- obtener factura de una sucursal.\n '3'- obtener sucursal que más facturó en un día.\n '4'- obtener sucursal que menos facturó en la semana.\n '5'- Calcular el total facturado\n"))
        if opcion == '1':
            dia=int(input("ingresar un día de la semana (1-7): "))
            suc=int(input("ingresar numero de sucursal(1-{}): ".format(xsuc)))
            imp=float(input("ingresar importe: "))
            Gestorvent.acumular(dia-1, suc-1, imp)
        elif opcion == '2':
            suc=int(input("ingresar una sucursal (1-{}): ".format(xsuc)))
            print("el total de esa sucursal es: {}".format(Gestorvent.total_sucursal(suc)))
        elif opcion == '3':
            dia=int(input("ingresar dia de la semana (1-7): "))
            print("la sucursal que más facturó el día {} fue {}".format(dia, Gestorvent.max_dia(dia)))
        elif opcion == '4':
            print("La sucursal que menos facturó durante la semana fue: {}".format(Gestorvent.min_sucursal()))
        elif opcion == '5':
            print("el total facturado por todas las sucursales es: {}".format(Gestorvent.total_total()))
        confirmar=str(input("¿quiere acceder a otra funcionalidad? si/no: "))