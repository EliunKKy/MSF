# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 21:29:59 2022

@author: rodri
"""

import numpy as np
import matplotlib.pyplot as plt

dt=0.00001
tf=1.00
n=np.int(tf/dt+0.1)

t=np.linspace(0,tf,n)


g=9.80      # m/s**2
vt=100*1000/3600  # m/s
vel0=100*1000/3600  # m/s
theta=10*np.pi/180  # rad
v0x=vel0*np.cos(theta)
v0y=vel0*np.sin(theta)
x0=0
y0=0


vy=np.empty(n)
y=np.empty(n)
vx=np.empty(n)
x=np.empty(n)
ax=np.empty(n)
ay=np.empty(n)
vx[0]=v0x
vy[0]=v0y
x[0]=x0
y[0]=y0
D = g/vt**2

for i in range(0,n-1):
    vv=np.sqrt(vx[i]**2+vy[i]**2)
    ax[i]=-D*vv*vx[i]
    ay[i]=-D*vv*vy[i]-g
    vx[i+1]=vx[i]+ax[i]*dt
    vy[i+1]=vy[i]+ay[i]*dt
    x[i+1]=x[i]+vx[i]*dt
    y[i+1]=y[i]+vy[i]*dt
    

xs=x0+v0x*t
ys=y0+v0y*t-0.5*g*t**2

fig, ax1 = plt.subplots(1)
ax1.set_xlabel( 'x(t) (m)' )
ax1.set_ylabel( 'y(t) (m)' )
ax1.plot(xs,ys,label='sem resistência')
ax1.plot(x,y,'-',label='com resistência')

ax1.set_ylim(0, 1.3*ys.max())
plt.legend()
plt.show()


# f) H máx e instante coreespondente (c/ e s/ res ar)

t_max_sem_resistencia = np.round(np.unique(t[y==y.max()])[0],4)
y_max_sem_resistencia = np.round(y.max(),4)
t_max_com_resistencia = np.round(np.unique(t[y==y.max()])[0],4)
y_max_com_resistencia = np.round(y.max(),4)

print("EULER: A altura máxima atingida pelo bola tendo em consideração a resistência do ar é: {} m ao fim de {}s".format(y_max_com_resistencia,t_max_com_resistencia))
print("EULER: A altura máxima atingida pelo bola sem resistência do ar é: {} m ao fim de {} s".format(y_max_sem_resistencia,t_max_sem_resistencia))


# g) Alcance máx e instante coreespondente (c/ e s/ res ar)

x_pos = x[y>=0]
y_pos = y[y>=0]
x_max_sem_resistencia = np.round(x_pos[x_pos == x_pos.max()],4)[0]
t_max_alcance_sem_resistencia = t[y>=0][x_pos == x_pos.max()][0]
x_max_com_resistencia = np.round(x_pos[x_pos == x_pos.max()],4)[0]
t_max_alcance_com_resistencia = t[y>=0][x_pos == x_pos.max()][0]

print("EULER: O alcance máxima atingido pelo bola tendo em consideração a resistência do ar é: {} m ao fim de {}s".format(x_max_com_resistencia,t_max_alcance_com_resistencia))
print("EULER: O alcance máxima atingido pelo bola tendo em sem a resistência do ar é: {} m ao fim de {}s".format(x_max_sem_resistencia,t_max_sem_resistencia))