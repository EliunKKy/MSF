# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 01:45:06 2022

@author: Alexandre
"""

from maxminv import maxminv
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import find_peaks

dt = 0.001 
t = np.arange(0, 1200+dt,dt)
g = 9.8
m = 1
x = np.zeros(t.size)
v = np.zeros(t.size)
Vforca = 1
F0 = 7.5
b = 0.05
k = 1

v[0] = -4
x[0] = -2

for i in range(t.size-1):
    a = (-k*x[i]-b*v[i]+F0*np.cos(Vforca*t[i]))/m
    v[i+1] = v[i] + a*dt
    x[i+1] = x[i] + v[i+1]*dt
    
Em = 0.5*k*x**2+0.5*m*v**2
plt.plot(t,Em)
plt.ylabel("En Mecanica")
plt.xlabel("t(s)")
print(Em[-1])