# Trabajo hecho por Aldahir Emmanuel Alonso Reyes, estudiante de Universidad Tecnológica de Emiliano Zapata de Morelos.
# Curso de Fundamentos de Programación de Python de Infotec.
# Unidad 2 - Ejercicio 2: SistemaEvaluacion.

# Pedir número de alumnos y materias
num_alumnos = int(input("Ingrese el número de alumnos: "))
num_materias = int(input("Ingrese el número de materias: "))

for i in range(num_alumnos):
    print(f"\nAlumno {i + 1}")

    # Pedir nombre
    nombre = input("Nombre del alumno: ")
    while nombre.strip() == "":
        nombre = input("Ingrese el nombre del alumno valido: ")

    # Pedir matrícula
    matricula = input("Matrícula del alumno: ")
    while matricula.strip() == "":
        matricula = input("Ingrese una matrícula válida: ")

    aprobadas = 0
    reprobadas = 0

    # Pedir calificaciones
    for j in range(num_materias):
        calificacion = input(f"Calificación de la materia {j + 1}: ")

        while calificacion.strip() == "":
            calificacion = input("Ingrese una calificación válida!")

        calificacion = float(calificacion)

        if calificacion > 6:
            aprobadas += 1
        else:
            reprobadas += 1

    # Mostrar resultados
    print("\nReporte del alumno.")
    print("Nombre del alumno:", nombre)
    print("Matrícula:", matricula)
    print("Materias Aprobadas:", aprobadas)
    print("Materias Reprobadas:", reprobadas)