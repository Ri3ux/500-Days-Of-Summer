# Las matrices son un tipo de dato que permite almacenar varios valores en una sola variable.
# Las matrices son mutables, es decir, se pueden modificar.
# Las matrices son un conjunto de listas de igual longitud.
# Las matrices se pueden representar como una lista de listas.

"""
Las matrices son un tipo de dato que permite almacenar varios valores en una sola variable.
Las matrices son mutables, es decir, se pueden modificar.
Las matrices son un conjunto de listas de igual longitud.
Las matrices se pueden representar como una lista de listas.
"""

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # Las matrices se declaran con corchetes
print(matrix)
print(type(matrix))
print(matrix[1]) # Imprime la segunda lista de la matriz

super_matrix = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
print(type(super_matrix))
print(super_matrix[1][0][1]) # Imprime el segundo elemento de la primera lista de la segunda lista de la tupla, es decir, 6


"""
Las tuplas son un tipo de dato que permite almacenar varios valores en una sola variable.
Las tuplas son inmutables, es decir, no se pueden modificar.
Las tuplas se pueden representar como una lista de tuplas.
"""

tupla = (1, 2, 3, 4, 5) # Las tuplas se declaran con paréntesis
print(type(tupla))
print(tupla)
print(tupla[2]) # Imprime el tercer elemento de la tupla