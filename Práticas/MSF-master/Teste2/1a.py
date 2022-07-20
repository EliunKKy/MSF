# -*- coding: utf-8 -*-
"""
Created on Fri Jun  3 11:57:34 2022

@author: Alexandre
"""


import matplotlib.pyplot as plt
import numpy as np



v0 = 140/3.6
angle = 7/180*np.pi
v0x = v0*np.cos(angle)
v0y = v0*np.sin(angle)
vt = 100/3.6
g = 9.8
x0 = 0
y0 = 0
dt = 0.001

##e)

t1 = np.arange(0,100, dt)
y1 = np.zeros(t1.size)
x1 = np.zeros(t1.size)
vx1 = np.zeros(t1.size)
vy1 = np.zeros(t1.size)


x1[0] = x0
y1[0] = y0
vx1[0] = v0x
vy1[0] = v0y
D = g/(vt**2)

for i in range(0, t1.size-1):
    v = np.sqrt(vx1[i]**2 + vy1[i]**2)
    ax1 = -D*vx1[i]*abs(v)
    ay1 = -g-D*vy1[i]*abs(v)
    vx1[i+1] = vx1[i] + ax1 * dt # velocidade no instante
    vy1[i+1] = vy1[i] + ay1 * dt # velocidade no instante
    x1[i+1] = x1[i] + vx1[i] * dt # posiçao no instante
    y1[i+1] = y1[i] + vy1[i] * dt # posiçao no instante
    if y1[i+1] < 0:
        break

t1 = t1[:i+2]
x1 = x1[:i+2]
y1 = y1[:i+2]
vx1 = vx1[:i+2]
vy1 = vy1[:i+2]

plt.plot(x1,y1, label="Com Res")
plt.xlabel("x (m)")
plt.ylabel("y (m)")

print("\n Com resistencia")
talc1 = t1[np.where(x1 == x1[-2])][0]
print("alcance: " + str(x1[-2]) + " Tempo -> " + str(talc1))


plt.grid()
plt.legend()