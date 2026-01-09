# Trabajo hecho por Aldahir Emmanuel Alonso Reyes, estudiante de Universidad Tecnológica de Emiliano Zapata de Morelos.
# Curso de Fundamentos de Programación de Python de Infotec.
# Unidad 4 - Ejercicio 1: Calculadora básica.

# Nombre de la clase.
class CalculadoraBásica:
    def __init__(self, numero1=0, numero2=0):
        # Atributos protegidos.
        self._numero1 = numero1
        self._numero2 = numero2
        self._historial = []

    # Getters y Setters para numero1
    @property
    def numero1(self):
        return self._numero1

    @numero1.setter
    def numero1(self, nuevo_numero1):
        if type(nuevo_numero1) in (int, float):
            self._numero1 = nuevo_numero1
        else:
            raise ValueError("Debe ser un número")

    # Getters y Setters para numero2
    @property
    def numero2(self):
        return self._numero2

    @numero2.setter
    def numero2(self, nuevo_numero2):
        if type(nuevo_numero2) in (int, float):
            self._numero2 = nuevo_numero2
        else:
            raise ValueError("Debe ser un número")

    # Funciones de operaciones sumar, restar, etc.
    def sumar(self):
        resultado = self._numero1 + self._numero2
        self._registrar_operacion('+', resultado)
        return resultado

    def restar(self):
        resultado = self._numero1 - self._numero2
        self._registrar_operacion('-', resultado)
        return resultado

    def multiplicar(self):
        resultado = self._numero1 * self._numero2
        self._registrar_operacion('*', resultado)
        return resultado

    def dividir(self):
        if self._numero2 == 0:
            raise ZeroDivisionError("No se puede dividir entre cero")
        resultado = self._numero1 / self._numero2
        self._registrar_operacion('/', resultado)
        return resultado

    # Gestión del historial
    def _registrar_operacion(self, operador, resultado):
        # Se guarda como diccionario
        self._historial.append({
            'operacion': f"{self._numero1} {operador} {self._numero2}",
            'resultado': resultado
        })

    def ver_historial(self):
        if not self._historial:
            print("No hay operaciones en el historial.")
            return

        print("\nHistorial")
        contador = 1
        for operacion in self._historial:
            # Uso de f-strings y acceso a llaves de diccionario
            print(f"{contador}. {operacion['operacion']} = {operacion['resultado']}")
            contador += 1


# Función interpretadora de expresiones
def interpretar_expresion(expresion):
    """Interpreta la expresión matemática ingresada"""
    for operador in ['+', '-', '*', '/']:
        if operador in expresion:
            partes = expresion.split(operador)
            if len(partes) == 2:
                # Convierte a float y elimina espacios
                num1 = float(partes[0].strip())
                num2 = float(partes[1].strip())
                return num1, num2, operador
    return None


# Programa principal
def main():
    calc = CalculadoraBásica()
    print("Bienvenido a Calculadora!")
    print("Escribe 'salir' para terminar o 'historial' para ver operaciones.\n")

    while True:
        entrada = input("Ingresa la operación: ")

        # Salir del programa
        if entrada.strip().lower() == "salir":
            print("¡Hasta pronto!")
            break

        # Consultar historial
        if entrada.strip().lower() == "historial":
            calc.ver_historial()
            continue

        # Procesar expresión
        resultado_interpretado = interpretar_expresion(entrada)
        if not resultado_interpretado:
            print("Expresión no válida.\n")
            continue

        num1, num2, operador = resultado_interpretado
        # Atributos usando setters
        calc.numero1 = num1
        calc.numero2 = num2

        # Ejecutar operación
        try:
            if operador == '+':
                print("Resultado:", calc.sumar())
            elif operador == '-':
                print("Resultado:", calc.restar())
            elif operador == '*':
                print("Resultado:", calc.multiplicar())
            elif operador == '/':
                print("Resultado:", calc.dividir())
        except Exception as e:
            print(f"Error: {e}")


# Método main que inicializa el programa.
if __name__ == "__main__":
    main()