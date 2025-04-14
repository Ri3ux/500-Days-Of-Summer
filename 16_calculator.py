# Definimos las funciones para cada operación
def add(a, b):
    return a + b

def substract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def calculator():
    while True:
        print("¿Qué operación deseas realizar?")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("0. Salir")

        option = int(input("Ingresa una opción [1-2-3-4-0]: "))
        operation = {1: "Suma", 2: "Resta", 3: "Multiplicación", 4: "División"}
        if option == 0:
            print("Saliendo...")
            break
        if option in [1, 2, 3, 4]:
            print(f"Haremos una {operation[option]}\n") #* Busca en el diccionario el valor de la opción elegida.
            a = float(input ("Ingresa el primer número: "))
            b = float(input ("Ingresa el segundo número: "))
            if option == 1:
                print("La summa es ", add(a, b), "\n")
            elif option == 2:
                print("La resta es ", substract(a, b), "\n")
            elif option == 3:
                print("La multiplicación es ", multiply(a, b), "\n")
            elif option == 4:
                print ("La división es ", divide(a, b), "\n")
        else:
            print("Opción no válida. Elige una opción válida [1-2-3-4-0]")
calculator()
        
