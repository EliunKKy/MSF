# -*- coding: utf-8 -*-
"""
Created on Tue May  3 17:35:15 2022

@author: rodri
"""

import numpy as np

# variaveis 
v0 = 36.11
vt = 27.78
m = 0.057
g = -9.8
d = 0.67
alpha = 0.1745
x0 = -10
y0 = 1 

#velocidade
vx = v0 * np.cos(alpha)
vy = v0 * np.sin(alpha)
# intervalo
n = 100
dt = 0.1
t = np.zeros(n+1)

#arrays
x = np.zeros(n+1)
y = np.zeros(n+1)
ax = np.zeros(n+1)
ay = np.zeros(n+1)

# forças
P = m*g
Fres = -(0.47/2)*(np.pi*(d/2)**2)*1.2754*np.abs(v0)*v0

# força resultante 
Fr = P + Fres
Fr_x = Fr * np.cos(alpha)
Fr_y = Fr * np.sin(alpha)

for i in range(n):
    t[i+1]=t[i]+dt
    r=np.sqrt(x[i]**2+y[i]**2)
    ax[i]=-gm/r**3*x[i]
    ay[i]=-gm/r**3*y[i]
    vx[i+1]=vx[i]+ax[i]*dt
    vy[i+1]=vy[i]+ay[i]*dt
    x[i+1]=x[i]+vx[i+1]*dt
    y[i+1]=y[i]+vy[i+1]*dt 
