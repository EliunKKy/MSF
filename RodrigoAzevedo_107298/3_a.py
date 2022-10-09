# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 16:42:43 2022

@author: rodri
"""

import matplotlib.pyplot as plt
import numpy as np

dt = 0.001

t = np.arange(0,4000+dt,dt)

ax = np.zeros(t.size)
vx = np.zeros(t.size)
x = np.zeros(t.size)

Cyu = 0.001
Cres = 0.9
area = 15.2256
Par = 1.225
m = 200000
Potencia = 7000000 
vx[0] = 0.5
g = 9.8

for i in range(t.size-1):
    Fcic = Potencia/vx[i]
    FRes = Cres/2*area*Par*vx[i]**2+Cyu*m*g
    F = Fcic - FRes
    ax[i] = F/m  
    vx[i+1] = vx[i] + ax[i]*dt
    x[i+1] = x[i] + vx[i]*dt
    if(x[i]>=2000):
        break;
        
        
t = t[:i]
x = x[:i]
ax = ax[:i]
vx = vx[:i]

h = 2*3600
ponto = x[h]
velocidade = vx[h]

xinverted = x[-1:-50:-1]
plt.plot(x,t, label="pos")

plt.plot(t,vx, label="velocity")
plt.legend()
plt.grid()


Vt = 0.5 * Cyu * area * vx[0]**2 * Par