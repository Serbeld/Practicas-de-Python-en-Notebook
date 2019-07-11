# encoding: utf-8 

# 4toCode.py

'''Este código hace parte de una serie de códigos utilizados 
para la práctica del lenguaje de programación Python'''

# Programador Sergio Luis Beleño Díaz
# 09.Julio.2019

# Acceder a las posiciones de una lista en Python

l = [1,"Dos",True,['Cuatro',5]]

l2 = l[3][0] # l2 = 'Cuatro'
print(l2)

# Selección de datos en una lista en Python

l3 = l[0:3:2] # l3 = [1,True]
print(l3)

l4 = l[1:4:2] # l4 = ['Dos', ['Cuatro', 5]]
print(l4)