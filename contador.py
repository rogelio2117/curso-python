#dado el texto 'esto es una prueba' imprimir una cadena formateada de la siguiente manera 

#'esto es una prueba<nombre>'

#-imprimir cuantas letra 'e' tiene la cadena 
#-capitalizar la cadena 
#-imprimir longitud de la  cadena 
#- reemplazar en la cadena la letra 'o' por 0

dato = (input("Ingrese texto por favor: "))
texto = dato
contador = 0
for carac in texto:
    if carac == 'e':
        contador += 1
print (dato, "contiene", contador, "palabras.")

print ("capitalizacion:", texto.upper())
print ("la longitud de la cadena:", len(dato))
replace(o, 0)
print ("intercambio de la letra o por 0: ", dato.replace())
