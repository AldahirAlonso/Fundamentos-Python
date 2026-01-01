# Trabajo hecho por Aldahir Emmanuel Alonso Reyes, estudiante de Universidad Tecnológica de Emiliano Zapata de Morelos.
# Curso de Fundamentos de Programación de Python de Infotec.
# Unidad 2 - Ejercicio 1: Calculadora de edad.

from datetime import date

# Pedir fecha de nacimiento.
fecha_nacimiento = input("Ingrese su fecha de nacimiento (DD-MM-AAAA): ")

# Solicitar campos vacíos.
if fecha_nacimiento.strip() == "":
    print("Llene todos los campos.")
else:
    try:
        # Separar la fecha en día, mes y año.
        dia, mes, anio = map(int, fecha_nacimiento.split("-"))

        # Validar fecha ingresada.
        if anio <= 1900:
            print("El año debe ser mayor a 1900!")
        elif mes < 1 or mes > 12:
            print("Mes inválido")
        elif dia < 1 or dia > 31:
            print("Día inválido")
        else:
            # Crear fecha de nacimiento.
            nacimiento = date(anio, mes, dia)
            hoy = date.today()

            # Calcular edad en años.
            edad = hoy.year - nacimiento.year

            # Verificar si ya cumplió años.
            if (hoy.month, hoy.day) < (nacimiento.month, nacimiento.day):
                edad -= 1

            print(f"Tienes: {edad} años")

    except ValueError:
        print("Fecha incorrecta!")
