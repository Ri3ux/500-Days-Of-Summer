"""
FOR:
Se utiliza cuando se conoce de antemano el número de iteraciones o
cuando se desea recorrer una secuencia (como una lista, rango, cadena, etc.).
La estructura del ciclo for incluye un iterador que avanza automáticamente en cada iteración.

WHILE:
Se utiliza cuando no se sabe cuántas veces se repetirá el ciclo,
pero se tiene una condición que debe cumplirse para continuar iterando.
La condición se evalúa antes de cada iteración, y el ciclo continúa mientras la condición sea verdadera.
"""

numbers = [1, 2, 3, 4, 5, 6]
for i in numbers: # i representa cada valor de la lista "numbers"
    print("Aqui i es igual a: ", i)

for i in range(5,11): # Itera desde el número 5 hasta el número 10
    print("El valor de i es: ", i)

fruits = ["Manzana", "Pera", "Naranja", "Pomelo"]
for fruta in fruits:
    print(fruta)
    if fruta == "Naranja":
        print("Hemos encontrado la naranja en la posición: ", fruits.index(fruta))

x = 0
while x < 5:
    print(x)
    x += 1

x = 0
while x < 5:
    x += 1 # Incrementa en 1 el valor de x en cada bucle
    if x == 3:
        break # Termina el bucle por completo. Cuando se ejecuta, el programa sale inmediatamente del bucle, sin importar si quedan iteraciones pendientes.
    print(x) # Se imprimirá el valor de x hasta que se cumpla alguna de las condiciones

x = 0
while x < 5:
    x += 1 # Incrementa en 1 el valor de x en cada bucle
    if x == 3:
        continue # Termina el bucle por completo. Cuando se ejecuta, el programa sale inmediatamente del bucle, sin importar si quedan iteraciones pendientes.
    print(x) # Se imprimirá el valor de x hasta que se cumpla alguna de las condiciones


items = ["Zapato", "Pantalón", "Gorra", "Amuleto"]
for item in items:
    if item == "Pantalón":
        continue # Salta a la siguiente iteración del bucle, omitiendo el resto del código en la iteración actual, pero sin salir del bucle.
    print(item)

for i in range(11):
    if i % 2 != 0:
        continue
    print(i) # Imprime los números pares (descartó a los que tienen módulo diferente de 0)