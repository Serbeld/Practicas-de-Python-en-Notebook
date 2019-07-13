# -*- coding: utf-8 -*-
# Reloj de 24 Hrs python 2.7

import time

horas = 0
minutos = 0
segundos = 0

for i in range(0, 24):
    horas = i
    for j in range(0, 60):
        minutos = j
        for k in range(0, 60):
        	segundos = k
        	time.sleep(0.99)
        	print(('%02d' % horas) + ":" + ('%02d' % minutos) + ":" + ('%02d' % segundos) )