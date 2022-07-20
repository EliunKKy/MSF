# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 00:50:58 2022

@author: Alexandre
"""

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

def rk4_2(t,x,vx,acelera,dt):
    """
    Integração numérica de equação diferencial de 2ª ordem:
			d2x/dt2 = ax(t,x,vx)    com dx/dt= vx    de valor inicial
	Erro global:  proporcional a dt**4
    acelera=dvx/dt=Força(t,x,vx)/massa      : acelera é uma FUNÇÃO
    input:  t = instante de tempo
            x(t) = posição
            vx(t) = velocidade
            dt = passo temporal 
    output: xp = x(t+dt)
		    vxp = vx(t+dt)
    """
    ax1=acelera(t,x,vx)
    c1v=ax1*dt
    c1x=vx*dt
    ax2=acelera(t+dt/2.,x+c1x/2.,vx+c1v/2.)
    c2v=ax2*dt
    c2x=(vx+c1v/2.)*dt			# predicto:  vx(t+dt) * dt
    ax3=acelera(t+dt/2.,x+c2x/2.,vx+c2v/2.)
    c3v=ax3*dt
    c3x=(vx+c2v/2.)*dt
    ax4=acelera(t+dt,x+c3x,vx+c3v)
    c4v=ax4*dt
    c4x=(vx+c3v)*dt
      
    xp=x+(c1x+2.*c2x+2.*c3x+c4x)/6.
    vxp=vx+(c1v+2.*c2v+2.*c3v+c4v)/6.
    return xp,vxp


def acelera(t,x,vx):
    ax=g-g/vt**2*np.abs(vx)*vx
    return ax