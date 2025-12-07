# Programa que determina si eres un ni;o, adolescente o adulto.

edad = int(input("Dime tu edad: "))
if edad >= 18:
    print(f'Eres mayor de edad, tienes {edad}')
elif edad >= 14:
    print(f'Eres un adolescente, tienes {edad}')
else:
    print(f'Eres un niño, tienes {edad}')