# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 17:40:43 2022

@author: rodri
"""
import numpy as np
import matplotlib.pyplot as plt

# Int tempo
dt = 0.0001
t = np.arange(3 + dt, dt)


# Arrays
vx = np.zeros(t.size)
vy = np.zeros(t.size)

# variables 
t = 2
vt = 6,80
vx[0] = 0
g = 9,8


def ay(t, vy):
    ay = g - (g/vt**2)*np.abs(vy)*vy

def rk4(t,vx,acelera,dt):
    """
    Integração numérica de equação diferencial de 2ª ordem:
			dvx/dt = ax(t,vx)    de valor inicial
	Erro global:  proporcional a dt**4
    acelera=dvx/dt=Força(t,vx)/massa     : acelera é uma FUNÇÃO
    input:  t = instante de tempo
            vx(t) = velocidade
            dt = passo temporal 
    output: vxp = vx(t+dt)
    """
    ax1=acelera(t,vx)
    c1v=ax1*dt
    ax2=acelera(t+dt/2.,vx+c1v/2.)
    c2v=ax2*dt       			# predicto:  vx(t+dt) * dt
    ax3=acelera(t+dt/2.,vx+c2v/2.)
    c3v=ax3*dt
    ax4=acelera(t+dt,vx+c3v)
    c4v=ax4*dt
          
    vxp=vx+(c1v+2.*c2v+2.*c3v+c4v)/6.
    return vxp