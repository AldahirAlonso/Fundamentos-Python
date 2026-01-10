# Trabajo hecho por Aldahir Emmanuel Alonso Reyes, estudiante de Universidad Tecnológica de Emiliano Zapata de Morelos.
# Curso de Fundamentos de Programación de Python de Infotec.
# Unidad 4 - Proyecto Final: Desarrollo de un script.

class Calculadora:
    def __init__(self):
        # Usamos una lista flexible para múltiples valores
        self._valores = []
        self._historial = []

    @property
    def valores(self):
        return self._valores

    @valores.setter
    def valores(self, nueva_lista):
        if all(isinstance(x, (int, float)) for x in nueva_lista):
            self._valores = nueva_lista
        else:
            raise ValueError("Todos los elementos deben ser numéricos")

    # Operaciones
    def sumar(self):
        resultado = sum(self._valores)
        self._registrar_operacion('+', resultado)
        return resultado

    def restar(self):
        resultado = self._valores[0] - sum(self._valores[1:])
        self._registrar_operacion('-', resultado)
        return resultado

    def multiplicar(self):
        resultado = 1
        for v in self._valores:
            resultado *= v
        self._registrar_operacion('*', resultado)
        return resultado

    def dividir(self):
        resultado = self._valores[0]
        for v in self._valores[1:]:
            if v == 0:
                raise ZeroDivisionError("División entre cero detectada")
            resultado /= v
        self._registrar_operacion('/', resultado)
        return resultado

    # Nuevo método de potencia
    def potencia(self):
        # Eleva el primer número a la potencia del segundo
        resultado = self._valores[0] ** self._valores[1]
        self._registrar_operacion('^', resultado)
        return resultado

    def _registrar_operacion(self, operador, resultado):
        # Registro de diccionario
        expresion = f" {operador} ".join(map(str, self._valores))
        self._historial.append({
            'operacion': expresion,
            'resultado': resultado
        })

    def ver_historial(self):
        if not self._historial:
            print("No hay operaciones registradas.")
            return
        print("\n--- Historial de Operaciones ---")
        for i, op in enumerate(self._historial, 1):
            print(f"{i}. {op['operacion']} = {op['resultado']}")