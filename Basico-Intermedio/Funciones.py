# encoding: utf-8 

# 7moCode.py

'''Este código hace parte de una serie de códigos utilizados 
para la práctica del lenguaje de programación Python'''

# Programador Sergio Luis Beleño Díaz
# 12.Julio.2019

def Funcion_de_ejemplo(num1,num2 = 4):
	suma = num1 + num2
	return(suma)


Suma1 = Funcion_de_ejemplo(3,4)
Suma2 = Funcion_de_ejemplo(3)

print(Suma1)
print(Suma2)