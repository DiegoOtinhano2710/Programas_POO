from gestorladrillo import Gladrillo
from gestormat import Gmaterial
def menu():
    gl=Gladrillo()
    gm=Gmaterial()
    gl.leerdatos()
    gm.leerdatos()
    opcion=input('''Seleccionar una opción:
                 1) Costo y características del ladrillo
                 2) Costo de fabricacion de cada ladrillo pedido
                 3) Mostrar datos de los ladrillos
                 4) Salir del menú
                 --> ''')
    while opcion!='4':
        if opcion=='1':
            pass
        elif opcion=='2':
            pass
        elif opcion=='3':
            pass
        opcion=input("Seleccionar una opción: ")
if __name__=='__main__':
    menu()