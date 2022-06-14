# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 17:56:48 2022

@author: Alexandre 107849
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.array([0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5])
y = np.array([0.1, 1.4, 1.7, 6.5, 7.7, 10.4, 19.5, 26.1, 26.5, 45.9, 52.5])

x = x**2

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


plt.plot(x, y, "o")
plt.plot(x, m*x+b, label="Regressão linear")


plt.xlabel("t**2 (s)")
plt.ylabel("s(m)")
plt.grid()
plt.legend()

print("m +/- m_erro = {:0.8f} +/- {:0.8f}".format(m,m_erro))
print("b +/- b_erro = {:0.8f} +/- {:0.8f}".format(b,b_erro))
print("r2 = {:0.8f}".format(r2))