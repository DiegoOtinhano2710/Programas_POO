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
        lis=gesfe.getlista()
        i=0
        nom=input("ingresar nombre del equipo: ")
        id=gesequi.buscarid(nom)
        print("Equipo: {}".format(nom))
        print("Fecha{10}Goles a Favor{10}Goles en Contra{10}Diferencia de goles{10}Puntos")
        while 1<len(lis):
            xfecha, gola, golco, xpunto = gestorF.buscarfecha(id)
            dif=abs(gola-golco)
            print("{10}{10}{10}{10}{10}".format(xfecha, gola, golco, dif, xpunto))

