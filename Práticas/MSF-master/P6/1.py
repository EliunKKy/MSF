# -*- coding: utf-8 -*-
"""
Created on Mon May  2 16:32:06 2022

@author: Alexandre
"""

import matplotlib.pyplot as plt
import numpy as np


v0 = 100/3.6
angle = 10/180*np.pi
v0x = v0*np.cos(angle)
v0y = v0*np.sin(angle)
vt = 100/3.6
g = -9.8
x0 = 0
y0 = 0
dt = 0.001


##d)

t = np.arange(0,100, dt)
x = np.zeros(t.size)
y = np.zeros(t.size)
vx = np.zeros(t.size)
vy = np.zeros(t.size)


x[0] = x0
y[0] = y0
vx[0] = v0x
vy[0] = v0y

#metodo de Euler
for i in range(0, t.size-1):
    vx[i+1] = vx[i]# velocidade no instante
    vy[i+1] = vy[i] + g*dt # velocidade no instante
    x[i+1] = x[i] + vx[i] * dt # posiçao no instante
    y[i+1] = y[i] + vy[i] * dt # posiçao no instante
    if y[i+1] < 0:
        break

t = t[:i+2]
x = x[:i+2]
y = y[:i+2]
vx = vx[:i+2]
vy = vy[:i+2]


plt.plot(x,y, label = "Sem Res")


##e)


t1 = np.arange(0,100, dt)
y1 = np.zeros(t.size)
x1 = np.zeros(t.size)
vx1 = np.zeros(t.size)
vy1 = np.zeros(t.size)


x1[0] = x0
y1[0] = y0
vx1[0] = v0x
vy1[0] = v0y
D = -g/(vt**2)

for i in range(0, t1.size-1):
    v = np.sqrt(vx1[i]**2 + vy1[i]**2)
    ax = -D*vx1[i]*abs(v)
    ay = g-D*vy1[i]*abs(v)
    
    vx1[i+1] = vx1[i] + ax*dt# velocidade no instante
    vy1[i+1] = vy1[i] + ay*dt # velocidade no instante
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

plt.legend()
plt.grid()

## f) e g)

print("Sem resistencia")
taltmax =t[np.where(y == np.max(y))][0]
print("alt max: " + str(np.max(y)) + " Tempo -> " + str(taltmax))
talc = t[np.where(x == x[-2])][0]
print("alcance: " + str(x[-2]) + " Tempo -> " + str(talc))

print("\n Com resistencia")
taltmax1 =t[np.where(y1 == np.max(y1))][0]
print("alt max: " + str(np.max(y1)) + " Tempo -> " + str(taltmax1))
talc1 = t1[np.where(x1 == x1[-2])][0]
print("alcance: " + str(x1[-2]) + " Tempo -> " + str(talc1))

