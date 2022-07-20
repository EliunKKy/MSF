# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 16:44:03 2022

@author: Alexandre
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 50, 5)
y = np.array([9.676 , 6.355, 4.261, 2.729, 1.862, 1.184, 0.7680, 0.4883, 0.3461, 0.2119])


y = np.log(y) ###passar a um grafico semi-log


###REGRESSAO LINEAR
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

print(r2)

plt.plot(x, y, "o", label="Pontos")
plt.plot(x, m*x+b, label="Reta de regressao linear")
plt.xlabel("Tempo (dias)")
plt.ylabel("Atividade (mCi)")
plt.legend()
plt.title("Gráfico semilog")
plt.show()

##b) num grafico semilog a atividade é inversamente proporcional ao tempo
