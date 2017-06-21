import argparse


if __name__ == '__main__':
	parser= argparse.ArgumentParser('valor')
	parser.add_argument('Nombre')

	args = parser.parse_args()

	datos = {
	    'Nombre': {
	        'edad': 36,
	        'direccion': 'Managua' 
	    }
	}

    #args.nombre

    # si ana esta en datos
    #if args.nombre in datos:

        #print('la llave',args.nombre,'no existe en el diccionario')
	#else
        #print('la llave',args.nombre,'si existe en el diccionario')	
	if args.Nombre in datos:
	    print 'La llave {Nombre} existe en el diccionario'.format(Nombre=args.Nombre)		
	else:
	    print 'La llave {Nombre} no existe'.format(Nombre=args.Nombre)	

	#for llave,valor in datos.iteritems():
	#	print 'La llave es: ', llave, 'El valor es: ', valor
	#	if args.Nombre == llave :
	#	    print('La llave',args.Nombre,' existe en el diccionario')	
	#	else:
		   
	#		print('La llave',args.Nombre,'no existe en el diccionario')