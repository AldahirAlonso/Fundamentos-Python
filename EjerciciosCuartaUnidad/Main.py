# Trabajo hecho por Aldahir Emmanuel Alonso Reyes, estudiante de Universidad Tecnológica de Emiliano Zapata de Morelos.
# Curso de Fundamentos de Programación de Python de Infotec.
# Unidad 4 - Proyecto Final: Desarrollo de un script.

# Heredar calculadora
from calculadora import Calculadora

# Funcion para reconocer el símbolo ^
def interpretar_expresion(expresion):
    for operador in ['+', '-', '*', '/', '^']:
        if operador in expresion:
            partes = expresion.split(operador)
            try:
                # Soporta múltiples valores
                valores = [float(p.strip()) for p in partes]
                return valores, operador
            except ValueError:
                return None
    return None

def main():
    calc = Calculadora()
    print("Bienvenido a la Calculadora Avanzada.")

    while True:
        entrada = input("\nOperación: ").strip().lower()

        if entrada == "salir":
            print("¡Hasta pronto!")
            break

        if entrada == "historial":
            calc.ver_historial()
            continue

        resultado_int = interpretar_expresion(entrada)
        if not resultado_int:
            print("Formato inválido.")
            continue

        lista_nums, operador = resultado_int
        calc.valores = lista_nums  # Asignación mediante setter

        try:
            # Excepcion de operación
            if operador == '+':
                print("Resultado:", calc.sumar())
            elif operador == '-':
                print("Resultado:", calc.restar())
            elif operador == '*':
                print("Resultado:", calc.multiplicar())
            elif operador == '/':
                print("Resultado:", calc.dividir())
            elif operador == '^':  # Funcionalidad de potencia
                print("Resultado:", calc.potencia())
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()