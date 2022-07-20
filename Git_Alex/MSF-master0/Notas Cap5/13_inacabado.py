# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 02:47:17 2022

@author: Alexandre
"""

import matplotlib.pyplot as plt
import numpy as np

dt = 0.01
t = np.arange(0,500+dt,dt)

ax = np.zeros(t.size)
vx = np.zeros(t.size)
x = np.zeros(t.size)

u = 0.004
Cres = 0.9
area = 0.3
Par = 1.225
m = 75
Potencia = 294.20
vx[0] = 1
g = 9.8
P = m * g
N = P * np.cos(np.pi*(5/180))

for i in range(t.size-1):
    Fcic = Potencia/vx[i]
    FRes = -(Cres/2)*area*Par*vx[i]**2
    FRol = -u*abs(N)
    F = Fcic + FRes + FRol - P * np.sin(np.pi*(5/180))
    
    ax[i] = F/m
    vx[i+1] = vx[i] + ax[i]*dt
    x[i+1] = x[i] + vx[i]*dt

plt.plot(t,vx, label="velocity")

plt.grid()

print("Vel Terminal: " + str(vx[-1]))


print("Tempo que demora a percorrer 2km: ", end="")
for i in range(x.size-1):
    if(x[i] == 2000):
        print(t[np.where(x == x[i])])
        break;
    elif(x[i] > 2000):
        t1 = t[np.where(x == x[i])]
        t2 = t[np.where(x == x[i-1])]
        tmed = (t1+t2)/2
        print(tmed)
        break;

plt.legend()