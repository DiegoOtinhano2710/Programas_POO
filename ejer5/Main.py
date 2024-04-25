from fecha.gestorfecha import gestorF
from equipo.gestorequipo import gestorE
if __name__=='__main__':
    gesequi=gestorE
    gesfe=gestorF
    opcion=input("Elegir la opción que quiera:\na- Leer los datos de los equipos.\nb- Leer los datos de las fechas.\nc- obtener datos de un equipo.\nd- Actualizar tabla.\ne- Ordenar la tabla.\nf- Almacenar tabla en csv.\n")
    if opcion=='a':
        gesequi.leerdatos()
    elif opcion=='b':
        gesfe.leerdatos()
    elif opcion=='c':
        nom=input("ingresar nombre del equipo: ")
        