# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 19:54:02 2022

@author: Alexandre
"""

import numpy as np
import matplotlib.pyplot as plt


v0 = 7.07106781187 # cos(45) * 10 m/s
g = 9.8
vt = 20 # já feita a convesão para m/s
vy = 10
t0 = 0
tf = 15
x0 = 2.5

delta_t = 0.001
N=int((tf-t0)/(delta_t))
print("N =", N)

D = g / (vt**2)
a = g - D * vy * abs(vy)

t = np.linspace(0,tf,N+1)
x = np.zeros(N+1)
vx = np.zeros(N+1)

t[0] = t0
x[0] = x0

for i in range(N):
    vx[i+1] = vx[i] + g*delta_t
    x[i+1] = x[i] + vx[i]*delta_t



plt.plot(t, x)