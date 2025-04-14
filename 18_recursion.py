# La recursividad es una técnica de programación en la que una función se llama a sí misma para resolver un problema.
# Es útil para problemas que pueden dividirse en subproblemas más pequeños y similares. La recursividad se basa en dos conceptos clave: el caso base y la llamada recursiva.

# Factorial y sumarial son ejemplos clásicos de problemas que se resuleven mediante recursividad.
def factorial (n):
    # Caso base: si n es 0 o 1, el factorial es 1
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1) #* Llamada recursiva: n! = n * (n-1)!

number = int(input("Ingresa un número para calcular su factorial: "))
print(f"El factorial de {number} es: {factorial(number)}\n") #? La función factorial se llama a sí misma con un valor decreciente de n hasta que alcanza el caso base (0 o 1).

def sumarial (n):
    # Caso base: si n es 0, la suma es 0
    if n == 0:
        return 0
    else:
        return n + sumarial(n - 1) #* Llamada recursiva: suma = n + suma(n-1)

number = int(input("Ingresa un número para calcular su sumarial: "))
print(f"El sumarial de {number} es: {sumarial(number)}\n")

# Fibonacci es otro ejemplo clásico de recursividad. La serie de Fibonacci es una secuencia en la que cada número es la suma de los dos anteriores.

def fibonacci(n):
    # Caso base: si n es 0, el resultado es 0; si n es 1, el resultado es 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

number = int(input("Ingresa el número de la serie de Fibonacci: "))
print(f"El {number}º de Fibonacci es: {fibonacci(number)}\n") #? La función fibonacci se llama a sí misma con un valor decreciente de n hasta que alcanza los casos base (0 o 1).