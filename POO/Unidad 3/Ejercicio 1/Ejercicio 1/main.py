## Menu principal del ejercicio N1 Unidad 3
from GestorEdificio import GestorEdi
if __name__ == '__main__':
    GestorE = GestorEdi()
    print ("[1] Carga de Edificios.")
    print ("[2] Dado un edificio muestra nombre de inquilinos.")
    print ("[3] Mostrar Superficie total cubierta por un edificio.")
    print ("[4] Dado un propietario mostrar superficie de su departamento.")
    print ("[5] Dado un numero de piso mostrar cantidad de departamento con 3 dormitorios y mas de un baño.")
    print ("[6] Salir del sistema.")
    aux = int (input ("Seleccione una opcion: "))
    while aux != 6:
        if aux == 1:
            GestorE.carga()
            print ("Carga realizada con exito.")
        elif aux == 2:
            nom = input ("Ingrese el nombre del edificio para conocer inquilinos: ")
            existe = GestorE.mostrar_inquilinos(nom)
            if existe == -1:
                print ("No existe edificio con ese nombre.")
        elif aux == 3:
            nom = input ("Ingrese el nombre del edificio para conocer su superficie: ")
            existe = GestorE.mostrarSup(nom)
            if existe == -1:
                print ("No existe edificio con ese nombre.")
            else:
                print (f"La superficie del edificio es: {existe}")
        elif aux == 4:
            prop = input ("Ingrese el nombre del propietario: ")
            GestorE.SuperficieInquilino(prop)
        elif aux == 5:
            nro = int (input("Ingrese el nro de piso a contar: "))
            GestorE.mostrarsuit(nro)
        else:
            aux = int (input("Seleccione una opcion valida: "))
        print ("[1] Carga de Edificios.")
        print ("[2] Dado un edificio muestra nombre de inquilinos.")
        print ("[3] Mostrar Superficie total cubierta por un edificio.")
        print ("[4] Dado un propietario mostrar superficie de su departamento.")
        print ("[5] Dado un numero de piso mostrar cantidad de departamento con 3 dormitorios y mas de un baño.")
        print ("[6] Salir del sistema.")
        aux = int (input ("Seleccione una opcion: "))
    print ("Gracias....")
