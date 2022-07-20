# -*- coding: utf-8 -*-
"""
Created on Fri Jun  3 12:35:40 2022

@author: Alexandre
"""

import matplotlib.pyplot as plt
import numpy as np


dt = 0.0001
t = np.arange(0,100,dt)

y0= 2.5
v0 = 10
angle = 45/180*np.pi
v0x = v0*np.cos(angle)
v0y = v0*np.sin(angle)
vt = 72/3.6
g = 9.8

D = g/vt**2


t = np.arange(0,100, dt)
x = np.zeros(t.size)
y = np.zeros(t.size)
vx = np.zeros(t.size)
vy = np.zeros(t.size)

vx[0] = v0x
vy[0] = v0y
y[0] = y0

#metodo de Euler
for i in range(0, t.size-1):
    v = np.sqrt(vx[i]**2+vy[i]**2)
    ax = -D * vx[i] * v
    ay = -g - D * vy[i] * v
   
    
    vx[i+1] = vx[i] + ax * dt # velocidade no instante
    vy[i+1] = vy[i] + ay * dt # velocidade no instante
    x[i+1] = x[i] + vx[i] * dt # posiçao no instante
    y[i+1] = y[i] + vy[i] * dt # posiçao no instante
    if y[i+1] < 0:
            break
        
t = t[:i+2]
x = x[:i+2]
y = y[:i+2]
vx = vx[:i+2]
vy = vy[:i+2]
plt.plot(x,y)
plt.grid()
print(x[-1])
print('Cai no chao a {:.2f} metros aos {:.2f} seg'.format(float(x[-1]), float(t[-1])))