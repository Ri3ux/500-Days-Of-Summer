"""
Los diccionarios son una estructura de datos que permite almacenar pares de valores clave-valor.
Se puede acceder a los valores a través de la clave.
Los diccionarios se definen con llaves {} y los elementos se separan con comas."
"""

numbers = {"Uno": "One", "Dos": "Two", "Tres": "Three"}
print(numbers)
print(numbers["Tres"]) # La consulta se hace con la clave, en este caso "Tres"

profile = {"Nombre": "Ricardo", "Apellido": "Estepa", "Edad": 35, "Ciudad": "Bogotá"}
print(profile)
del profile["Ciudad"] # Se puede eliminar un elemento con la función del
print(profile)

print(profile.keys()) # Se pueden obtener las claves de un diccionario con la función keys()
print(profile.values()) # Se pueden obtener los valores de un diccionario con la función values()
print(profile.items()) # Se pueden obtener los elementos de un diccionario con la función items()

contacts = {"Ricardo":{"Apellido": "Estepa", "Edad": 35}, "Juan":{"Apellido": "Perez", "Edad": 25}}
print(contacts)
print(contacts["Ricardo"])
print(contacts["Juan"]["Edad"]) # Se puede acceder a un valor anidado con la clave correspondiente