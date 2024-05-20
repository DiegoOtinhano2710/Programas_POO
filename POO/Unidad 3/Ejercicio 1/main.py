from gestoredi import gestor
def menu():
    ge=gestor()
    ge.leerdatos()
    opcion=input('''Seleccionar una opción: 
                 1) Propietarios de los departamentos
                 2) Superficie total cubierta de un edificio
                 3) Superficie cubierta por un departamento
                 4) Cantidad de departamentos con tres dormitorios y más de un baño
                 5) Salir del Menú
                 --> ''')
    while opcion!='5':
        if opcion=='1':
            ge.propietarios()
        elif opcion=='2':
            ge.superficie()
        elif opcion=='3':
            ge.superficiexdueño()
        elif opcion=='4':
            ge.depa4()
        opcion=input("Seleccionar una opción: ")

if __name__=='__main__':
    menu()