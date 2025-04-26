# Las excepciones son una forma de manejar errores en Python, ya sea errores en nuestro código o errores del lado del usuario.

try:
    divisor = int(input("Ingresa un número divisor: "))
    result = 10 / divisor
    print(f"El resultado de la división es: {result}")
except ZeroDivisionError as e: #@ Almacena la excepción ZeroDivisionError en la variable e.
    print("Error: No se puede dividir entre cero.")
    print(f"Ha ocurrido un error: {e}")
except ValueError as e:
    print("Error: Debes ingresar un número entero.")
    print(f"Ha ocurrido un error: {e}")