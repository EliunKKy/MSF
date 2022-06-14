import matplotlib.pyplot as plt
import numpy as np

# listas de valores 
y = np.array([0.00, 0.735, 1.363, 1.739, 2.805, 3.814, 4.458, 4.955, 5.666, 6.329])
x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

# sumatórios
xy=x*y
xx=np.square(x)
yy=np.square(y)

Sum_x=np.sum(x)
Sum_y=np.sum(y)
Sum_xy=np.sum(xy)
Sum_xx=np.sum(xx)
Sum_yy=np.sum(yy)
n=len(x)


# declive, ordenada na origem ...
m = (n*Sum_xy-Sum_x*Sum_y)/(n*Sum_xx-Sum_x**2)
b = (Sum_xx*Sum_y-Sum_x*Sum_xy)/(n*Sum_xx-Sum_x*Sum_x)
r2 = np.square(n*Sum_xy-Sum_x*Sum_y)/((n*Sum_xx-Sum_x*Sum_x)*(n*Sum_yy-Sum_y*Sum_y))
r = np.sqrt(r2)
delta_m = np.abs(m)*np.sqrt((1/r2-1)/(n-2))
delta_b = delta_m*np.sqrt(Sum_xx/n)


# velocidade média
h = (np.max(x)-np.min(x))/60
vm = (np.max(y)-np.min(y))/h


# reta de aproximação
xmax = np.max(x)*1.1
xmin = np.min(x)*0.9
ymax = np.max(y)*1.1
ymin = np.min(y)*0.9
x1 = np.array([xmin,xmax])
yline = m*x1+b

z = np.polyfit(x, y, 1)

# gráficor
fig1, ax = plt.subplots(1, 3, figsize=(21,11), layout="constrained")
ax[0].plot(x,y,"o")
ax[0].set_xlim([xmin,xmax])
ax[0].set_ylim([ymin,ymax])

ax[1].plot(x,y,"o",x1,yline)
ax[1].set_xlim([xmin,xmax])
ax[1].set_ylim([ymin,ymax])

ax[2].plot(x,y,"o",z)
ax[2].set_xlim([xmin,xmax])
ax[2].set_ylim([ymin,ymax])
