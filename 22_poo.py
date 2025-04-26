"""
La programación orientada a objetos (POO) es un paradigma de programación que utiliza "objetos" para representar datos y métodos. En POO, una clase es una plantilla para crear o instanciar objetos. Cada objeto tiene atributos (propiedades) y métodos (funciones) que definen su comportamiento. La POO permite organizar el código de manera más estructurada y reutilizable.
"""
# En este ejemplo, definimos una clase llamada Person que representa a una persona. La clase tiene un constructor que inicializa el nombre y la edad de la persona. También tiene un método greet que imprime un saludo personalizado.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        print(f"¡Hola, {self.name}! Tienes {self.age} años.")

persona_1 = Person("Juan", 30)
persona_2 = Person("Ana", 25)

persona_1.greet()
persona_2.greet()