# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 15:21:41 2022

@author: Alexandre
"""

import numpy as np
import matplotlib.pyplot as plt

g=9.8
vt=100*1000/3600
massa=0.45
omega=400
dt=0.001
n=int(0.5/dt)
print('n: ', n)
t=np.zeros(n+1)
x=np.zeros(n+1)
y=np.zeros(n+1)
z=np.zeros(n+1)
vx=np.zeros(n+1)
vy=np.zeros(n+1)
vz=np.zeros(n+1)
ax=np.zeros(n+1)
ay=np.zeros(n+1)
az=np.zeros(n+1)

z[0]=23.8
vx[0]=25
vy[0]=5
vz[0]=-50
mag=0.5*1.225*0.11*np.pi*0.11**2


for i in range(n):
    t[i+1]=t[i]+dt
    vv=np.sqrt(vx[i]**2+vy[i]**2+vz[i]**2)
    dres=g/vt**2
    amx=mag*omega*vz[i]/massa
    amz=-mag*omega*vx[i]/massa
    ax[i]=dres*vv*vx[i]+amx
    ay[i]=-g-dres*vv*vy[i]
    az[i]=-dres*vv*vz[i]+amz
    vx[i+1]=vx[i]+ax[i]*dt
    vy[i+1]=vy[i]+ay[i]*dt
    vz[i+1]=vz[i]+az[i]*dt
    x[i+1]=x[i]+vx[i]*dt
    y[i+1]=y[i]+vy[i]*dt
    z[i+1]=z[i]+vz[i]*dt
    
plt.grid()
plt.plot(t, x, label='x(t)')
plt.plot(t, y, label='y(t)')
plt.plot(t, z, label='z(t)')
plt.xlabel("t(m)")
plt.legend()