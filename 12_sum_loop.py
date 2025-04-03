# Se sumarán los números que el usuario ingrese. El bucle terminará en caso de que se ingrese un 0

suma = 0
print("¡Bienvenido! \nSumaremos los números que ingreses. Al ingresar un 0, terminaremos la suma.")
number = int(input("Ingresa un número para sumar (o 0 para salir): "))

while number != 0:
    suma += number
    number = int(input("Ingresa otro número para sumar (o 0 para salir): "))
print("Los números que ingresaste suman: ", suma)

