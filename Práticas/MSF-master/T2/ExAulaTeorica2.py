# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 16:19:09 2022

@author: Alexandre
"""

import matplotlib.pyplot as plt
import numpy as np
x = np.array([])
y = np.array([])

v=6.8
g=9.8
t=0
while t < 2.2:
    y = np.append(y, v**2/g*np.log(np.cosh(g*t/v)))
    x = np.append(x, t)
    t = t+0.1
plt.plot(x,y)