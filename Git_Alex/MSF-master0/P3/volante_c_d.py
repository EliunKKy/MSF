# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 00:10:58 2022

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

a = sym.Derivative(D, t, evaluate=True)
print('ac=', a)
aS = sym.simplify(a)
print('ac=', a)

t2 = np.arange(0,4,0.1)
vt2 = 6.80
g2=9.8

ac = -g2*np.sinh(g2*t2/vt2)**2/np.cosh(g2*t2/vt2)**2 + g2

v2 = vt2 * np.tanh(g2*t2/vt2)

ac2 = g2 - g2/(vt2**2) * v2 * abs(v2)


fig = plt.figure()
ax = fig.add_subplot(1,1,1)

ax.set_xlabel('tempo (s)')
ax.set_ylabel('a (m/s2)')
ax.plot(t2, ac, label='Posição do Volante')
ax.plot(t2, ac2, label='Posição do Volante formula d)')
#como se pode ver, da a msm coisa
plt.legend()