# Programa que determina si un numero es positivo o negativo.

numero = int(input('Digite un numero: '))

if numero > 0:
    print(f'El numero {numero} es positivo.')
elif numero < 0:
    print(f'El numero {numero} es negativo.')
else:
    print(f'El numero {numero} es cero.')