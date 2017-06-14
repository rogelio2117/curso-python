lista = []
for i in range(4):
	    print("ingrese numeros", str(i + 1) + ": ", end="")
	    digitos =input()
	    lista += [digitos]
print("la lista creada es:", lista)
print("primer numero de lista", lista[0])
print("ultimo d ela lista", lista[3])