# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 16:10:31 2022

@author: Alexandre
"""
######RESOLUCAO DO STOR

import numpy as np
import matplotlib.pyplot as plt

dt=0.01
tf=4.0
t0=0
x0=0
n=np.int((tf-t0)/dt+0.1)
print('n',n)

t=np.zeros(n+1)
x=np.zeros(n+1)
vx=np.zeros(n+1)

g=9.80
v0x=0
vx[0]=v0x
t[0]=t0
x[0]=x0
vx=g*t

for i in range(n): #Método de Euler
    t[i+1]=t[i]+dt
    vx[i] = g*t[i]
    x[i+1]=x[i]+vx[i]*dt

plt.plot(t,x)