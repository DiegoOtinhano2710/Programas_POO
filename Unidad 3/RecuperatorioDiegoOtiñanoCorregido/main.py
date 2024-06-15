from gestor import gestorplanes

def menu():
    gp=gestorplanes()
    gp.leerdatos()
    try:
        op=int(input('''Seleccionar una opción:
                1) Tipo de plan
                2) Planes por cobertura geográfica
                3) Cantidad de canales internacionales
                4) Datos de los planes
                5) Salir
                --> '''))
        while op!=5:
            if op==1:
                gp.tipoplan()
            elif op==2:
                gp.planesxcob()
            elif op==3:
                gp.canalesinter()
            elif op==4:
                gp.datosplanes()
            assert op<5
            op=int(input('seleccionar una opción: '))
    except ValueError:
        print("ERROR. Ingrese una opción válida")
        menu()
    except AssertionError:
        print("ERROR. Ingrese una opción válida")
        menu()



if __name__=='__main__':
    menu()