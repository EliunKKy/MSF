# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 23:58:49 2022

@author: Alexandre
"""

import numpy as np
import matplotlib.pyplot as plt

M = np.array([0.15, 0.20, 0.16, 0.11, 0.25, 0.32, 0.40, 0.45, 0.50, 0.55])
T = np.array([1.21, 1.40, 1.26, 1.05, 1.60, 1.78, 2.00, 2.11, 2.22, 2.33])

x = M
y = T**2


##Regressao linear
N = len(x)

xy = x*y
sumxy = xy.sum()
sumx = x.sum()
sumy = y.sum()

xx = np.square(x)
sumxx = xx.sum()
yy = np.square(y)
sumyy = yy.sum()


m = (N*sumxy - sumx*sumy)/(N*sumxx - (sumx)**2)
b = (sumxx*sumy - sumx*sumxy)/(N*sumxx - (sumx)**2)
r_num = (N * sumxy - sumx * sumy)**2
r_den  = (N * sumxx - (sumx)**2) * (N * sumyy - (sumy)**2)
r2 = r_num/r_den

m_erro = np.abs(m) * np.sqrt(((1/r2) - 1) / (N - 2))
b_erro = m_erro * np.sqrt(sumxx/N)


plt.plot(x, y, "X")
plt.plot(x, m*x+b, label="Reta Regressão T/M")


plt.xlabel("Massa (kg)")
plt.ylabel("Periodo (T**2)")
plt.grid()

print("m +/- m_erro = {:0.8f} +/- {:0.8f}".format(m,m_erro))
print("b +/- b_erro = {:0.8f} +/- {:0.8f}".format(b,b_erro))
print("r2 = {:0.8f}".format(r2))

#d)Colocando a expressão dada ao quadrado temos que o declive da reta é 4Pi^2/K