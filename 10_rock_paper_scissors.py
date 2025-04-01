"""
Es es un ejemplo de un juego de piedra, papel o tijera.
El juego consiste en que dos jugadores eligen entre piedra, papel o tijera.
El ganador se determina de la siguiente manera:
- Piedra vence a tijera
- Tijera vence a papel
- Papel vence a piedra
- Si ambos jugadores eligen la misma opción, es un empate.

El programa solicita a los jugadores que ingresen su elección y luego determina el ganador.
"""
import random # Importamos la librería random para generar opciones aleatorias

# Se solicita el nombre del jugador
player_name = input("¿Cuál es tu nombre? ")
print(f"Hola, {player_name} ¡Bienvenido al juego de Piedra-🪨, Papel-📄 o Tijera-✂!")
print("Recuerda que: Piedra vence a Tijera, Tijera vence a Papel y Papel vence a Piedra")
print("¡Buena suerte!")

options = {"piedra": "🪨", "papel": "📄", "tijera": "✂"}

# Se solicita al jugador que elija una opción
while True:
	player = input("Elige una opción entre Piedra, Papel o Tijera: ").lower()
	if player in options.keys():
		break
	print("Opción no válida. Por favor, elige entre Piedra, Papel o Tijera.")


# Se elige una opción aleatoria para la computadora

computer = random.choice(list(options.keys()))
print("La computadora eligió: " + options[computer])

if player == computer:
    print("¡Es un empate!")
elif (player == "piedra" and computer =="tijera") or \
     (player == "tijera" and computer =="papel") or \
     (player == "papel" and computer =="piedra"):
    print(f"¡Ganaste, {player_name}!")
else:
    print(f"¡Perdiste, {player_name}!")

print("Gracias por jugar, ¡hasta la próxima!")