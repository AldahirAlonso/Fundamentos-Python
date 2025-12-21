# Trabajo hecho por Aldahir Emmanuel Alonso Reyes, estudiante de Universidad Tecnológica de Emiliano Zapata de Morelos.
# Curso de Fundamentos de Programación de Python de Infotec.
# Unidad 1 - Ejercicio 1: Cajero Automatico.

# Asignacion de variables para contar billetes.
billetes1000 = 10
billetes500 = 10
billetes200 = 10
billetes100 = 10
billetes50 = 10
billetes20 = 10

# Asignacion de variables para entrega de billetes.
entregar1000 = 0
entregar500 = 0
entregar200 = 0
entregar100 = 0
entregar50 = 0
entregar20 = 0

# Saldo en la cuenta del usuario.
montoRestante = 1000

print("========== BIENVENIDO AL CAJERO AUTOMÁTICO! ==========")
print("Saldo actual:", montoRestante)
entrada = input("Ingrese el monto a retirar (0 para salir): ")

# Inicia ciclo while.
# El ciclo se repite mientras el usuario no ingrese 0 para salir.
while entrada != "0":
    # Validacion de entrada.
    if not entrada.isdigit():
        print("Por favor, ingrese un número válido.")
    else:
        monto = int(entrada)
        
        # Validacion de monto.
        if monto > montoRestante:
            print("Saldo insuficiente!")
        elif monto % 10 != 0:
            print("El monto debe ser múltiplo de 20.")
        else:
            # Guardamos el monto original para restarlo al final si la operación es exitosa
            monto_original = monto 
            
            # Calculo de billetes a entregar.
            entregar1000 = min(monto // 1000, billetes1000)
            monto -= entregar1000 * 1000

            entregar500 = min(monto // 500, billetes500)
            monto -= entregar500 * 500

            entregar200 = min(monto // 200, billetes200)
            monto -= entregar200 * 200

            entregar100 = min(monto // 100, billetes100)
            monto -= entregar100 * 100

            entregar50 = min(monto // 50, billetes50)
            monto -= entregar50 * 50

            entregar20 = min(monto // 20, billetes20)
            monto -= entregar20 * 20

            # Verificacion de si se pudo entregar el monto solicitado.
            if monto == 0:
                
                montoRestante -= monto_original
                billetes1000 -= entregar1000
                billetes500 -= entregar500
                billetes200 -= entregar200
                billetes100 -= entregar100
                billetes50 -= entregar50
                billetes20 -= entregar20

                print("\nRetiro exitoso! Se entregaron:")
                if entregar1000 > 0:
                    print(f"{entregar1000} billetes de $1000")
                if entregar500 > 0:
                    print(f"{entregar500} billetes de $500")
                if entregar200 > 0:
                    print(f"{entregar200} billetes de $200")
                if entregar100 > 0:
                    print(f"{entregar100} billetes de $100")
                if entregar50 > 0:
                    print(f"{entregar50} billetes de $50")
                if entregar20 > 0:
                    print(f"{entregar20} billetes de $20")
                
                print(f'Saldo actual: {montoRestante}')
            else:
                print('No hay billetes disponibles!')

    # Reiniciar variables temporales de entrega
    entregar1000 = entregar500 = entregar200 = entregar100 = entregar50 = entregar20 = 0
    entrada = input("Ingrese el monto a retirar (0 para salir): ")

print("HASTA LUEGO!")