### Strings ###

my_string = "Hello, World!"

print(len(my_string)) # Longitud de la cadena
print(my_string[0]) # Primer caracter
print(my_string[2:5]) # Slice de la cadena
print(my_string[:6]) # Slice desde el principio
print(my_string[7:]) # Slice hasta el final
print(my_string[-1]) # Último caracter
print(my_string[-6:]) # Slice desde el final

### Formateo de Cadenas ###

name = "Ricardo"
surname = "Estepa"
alias = "Rieux"
age = 35

print("Me llamo:", name, surname,". Mi alias es:", alias, ", y tengo ", age, " años.")
print("Me llamo: %s %s. Mi alias es: %s, y tengo %d años." % (name, surname, alias, age))
print("Me llamo: {} {}. Mi alias es: {}, y tengo {} años.".format(name, surname, alias, age))
print(f"Me llamo: {name} {surname}. Mi alias es: {alias}, y tengo {age} años.")

### Desenpaquetado de Cadenas ###
language = "rieux"
a, b, c, d, e = language
print(a, b)

### Reverse de Cadenas ###
print(language[::-1])

### Métodos de Cadenas ###
print(language.capitalize()) # Primera letra en mayúscula
print(language.upper()) # Mayúsculas
print(language.lower()) # Minúsculas
print(language.replace("r", "Q")) # Reemplazar
print(language.count("r")) # Contar

### Formateo de Números ###
pi = 3.14159
print("El valor de PI con tres decimales es: {:.3f}".format(pi)) # :.3f indica 3 decimales
print("El valor de PI con tres decimales es: %.4f" % pi) # %.4f indica 4 decimales
print(f"El valor de PI con tres decimales es: {pi:.2f}") # :.2f indica 2 decimales

### Secuencias de Escape ###
print("Hola\nMundo") # Salto de línea
print("Hola\tMundo") # Tabulador
print("Hola\\Mundo") # Barra invertida
print("Hola \"Mundo\"") # Se usa la secuencia de escape para evitar confusiones con la sintaxis de Python.
print("La ruta es: C:\\Users\\rieux\\Documents") # Se usa doble "\\" para evitar confusiones con la sintaxis de Python.
print(r"La ruta es: C:\Users\rieux\Documents") # Se usa la "r" antes de la cadena para indicar que es una cadena cruda.