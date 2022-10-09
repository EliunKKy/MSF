# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 16:01:42 2022

@author: rodri
"""

import matplotlib.pyplot as plt
import numpy as np

#import scipy as stats

y = np.array([10.07, 6.293, 3.831, 2.500, 1.409, 0.8775, 0.5369, 0.3522, 0.2173, 0.1357])
x = np.array([0, 5, 10, 15, 20, 25, 30, 35, 40, 45])
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

#regressão 

xmax= np.max(x)*1.1
xmin= np.min(x)*0.9
ymax= np.max(y)*1.1
ymin= np.min(y)*0.9
x1 = np.array([xmin,xmax])
yline = m*x1+b



plt.plot(x,y, "o", x1, yline)
plt.legend()
plt.grid()

