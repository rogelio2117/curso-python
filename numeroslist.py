# crear 20 numeros aleaatorios entre el 0 y el 100 
#imprimir un alista de los numeros generados 
#ordenados ascendentemente, primero los pares y luegos los impares

#ejemplo: si los numeros generados son [4,3,5,6,2]
#el resultado sera: [2,4,6,3,5]

import random
listaA=[]
numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,95,74,65,35,81,54]
listapar=[]
listaimpar=[]
while len(numeros)>0:
	num = numeros.pop()
	if (num % 2 == 0):
		listapar.append(num)
	else:
		listaimpar.append(num)

for i in range(20):

	listaA.append(random.randint(0, 100))

print (listaA)
listaA.sort()
print ("orden ascendente")
print (listaA)
print ("numeros pares", )
print (listapar)
listapar.sort()
print ("orden ascendente de pares", listapar)
print ("numeros impares", )
print (listaimpar)
listaimpar.sort()
print ("orden ascendente de impares", listaimpar)
listaimpar
 #random.randrange(0,99) #genera numeros aleatorios, entre esos valores
