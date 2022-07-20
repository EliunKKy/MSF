# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 18:17:53 2022

@author: Alexandre
"""

import matplotlib.pyplot as plt
import numpy as np

dt = 0.001
x = np.arange(-5,5,dt)

xeq = 2
k = 1
Ep = 0.5*k*(abs(x)-xeq)**2

plt.plot(x,Ep)

##b) ele vai oscilar harmonicamente a volta da posicao de equilibrio quer de um lado como de outro

t = np.arange(0,10, dt)
ax = np.zeros(t.size)
vx = np.zeros(t.size)
x = np.zeros(t.size)


for i in range(t.size-1):
    vx[i+1] = vx[i] + ax[i]*dt
    x[i+1] = x[i] + vx[i+1]*dt