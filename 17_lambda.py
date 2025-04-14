# Las funciones lamba son funciones anónimas, es decir, no tienen nombre.
# Se utilizan para crear funciones pequeñas y rápidas que se pueden usar en una sola línea de código.
# Se definen con la palabra clave lambda, seguida de los argumentos de entrada, dos puntos y la expresión que se va a evaluar.

add = lambda a, b: a + b
print("El resultado de la suma es", add(2, 4))

multiply = lambda a, b: a * b
print("El resultado de la multiplicación es", multiply(2, 4))

# Si queremos aplicar una función lambda a una lista, podemos usar la función map.
# La función map aplica una función a cada elemento de una lista y devuelve una nueva lista con los resultados.

numbers = range(0, 11)
squared_numbers = list(map(lambda x: x ** 2, numbers))
print("Los números al cuadrado del rango [0-10] son:", squared_numbers)

# También podemos usar la función filter para filtrar elementos de una lista según una condición.
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Los números pares del rango [0-10] son:", even_numbers)