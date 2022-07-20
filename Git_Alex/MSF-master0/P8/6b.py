# -*- coding: utf-8 -*-
"""
Created on Sat May 28 18:29:52 2022

@author: Alexandre
"""

import matplotlib.pyplot as plt
import numpy as np

dt = 0.01
m = 1
k = 1
w = np.sqrt(k/m)
t = np.arange(0,18,dt)
A = 4
O = 0

x0 = 4
v0x = 0

x = np.zeros(t.size)
vx = np.zeros(t.size)

x[0] = x0
vx[0] = v0x

va = -A*w*np.sin(w*t+O)

#metodo de Euler-Cromer
for i in range(0, t.size-1):
    ax = -k/m * x[i]
    vx[i+1] = vx[i] + ax * dt
    x[i+1] = x[i] + vx[i+1] *dt
    

#plt.ylim([-5,5])
plt.xlim([0,17.5])
plt.plot(t,vx, "x", label = "NUMERICO")
plt.plot(t, va, label = "ANALITICO")

plt.grid()
plt.legend()
