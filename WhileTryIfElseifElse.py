respuesta = "si"
numero = 0
print ("Inicio")
while respuesta == 'si':

	#Error se muestra una sola vez
	try:
		numero = int(input("\nDigite un numero: "))
	except ValueError:
		print("\nError\n")
		numero = int(input("\nDigite un numero: "))	


	if numero > 0:
		print("\nEl numero ingresado es positivo\n")
	elif numero < 0:
		print("\nEl numero ingresado es negativo\n")
	else:
		print("\nEl numero ingresado es igual a cero\n")
	respuesta = (input("¿Desea continuar? < si - no>    ")) 
	while respuesta != 'no' and respuesta != 'si':
		print("\nError por favor digite denuevo su respuesta en minuscula\n")
		respuesta = (input("¿Desea continuar? < si - no>    ")) 
print("\nSaliste")