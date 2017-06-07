variable_uno='hola'
variable_dos=1
variable_tres=2.3


#concatenacion

cadena = 'cadena uno' + 'cadena dos'

#interpolacion 
otra_cadena = 'hola{}'.format('un valor')
variable_cuatro = 'hola {0} {1}'.format('val','val2')
var = 'hola {variable1} {variable2}'.format(variable1='val',variable2='val2')

def mi_funcion(val):
	print('dentro de mi_funcion') # un comentario
	print(otra_cadena)
	print(variable_cuatro)
	print(var)


if __name__=='__main__':
	import argparse 
	parser=argparse.ArgumentParser()
	parser.add_argument('Nombre')
	parser.add_argument('Apellido')

	args = parser.parse_args()

	print (args.Nombre)
	print (args.Apellido)
	print (variable_cuatro.format(args.Nombre, args.Apellido))

	print ('hola mundo')
	mi_funcion(1)
