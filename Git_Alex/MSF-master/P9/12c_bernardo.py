# -*- coding: utf-8 -*-
"""
Created on Mon May 23 17:37:00 2022

@author: Alexandre
"""

import matplotlib.pyplot as plt
import numpy as np

dt = 0.001

t = np.arange(0,4000+dt,dt)

ax = np.zeros(t.size)
vx = np.zeros(t.size)
x = np.zeros(t.size)

Cyu = 0.1
Cres = 0.9
area = 2.34
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