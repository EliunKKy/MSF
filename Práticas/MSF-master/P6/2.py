# -*- coding: utf-8 -*-
"""
Created on Tue May 24 18:51:45 2022

@author: Alexandre
"""

import matplotlib.pyplot as plt
import numpy as np

dt = 0.01
t = np.arange(0, 0.5+dt, dt)
t0 = 0
m = 0.45
r = 0.11
A = np.pi*(r)**2
PAr = 1.225
g = 9.8
vt = 100/3.6
D = g/(vt**2)
mag = 0.5*A*PAr*r



Rx = np.zeros(t.size)
Ry = np.zeros(t.size)
Rz = np.zeros(t.size)

Vx = np.zeros(t.size)
Vy = np.zeros(t.size)
Vz = np.zeros(t.size)

Rz[0] = 23.8

Vx[0] = 25
Vy[0] = 5
Vz[0] = -50

Wy = 400

for i in range(0,t.size-1):
    v = np.sqrt(Vx[i]**2+Vy[i]**2+Vz[i]**2)
    
    amagx = mag * Wy * Vz[i] / m
    amagz = - mag * Wy * Vx[i] / m
    
    ax = -D * Vx[i] * abs(v) + amagx
    ay = -g - D * Vy[i] * abs(v)
    az = -D * Vz[i] * abs(v) + amagz
    
    Vx[i+1] = Vx[i] + ax * dt
    Vy[i+1] = Vy[i] + ay * dt
    Vz[i+1] = Vz[i] + az * dt
    
    Rx[i+1] = Rx[i] + Vx[i] *dt
    Ry[i+1] = Ry[i] + Vy[i] * dt
    Rz[i+1] = Rz[i] + Vz[i] * dt


plt.plot(t, Rx, label="x(t)")
plt.plot(t, Ry, label="y(t)")
plt.plot(t, Rz, label="z(t)")
plt.legend()
plt.grid()