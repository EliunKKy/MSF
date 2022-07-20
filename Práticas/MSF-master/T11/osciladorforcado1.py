# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 22:43:19 2022

@author: Alexandre
"""

import matplotlib.pyplot as plt
import numpy as np

dt = 0.001

t = np.arange(0, 100+dt,dt)
k = 1
m = 1
omega = np.sqrt(k/m)
b = 0.01
F0 = 2
omegaf = 1



v1 = np.zeros(t.size)
x1 = np.zeros(t.size)

f = np.zeros(t.size)

x1[0] = 4
v1[0] = 0

for i in range(t.size-1):
    f[i] =  -k * x1[i] - b*v1[i]
    a = f[i]/m
    v1[i+1] = v1[i] + a*dt
    x1[i+1] = x1[i] + v1[i+1]*dt


plt.plot(t,x1, label="amortecido")
plt.xlabel("tempo")
plt.ylabel("x(m)")
#ax[1].plot(t,x1)

for i in range(t.size-1):
    f[i] =  -k * x1[i] + F0*np.cos(omegaf * t[i])
    a = f[i]/m
    v1[i+1] = v1[i] + a*dt
    x1[i+1] = x1[i] + v1[i+1]*dt

plt.plot(t,x1, label="forçado")
plt.xlabel("tempo")
plt.ylabel("x(m)")
#ax[1].plot(t,x1)
plt.legend()
plt.xlim([0,100])
plt.ylim([-20,20])