"""
Un iterador es un objeto que implementa los métodos especiales __iter__() y __next__().
Esto permite recorrer sus elementos uno a uno utilizando un bucle for o la función next().

Características:

- Es un objeto que sabe cómo producir el siguiente valor de una secuencia.
- Se utiliza para iterar sobre estructuras de datos como listas, tuplas, diccionarios, etc.
- Cuando no hay más elementos, lanza una excepción StopIteration.
"""

# Crear un iterador elementos de una lista

lista = [1, 2, 3, 4] #Creamos la lista
iterador = iter(lista) #Creamos un iterador para la lista
print(next(iterador)) #Next itera entre cada elemento de la cadena. Se imprime 1.
print(next(iterador)) #Se imprime 2.
print(next(iterador)) #Se imprime 3.
print(next(iterador)) #Se imprime 4.
# print(next(iterador)) #Detienen la iteración porque ya no quedan elementos en memoria.

# Crear un iterador para los caracteres de una cadena de texto

text = "Ridiculus suspendisse ligula" #Creamos una cadena
iterador = iter(text) #Creamos un iterador para la cadena
for word in iterador: #Por cada caracter que esté en el iterador, imprimimos cada valor/caracter
    print(word)

# Crear un iterador para los números impares, con el número 10 como límite

limit = 10 #Creamos la variable con el límite.
odd_iter = iter(range(1, limit + 1, 2)) #Creamos el iterador. El rango inicia en 1 hasta 11 y con incrementos de 2.
for number in odd_iter: #Por cada entero que esté en el iterador, imprimimos cada entero del rango 1, 3, 5, 7, 9
    print(number)