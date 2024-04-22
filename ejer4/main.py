from moto.gestormoto import gestorm
from moto.classmoto import moto
from pedido.classpedido import pedido
from pedido.gestorp import gestorpedi
if __name__ == '__main__':
    unamoto=gestorm
    unamoto.leerdatos()
    unpedido=gestorpedi
    unpedido.leerdatos()
    confirmar=str(input("¿Agregar pedidos? si/no"))
    while confirmar=='si':
        pat=str(input("Patente de la moto asignada: "))
        indice=unamoto.buscar()
        if indice == False:
            print("Error al ingresar patente")
        else:
            id=str(input("ingresar ID del pedido: "))
            com=str(input("ingresar comida ordenada: "))
            est=str(input("ingresar tiempo estimado de entrega: "))
            real=str(input("ingresar tiempo real de entrega: "))
            precio=float(input("ingresar precio del pedido: "))
            nuevopedido=pedido(pat, id, com, est, real, precio)
    