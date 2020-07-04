# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Se importan las librerias

# Se lee el archivo CSV con la libreria pandas
Archivo = pd.read_csv('k.csv')

#imprime el nombre de las columnas
names = Archivo.columns[:]
print(names)

# Se leen los valores de voltaje y tiempo en nanosegundos
voltajes = Archivo['Unnamed: 0'].values
tiempo = Archivo['Unnamed: 3'].values

# Se toman los primeros 7940 datos
voltajes = voltajes[0:7940]
tiempo = tiempo[0:7940]

# Se toman vectores de inicializacion
picosdevoltaje = []
tiempodeplotinicial = []
tiempodeplot = []

# Inicia el intervalo de la toma de datos a plotear en cero
puntoinicio = 0

# Contador auxiliar
contador = 0

# Contador de pulsos obtenidos
pulsos = 0

# Lista auxiliar
listaactual = []

# Almacena en tiempodeplotincial todos los valores de tiempo encontrados
for i in range(0, len(tiempo)):
    if str(tiempo[i]) != 'nan':
        tiempodeplotinicial.append(int(tiempo[i]))

# Almacena todos los valores de voltaje encontrados
for i in range(0, len(voltajes)):
    if voltajes[i] != '#':
        picosdevoltaje.append((voltajes[i]))
        contador = contador + 1

        # cuenta el numero de pulsos que se dan cada 12 valores de voltaje
        if contador == 12:
            pulsos = pulsos + 1

    else:
        contador = 0

for i in range(0, pulsos):
    listaactual = np.linspace(puntoinicio, int(tiempodeplotinicial[i]), num=12)
    puntoinicio = int(tiempodeplotinicial[i])
    tiempodeplot.extend(listaactual)

#Convierte la fecha

#pip install datetime
from datetime import datetime
#Fecha
fecha = 1558162800

textodelafecha = str(datetime.utcfromtimestamp(fecha).strftime('%Y-%m-%d'))

print(textodelafecha)

# Se extrae un tiempo de plot
tiempodeploteado = tiempodeplot[0:len(tiempodeplot)]
voltajeploteado = picosdevoltaje[0:len(picosdevoltaje)]

# Graficar
plt.figure(1, figsize=[7.4, 6])
plt.plot(tiempodeploteado, voltajeploteado, 'b', linewidth=1)
plt.xlabel("Tiempo (nS)", fontsize='xx-large')
plt.ylabel("Voltaje (V)", fontsize='xx-large')
plt.title("Serie de tiempo", fontsize='xx-large')
plt.legend([textodelafecha], fontsize='x-large')
plt.grid(color='b', ls='-.', lw=0.2)

plt.savefig("SeriedeTiempo.png", bbox_inches='tight')

plt.show()

# Se extrae un tiempo de plot
npuntos = 1000
tiempodeploteado = tiempodeplot[0:int(npuntos)]
voltajeploteado = picosdevoltaje[0:int(npuntos)]

# Graficar
plt.figure(2, figsize=[7.4, 6])
plt.plot(tiempodeploteado, voltajeploteado, 'b', linewidth=2)
plt.xlabel("Tiempo (nS)", fontsize='xx-large')
plt.ylabel("Voltaje (V)", fontsize='xx-large')
plt.title("Serie de tiempo", fontsize='xx-large')
plt.legend([textodelafecha], fontsize='x-large')
plt.grid(color='b', ls='-.', lw=0.2)

plt.savefig("SeriedeTiempo_1000_Datos.png", bbox_inches='tight')

plt.show()

# Se extrae un tiempo de plot
npuntos = 100
tiempodeploteado = tiempodeplot[0:int(npuntos)]
voltajeploteado = picosdevoltaje[0:int(npuntos)]

# Graficar
plt.figure(3, figsize=[7.4, 6])
plt.plot(tiempodeploteado, voltajeploteado, 'b', linewidth=3)
plt.xlabel("Tiempo (nS)", fontsize='xx-large')
plt.ylabel("Voltaje (V)", fontsize='xx-large')
plt.title("Serie de tiempo", fontsize='xx-large')
plt.legend([textodelafecha], fontsize='x-large')
plt.grid(color='b', ls='-.', lw=0.2)

plt.savefig("SeriedeTiempo_100_Datos.png", bbox_inches='tight')

plt.show()