# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 10:00:37 2021

@author: vitor.torres
"""

def rk4(t,vx,acelera,dt):
    """
    Integração numérica de equação diferencial de 2ª ordem respeitante ao movimento
    acelera=dvx/dt=Força(t,x,vx)/massa      com vx=dx/dt   (acelera é uma função)
    input:  t = instante de tempo
            vx(t) = velocidade
            dt = passo temporal 
    output: vx(t+dt)
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

