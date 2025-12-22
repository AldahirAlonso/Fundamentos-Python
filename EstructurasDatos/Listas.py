# Introduccion a listas
from traceback import print_tb

var = [5, 'Marzo', True]
print(var)
print(var[1])

numbers = [10, 5, 7, 2, 1]
print("\n", numbers)

numbers[0] = 111
print("\n", numbers)

numbers[1] = numbers[4]
print("\n", numbers)

# Accediendo al contenido de una lista
print("\n Accediento al contenido de una lista")
numbers = [10, 5, 7, 2, 1]
print(numbers)
print(numbers[0])
print(len(numbers))

# Funcion len
print("\nFuncion len")
print(numbers)
numbers = [10, 5, 7, 2, 1, 8, 15, 33, 45]
print(len(numbers))
print(numbers[8])

# Eliminando elementos de una lista
print("\n Eliminar Elementos con DEL")
numbers = [10, 5, 7, 2, 1]
print(numbers)
print("\n Eliminando Elementos Con DEL")
del numbers[1]
print(numbers)

# Indice negativo
print("\nIndice negativo")
numbers = [10, 5, 7, 2, 1]
print(numbers[-1])
print(numbers[-2])
print(numbers[-5])
print(numbers[-3])
print(numbers[-4])

# Agregar elementos a una lista: append()
print("\nAgregar Elementos con APPEND()")
numbers = [10, 5, 7, 2, 1]
print(numbers)
print("Agregamos Un Elemento Con APPEND()")
numbers.append(4)
print(numbers)

# Agregar elementos a una lista: insert()
print("\nAgregar Elementos Con INSERT()")
numbers = [10, 5, 7, 2, 1]
print(numbers)
print("Agregamos Un Elemento Con INSERT()")
numbers.insert(1, 222)
print(numbers)

# Agregar elementos a una lista: (cont.)
print("\nAgregar Elementos Con Cont")
myList = []
for i in range(5):
    myList.append(i + 1)
print(myList)

# Hacer uso de listas
# Calcular la suma de todos los valores almacenados en la lista myList.
print("\nHacer uso de listas.")
myList = [10, 1, 8, 3, 5]
acum = 0
for i in range(len(myList)):
    acum += myList[i]
    print(acum)

# Ordenar una lista con sort()
print("\nOrdenar una lista con SORT().")
print("Lista desordenada.")
myList = [8, 10, 6, 2, 4]
print(myList)
print("\nLista ordenada.")
myList.sort()
print(myList)

# Invertir una lista con reverse()
print("\nInvertir una lista con reverse")
print("Lista desordenada")
lst = [5, 3, 1, 2, 4]
print(lst)
print("Lista ordenada como espejo")
lst.reverse()
print(lst)