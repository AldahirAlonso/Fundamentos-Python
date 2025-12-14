print("****** Sistema de Administracion de cuentas ******")

salir = False
while not salir:
    print(f'''Menu:
    1. Crear Cuenta
    2. Eliminar Cuenta
    3. Salir''')

    opcion = int(input("Ingrese una opcion: "))

    if opcion == 1:
        print('Creando Cuenta...\n')
    elif opcion == 2:
        print('Eliminando Cuenta...\n')
    elif opcion == 3:
        print('Saliendo del Sistema...\n')
        salir = True
    else:
        print("Opcion invalida.\n")
else:
    print("Terminando el Sistema de Administracion de Cuentas.")