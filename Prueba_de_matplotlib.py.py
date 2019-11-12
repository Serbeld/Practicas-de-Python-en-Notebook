# Prueba_de_matplotlib.py

# Programador Sergio Luis Beleño Díaz
# 29.Octubre.2019

import numpy as np
import matplotlib.pyplot as plt

lista = [['0','1',"2",'3','4','5',6],['7',"8.5",'9','10',"11",'12','13'],['14','15','16','17','18',"19","20"],]
lista = np.array(lista)
print(lista[:,1])
Data = lista[:,1]

plt.plot(Data)
plt.show()

Data = np.append(Data,24)
print(Data)
plt.plot(Data)
plt.show()

Data = np.delete(Data,0)
print(Data)
plt.plot(Data)
plt.show()
