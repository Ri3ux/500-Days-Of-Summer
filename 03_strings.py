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