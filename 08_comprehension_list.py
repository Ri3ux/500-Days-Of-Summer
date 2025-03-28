"""
Las comprehension list son una forma de crear listas de forma más rápida y sencilla
que con un bucle for. Se pueden aplicar a listas, diccionarios y conjuntos.
"""
# Crear una lista con la segunda potencia de los números del 1 al 10
squares = [x**2 for x in range(1,11)]
print("La segunda potencia de los números del 1 al 10 es:", squares)

# Convertir una lista de grados Celsius a Fahrenheit
celsius = [0, 10, 20, 30, 40, 50]
farenheit = [((9/5)*temp + 32) for temp in celsius]
print("La temperatura en ºF es:", farenheit)

# Crear una lista con los números pares del 1 al 20
even_numbers = [x for x in range (1,21) if x%2 == 0]
print("Los números pares del 1 al 20 son:", even_numbers)

# Crear una matriz transpuesta
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

transpose = [[fila[i] for fila in matrix] for i in range(len(matrix))] # Se crea una lista con los elementos de la matriz transpuesta
print(matrix)
print(transpose)

# Crear una lista con las vocales de una palabra
word = "Murcielago"
vowels = [letter for letter in word if letter in "aeiou"]
print("Las vocales de la palabra", word, "son:", vowels)

# Crear una lista con el doble de los números
double = [x*2 for x in range (1, 11)]
print("El doble de los números del 1 al 10 es:", double)

# Crear una lista que filtre y transforme en mayúsculas los elementos de una lista
words = ["hola", "mundo", "python", "es", "genial"]
filtered = [letter.upper() for letter in words if len(letter) > 3]
print("Esta es una lista de palabras:", words)
print("Las palabras con más de 3 letras son:", filtered)

# Crear un diccionario con las claves y valores de una lista
claves = ["Nombre", "Edad", "Ocupación"]
valores = ["Ricardo", 35, "Ingeniero"]
dictionary = {claves[i]: valores[i] for i in range(len(claves))}
print("El diccionario es:", dictionary)

# Extraer una lista de nombres de personas que viven en Madrid y tienen más de 30 años
personas = [
    {"Nombre": "Juan", "Edad": 25, "Ciudad": "Madrid"},
    {"Nombre": "Ana", "Edad": 32, "Ciudad": "Madrid"},
    {"Nombre": "Pedro", "Edad": 35, "Ciudad": "Barcelona"},
    {"Nombre": "Laura", "Edad": 40, "Ciudad": "Madrid"}
]

madrid = [[persona["Nombre"]] for persona in personas if persona["Ciudad"] == "Madrid" and persona["Edad"] > 30] 
print("Las personas que viven en Madrid y tienen más de 30 años son:", madrid)

# Crear una lista multiplicando por 2 los números pares y dejar los impares como están
numbers = [x**2 if x%2 == 0 else x for x in range (1,11)]
print("La lista es:", numbers)