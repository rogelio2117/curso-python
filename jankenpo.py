##crear el juego de piedra papel y tijera 
#-usar while
#-diccionario 
#-argsparse
#la app debera solicitar al usuario un valor 'piedra', 'papel' o 'tijera'
#la appp debera de generar un valor aleatorio de entre piedra papel o tijera 
#el app debera imprimir el resultado de cada mano 
#la app debera imprimir el ganador entre maquina y el usuario (el que gane tres rondas)
#si es empate nadie gana puntos y se realiza otra ronda##/

print (input("BIENVENIDO" "AL JUEGO DE PIEDRA, PAPEL O TIJERA"))

import random
import sis

empate = 0
ganado = 0
perdido = 0

def elige(x):
 	return {
 	    '1':'piedra',
 	    '2':'papel',
 	    '3':'tijeras',
 	    '0':'cancelar',

 	}.get(x, 'papel')

def eligeopcion():
	print("presione 1 para elegir piedra")
	print("presione 2  para elegir papel")
	print("presione 3 para elegir tijeras")
	print("presione 0 para cancelar")
	print("")

	eleccion = input("¿Que opcion elijes?")

	resultado = elige(eleccion)

	if resultado == 'salir':
		print("")
		sis.exit("saliendo del juego......")
	else:
		return resultado

def sistemaeleccion():
	opciones = ["piedra", "papel", "tijeras"]
	opcioaleatoria  = random,randit(0,2)
	return  opciones[opcionaleatoria]

def comparacion(jugador, sistema):
	opcioaleatoria  = random,randit(0,2)
	return  opciones[opcionaleatoria]


	if jugador == sistema:
		return "empate"
	if jugador == "piedra" and sistema == "papel":
		return "sistema"
	if jugador == "papel" and sistema == "tijeras":
		return "sistema"
	if jugador == "tijeras" and sistema == "piedras":
		return "sistema"
	else:
		return "jugador"

while true:
		jugador = eligeopcion()
		sistema = sistemaeleccion()
		print ("")
		print ("tu eleccion", jugador)
		print ("eleccion de sistema", sistema)

		resultado = comparacion(jugador, sistema)

		if resultado == "empate":
			empate += 1

			if empate <= 1:
				print("has empatado")
			else:
				print("has empatado", + str(empate)+ 'veces')

		elif resultado == "sistema"
			perdido += 1
			if perdido <= 1:
				print("has perdido")
			else:
				print("has perdido" + str(perdido)"veces")

		else:
			ganado += 1
			if ganado <= 1:
				print("has ganado")
			else:
				print("has ganado" + str(ganado)"veces")

		print("")
