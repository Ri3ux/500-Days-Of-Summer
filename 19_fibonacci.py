def fibonacci(limit):
    a, b = 0, 1 # Inicializamos los dos primeros números de Fibonacci
    f = 1 # Contador para rastrear la posición en la secuencia
    while f <= limit: # Mientras no superemos el límite dado
        print(f"Fibonacci({f}) = ", end=" ") # Mostramos el número actual
        f += 1 # Incrementamos el contador
        yield b # Usamos `yield` para devolver el siguiente número de Fibonacci
        a, b = b, a + b # Actualizamos a y b para el siguiente número
limit = int(input("¿Hasta qué número quieres calcular el Fibonacci? "))
for num in fibonacci(limit):
    print(num) # Imprimimos los números de Fibonacci generados por el generador