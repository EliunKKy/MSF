# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 21:07:41 2022

@author: Alexandre
"""

import matplotlib.pyplot as plt
import numpy as np

vi = 10 # m/s
dt = 0.001
vt = 27.7778
g = -9.8

T = np.arange(0,2.2+dt, dt)
v = np.zeros(T.size)
y = np.zeros(T.size)

v[0] = 10
    
y1 = 10.0*T + 0.5*g*T**2

# aceleraçao inicial

D = -g/(vt**2)

floor = np.zeros(T.size)

for i in range(0, T.size-1):
        v[i+1] = v[i] + (g-D*v[i]*abs(v[i]))*dt # velocidade no instante
        y[i+1] = y[i] + v[i] * dt # posiçao no instante


fig = plt.figure()
ax = fig.add_subplot(1,1,1)

ax.set_xlabel('tempo (s)')
ax.set_ylabel('X (m)')
ax.plot(T, floor, label="Y = 0")
ax.plot(T, y, label="Metodo de Euler")
ax.plot(T, y1, label="Exato")

plt.legend()
