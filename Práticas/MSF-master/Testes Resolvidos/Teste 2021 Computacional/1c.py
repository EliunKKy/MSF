# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 16:22:18 2022

@author: Alexandre
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.array([0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5])
y = np.array([0.121, 0.997, 2.55, 6.09, 9.31, 15.8, 17.1, 25.5, 26.5, 38.8, 41.9])

x = x**1.948
y = y


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


plt.xlabel("s (m)")
plt.ylabel("t (s)")
plt.grid()

print("m +/- m_erro = {:0.8f} +/- {:0.8f}".format(m, m_erro))
print("b +/- b_erro = {:0.8f} +/- {:0.8f}".format(b, b_erro))
print("r2 = {:0.8f}".format(r2))