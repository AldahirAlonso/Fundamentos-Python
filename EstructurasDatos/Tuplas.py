# Ejemplo de tupla usando dos puntos usando rebanada :

myTuple = (1, 10, 100, 1000)

print(myTuple[0])
print(myTuple[-1])
print(myTuple[1:])
print(myTuple[:-1])
print(myTuple[:3])

print(myTuple[1:3])

# Como usar una tupla
print("\nComo usar una tupla.")
myTuple = (1, 10, 100)
t1 = myTuple + (1000, 10000)
t2 = myTuple * 3

print(len(t2))
print(t1)
print(t2)
print(10 in myTuple)
print(-10 not in myTuple)