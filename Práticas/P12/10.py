# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 16:40:46 2022

@author: Alexandre
"""

import matplotlib.pyplot as plt
import numpy as np

dt = 0.001
L = 1
angeq = 0
ang0 = 1/180*np.pi
g = 9.8

w0 = 0

t = np.arange(0,25+dt, dt)
w = np.zeros(t.size)
ang = np.zeros(t.size)
ang[0] = ang0
w[0] = w0
for k in range(t.size-1):
    alfa = -g/L * np.sin(ang[k])
    w[k+1] = w[k] + alfa * dt
    ang[k+1] = ang[k] + w[k+1]*dt

plt.plot(t, ang)
