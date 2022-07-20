# -*- coding: utf-8 -*-
"""
Created on Tue May 31 01:29:40 2022

@author: Alexandre
"""

import matplotlib.pyplot as plt
import numpy as np

#Constantes
g = 9.8
m = 0.45
r = 0.11
PAr = 1.225
vt = 100/3.6
dt = 0.01

t = np.arange(0, 5+dt, dt)

A = np.pi*(r)**2
D = g / vt**2
mag = 0.5*A*PAr*r

Rx = np.zeros(t.size)
Ry = np.zeros(t.size)
Rz = np.zeros(t.size)

Vx = np.zeros(t.size)
Vy = np.zeros(t.size)
Vz = np.zeros(t.size)


Rx[0] = 0
Ry[0] = 0
Rz[0] = 23.8

Vx[0] = 25
Vy[0] = 5
Vz[0] = -50

Wx = 0
Wy = 400
Wz = 0

#metodo de Euler
for i in range(0, t.size-1):
    v = np.sqrt(Vx[i]**2+Vy[i]**2+Vz[i]**2)
    
    #Consoante a rotacao -> mudar isto
    amagx = mag * Wy * Vz[i] / m
    amagy = 0
    amagz = -mag * Wy * Vx[i] / m
    
    #ha de estar certo para os casos gerais
    ax = -D * Vx[i] * abs(v) + amagx
    ay = - g - D * Vy[i] * abs(v) + amagy
    az = -D * Vz[i] * abs(v) + amagz
    
    Vx[i+1] = Vx[i] + ax * dt
    Vy[i+1] = Vy[i] + ay * dt
    Vz[i+1] = Vz[i] + az * dt
    
    Rx[i+1] = Rx[i] + Vx[i] *dt
    Ry[i+1] = Ry[i] + Vy[i] * dt
    Rz[i+1] = Rz[i] + Vz[i] * dt
    


indice = np.argmax(Ry)
y_max = np.max(Ry)
t_ymax = t[indice]
print("Y Maximo:", y_max)
print("Alcance: ",Rx[-2])

plt.plot(t,Rx, label="x(t)")
plt.plot(t,Ry, label="y(t)")
plt.plot(t,Rz, label="z(t)")
plt.xlim([0,1])
plt.ylim([-5,25])
plt.legend()
plt.grid()
plt.show()

##dos 4 aos 5s as condicoes coincidem