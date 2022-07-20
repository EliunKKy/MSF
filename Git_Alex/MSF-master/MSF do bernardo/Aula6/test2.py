# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 19:58:50 2022

@author: draki
"""

import matplotlib.pyplot as plt
import numpy as np

dt = 0.01
angle = 15/180*np.pi
g1 = -9.8
t1 = np.arange(0,10+dt, dt)
y1 = np.zeros(t1.size)
x1 = np.zeros(t1.size)
vx1 = np.zeros(t1.size)
vy1 = np.zeros(t1.size)
v0 = 230/3.6

D1 = -g1/(6.8)**2
y1[0] = 2.5
vx1[0] = v0*np.cos(angle)
vy1[0] = v0*np.sin(angle)

#ax = 0
#ay = g

for i in range(t1.size-1):
    v1 = np.sqrt(vx1[i]**2 + vy1[i]**2)
    ax1 = -D1*v1*vx1[i]
    ay1 = g1-D1*v1*vy1[i]
    vx1[i+1] = vx1[i] + ax1 * dt
    vy1[i+1] = vy1[i] + ay1 * dt
    x1[i+1] = x1[i] + vx1[i] * dt
    y1[i+1] = y1[i]+ vy1[i] * dt
    if y1[i+1] < 0:
        break

t1 = t1[:i+2]
x1 = x1[:i+2]
y1 = y1[:i+2]
vx1 = vx1[:i+2]
vy1 = vy1[:i+2]

plt.plot(x1,y1)