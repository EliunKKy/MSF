# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 17:45:52 2022

@author: Alexandre
"""

import numpy as np
import matplotlib.pyplot as plt
import sympy as sym
from numpy import block

t = sym.Symbol('t')
v = sym.Symbol('v')
vt = sym.Symbol('vt')
g = sym.Symbol('g')
D = sym.Symbol('D')
a = sym.Symbol('a')
aS = sym.Symbol('aS')

D = sym.Derivative(vt**2 / g*sym.log(sym.cosh(g/vt*t)), t, evaluate=True)
print('v', D)

v = sym.simplify(D)
print('v=', v)

t2 = np.arange(0,4,0.1)
vt2 = 6.80
g2=9.8

v2 = vt2 * np.tanh(g2*t2/vt2)

fig = plt.figure()
ax = fig.add_subplot(1,1,1)

ax.set_xlabel('tempo (s)')
ax.set_ylabel('v (m/s)')
ax.plot(t2, v2, label='Posição do Volante')
plt.legend()
