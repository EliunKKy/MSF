# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 15:09:31 2022

@author: Alexandre
"""

import numpy as np
import matplotlib.pyplot as plt

t0 = 0
tf = 4
x0 = 0
v0x = 0
g = 9.8
delta_t = 0.1
N=int((tf-t0)/(delta_t+0.1))
print("N =", N)

t = np.linspace(0,tf,N+1)
x = np.zeros(N+1)
vx = np.zeros(N+1)

t[0] = t0
x[0] = x0

for i in range(N):
    t[i+1] = t[i] + delta_t
    vx[i] = g * t[i]
    x[i+1] = x[i] + vx[i]*delta_t

#POSICAO EXATA
xExact = 1/2 * (g*(t**2))
plt.plot(t, xExact, label="Exact")

plt.plot(t, x, "x", label="Método de Euler")


##plt.plot(t, vx, label="v(t)")
plt.xlabel('Tempo (s)')
plt.ylabel('Posição (m)')
plt.title('Movimento Uniformemente Acelerado')
plt.legend()
plt.grid()
plt.show()

