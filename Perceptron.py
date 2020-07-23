#Perceptron.py

import numpy as np

#Inicialización de los pesos de la neurona
w = np.array([0.5, -0.5, 0.8])

#Tasa de aprendizaje
ta = 0.9

#entradas = np.array([ Patrón 1,  Patrón 2,  Patrón 3, Patrón 4])
entradas =  np.array([[0, 0, 1], [0, 1, 1], [1, 0, 1], [1, 1, 1]])
salida =    np.array([ 0,         1,         1,         1       ])

######################################################################
######################################################################
for epocas in range(2):

	print("Época actual: " + str(epocas))

	for patron in range(len(entradas)):

		#Sumatoria entre la multiplicación de los pesos y las entradas
		sumatoria = np.dot(w, entradas[patron])
		
		#Función de activación umbral
		if (sumatoria > 0):
			salida_obtenida = 1
		else:
			salida_obtenida = 0

		#Error
		error = ta * (salida[patron] - salida_obtenida)

		#Multiplicación entre las entradas y el error
		add = error * entradas[patron]

		#Ajuste de los pesos
		w = w + add

		print(w)

print("Evaluando los pesos en las entradas")

for patron in range(len(entradas)):

	#Sumatoria entre la multiplicación de los pesos y las entradas
	sumatoria = np.dot(w, entradas[patron])
		
	#Función de activación umbral
	if (sumatoria > 0):
		salida_obtenida = 1
	else:
		salida_obtenida = 0

	print(salida_obtenida)