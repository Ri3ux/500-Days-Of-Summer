"""
Un generador es un tipo especial de iterador que se define mediante una función que
utiliza la palabra clave yield. Cada vez que se llama a yield, la función "pausa" su estado
y puede reanudarse más tarde desde donde se quedó.

Características:

- Son más eficientes en memoria porque no almacenan toda la secuencia en memoria; generan los valores bajo demanda.
- Se utilizan para producir secuencias grandes o infinitas.
- No necesitan implementar manualmente __iter__() y __next__(); Python lo hace automáticamente.
"""

def generator(): #Definimos la función 'generator'
    yield 1 #Retorna el valor de 1 cuando se invoca la función 'generator'
    yield 2
    yield 3

for number in generator():
    print(number)

# Crear una función que genere los números de fibonacci con un límite.

def fibonacci(limit):
    a, b = 0 , 1 #Es lo mismo que tener a = 0 b = 1
    while a <= limit:
        yield a
        a, b = b, a + b

for numero in fibonacci(15):
    print(numero)

# Crear una función que genere una secuencia con incrementos de 2, y reciba como parámetro el inicio y el límite

def even_number(init, limit):
    a = init
    while init < limit and a < limit:
        yield a
        a += 2

for even in even_number(3, 15):
    print(even)