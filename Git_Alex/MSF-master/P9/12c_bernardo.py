# -*- coding: utf-8 -*-
"""
Created on Mon May 23 17:37:00 2022

@author: Alexandre
"""

import matplotlib.pyplot as plt
import numpy as np

dt = 0.001

t = np.arange(0,200+dt,dt)

ax = np.zeros(t.size)
vx = np.zeros(t.size)
x = np.zeros(t.size)

Cyu = 0.1
Cres = 0.9
area = 2.34
Par = 1.225
m = 1500
cv = 283
Potencia = cv*735.4975
vx[0] = 1
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

h = 3*3600
ponto = x[h]
velocidade = vx[h]

xinverted = x[-1:-50:-1]
plt.plot(t,x, label="pos")

plt.plot(t,vx, label="velocity")
plt.legend()
print(t[-1])
plt.grid()