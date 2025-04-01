"""
Las estructuras condicionales permiten ejecutar un bloque de código si se cumple una condición.
En Python, se utilizan las palabras clave if, elif y else para crear estructuras condicionales."
"""
# Ejemplo de una estructura condicional simple con varios if

x = 15
y = 20

if x > 10 and y > 25:
    print("X es mayor que 10 y Y es mayor que 15")

if x > 10 or y > 25:
    print("X es mayor que 10 o Y es mayor que 25")

if not x > 10:
    print("X no es mayor que 10")

# Ejemplo de una estructura condicional con if anidado

is_member = False
age = 15

if is_member:
    if age >= 15:
        print("Tienes acceso ya que eres miembro y tienes o eres mayor de 15 años")
    else:
        print("NO tienes acceso ya que eres miembro pero eres menor de 15 años")
else:
    print("No tienes acceso ya que no eres miembro")