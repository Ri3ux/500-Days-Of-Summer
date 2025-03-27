### Listas ###
# Las listas son un tipo de dato que permite almacenar varios valores en una sola variable.
# Las listas son mutables, es decir, se pueden modificar.

to_do = ["Estudiar", "Trabajar", "Descansar", "Comer", "Dormir"]
print(to_do)

mix = ("Estudiar", 35, True, 3.14159, ["Python", "C++", "Java"])
print(mix)
print(len(mix))
print("Primer elemento de la lista:", mix[0])
print("Último elemento de la lista:", mix[-1])
print("Slice de la lista:", mix[2:5])

### Métodos de Listas ###
to_do.append("Correr") # Agregar un elemento al final de la lista
print(to_do)

to_do.insert(2, "Leer") # Agregar un elemento en una posición específica
print(to_do)

to_do.remove("Descansar") # Eliminar un elemento de la lista específico
print(to_do)

to_do.pop() # Eliminar el último elemento de la lista
print(to_do)

print(to_do.index("Comer")) # Encontrar la posición de un elemento en la lista

ages = [35, 25, 30, 40, 45, 50]
print("La mayor edad es:", max(ages)) # Encontrar el mayor valor de la lista
print("La menor edad es:", min(ages)) # Encontrar el menor valor de la lista

del ages[2] # Eliminar un elemento de la lista por su posición
print(ages)

del ages[-3:-1] # Eliminar un slice de la lista
print(ages)

"""
Hay que tener en cuenta que si asignamos una lista a otra variable,
estaremos asignando la dirección de memoria de la lista original a la nueva variable.
"""
a = [1, 2, 3, 4, 5]
b = a # Asigna todos los elementos de a en b, incluyendo la dirección de memoria
print(a)
print(b)
del a[0]
print(id(a)) # Muestra la dirección de memoria de la variable a
print(id(b)) # Muestra la dirección de memoria de la variable b

# Para copiar una lista sin asignar la dirección de memoria, se puede hacer lo siguiente:
c = a[:] # Copia todos los elementos de a en c, sin asignar la dirección de memoria
print(id(a))
print(id(c))

a.append(6)
print(a)
print(b)
print(c)