# Definimos una función sin argumentos
def greet():
    print("Hola mundo")
greet()

# Definimos una función con un argumento
def greet(name):
    print(f"Hola {name}")
greet("Rick")

# Definimos una función con varios argumentos
def greet(name, lastname):
    print(f"Hola {name} {lastname}")
greet("Rick", "Sánchez")

# Definimos una función con varios argumentos y un valor predeterminado
def greet(name, lastname="Sánchez"):
    print(f"Hola {name} {lastname}")
greet("Rick")