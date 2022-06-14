# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 15:48:11 2022

@author: rodri
"""

import numpy as np
import matplotlib.pyplot as plt

# Int tempo
dt = 0.0001
t = np.arange(0,40+dt, dt)

# Cons
m = 1
k = 1
kder = 0.5
Axeq = 1.0
Bxeq = 1.2

# Arrays pos
Ax = np.zeros(t.size)
Bx = np.zeros(t.size)

# Arrays vel
Av = np.zeros(t.size)
Bv = np.zeros(t.size)

# pos iniciais
Ax[0] = Axeq + 0.05
Bx[0] = Bxeq


# Euler-Cromer 
for i in range(t.size-1):
    Aacc = (-k*(Ax[i]-Axeq)-kder*((Ax[i]-Axeq)-(Bx[i]-Bxeq)))/m
    Bacc = (-k*(Bx[i]-Bxeq)+kder*((Ax[i]-Axeq)-(Bx[i]-Bxeq)))/m
    
    Av[i+1] = Av[i] + Aacc*dt
    Bv[i+1] = Bv[i] + Bacc*dt
    
    Ax[i+1] = Ax[i] + Av[i+1]*dt
    Bx[i+1] = Bx[i] + Bv[i+1]*dt


plt.plot(t,Ax, label = "A", color = "red")
plt.plot(t,Bx, label = "B", color = "blue")
plt.legend()
plt.grid()