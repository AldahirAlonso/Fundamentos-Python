# Trabajo hecho por Aldahir Emmanuel Alonso Reyes, estudiante de Universidad Tecnológica de Emiliano Zapata de Morelos.
# Curso de Fundamentos de Programación de Python de Infotec.
# Unidad 1 - Ejercicio 2: Inicio de Sesion.

# Declaracion de variables.
# Datos del usuario.
usuario_correcto = "admin"
contrasena_correcta = "1234"
intentos = 3

# Mensaje de bienvenida.
print("======Sistema de inicio de sesión======")
print(f'Intentos restantes: {intentos}')

# Solicitud de datos al usuario.
print("Usuario:", end=' ')
usuario = input()
print("Contraseña:", end=' ')
contrasena = input()

# Ciclo while para validar los datos ingresados.
# El ciclo se repite mientras los datos sean incorrectos y aun queden intentos.
while (usuario != usuario_correcto or contrasena != contrasena_correcta) and intentos > 1:
    intentos -= 1
    print("Datos incorrectos. Por favor, inténtalo de nuevo.")
    print(f'Intentos restantes: {intentos}')
    print("Usuario:", end=' ')
    usuario = input()
    print("Contraseña:", end=' ')
    contrasena = input()
# Verificacion final de los datos ingresados.
if usuario == usuario_correcto and contrasena == contrasena_correcta:
    print("Inicio de sesión exitoso!")
else:
    print("Acceso bloqueado.")