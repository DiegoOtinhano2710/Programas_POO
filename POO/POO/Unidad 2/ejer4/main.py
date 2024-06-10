from moto.gestormoto import gestorm
from moto.classmoto import moto
from pedido.classpedido import pedido
from pedido.gestorp import gestorpedi
if __name__ == '__main__':
    gestormoto=gestorm
    gestorpedido=gestorpedi
    opcion=input("Ingrese numero de opción:1-leer datos de motos.\n 2- Leer los datos de los pedidos.\n 3-agregar pedido.\n 4-tiempo real de entrega.\n 5-Tiempo promedio de un repartidor.\n 6-generar listado por moto.\n")
    if opcion=='1':
        gestormoto.leerdatos()
    elif opcion=='2':
        gestorpedido.leerdatos()
        gestorpedido.ordenar()
    elif opcion=='3':
        pat=input("Patente de la moto asignada: ")
        indice=gestormoto.buscar()
        if indice == False:
            print("Error al ingresar patente")
        else:
            id=input("ingresar ID del pedido: ")
            com=input("ingresar comida ordenada: ")
            est=input("ingresar tiempo estimado de entrega: ")
            precio=float(input("ingresar precio del pedido: "))
            nuevopedido=pedido(pat, id, com, est, precio)
            gestorpedido.agregarpedido(nuevopedido)
    elif opcion=='4':
        xpat=input("Ingresar patente: ")
        xid=input("ingresar ID del pedido: ")
        xtiempo=str(input("Ingresar tiempo real del pedido: "))
        gestorpedido.definirtiempo(xpat, xid, xtiempo)
    elif opcion=='5':
        xpat=input("ingresar patente: ")
        print("El nombre del conductor de la moto con patente {} es: {}".format(xpat, gestormoto.devolvernya(xpat)))
        print("el tiempo promedio de entrega es: {}".format(gestorpedido.promedio(xpat)))
        