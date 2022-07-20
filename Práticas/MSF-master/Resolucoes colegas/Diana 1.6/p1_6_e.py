import numpy as np
import matplotlib.pyplot as plt

d=np.array([0.00, 0.735, 1.363, 1.739, 2.805, 3.814, 4.458, 4.955, 5.666, 6.329])
npontos = len(d)
t = np.arange(0,npontos,1)
#Truque para não ter de alterar o código abaixo: identificar x e y corretamente
x=t
y=d

#d)  Use a função polyfit dos pacote numpy ou do pacote pylab para encontrar a reta que mais se aproxima das medições. 
z=np.polyfit (x,y,1)
M=z[0] #declive (velocidade em Km/min)
B=z[1] #ordenada na origem

#e) Apresente a velocidade em km/hora
v= M*60
print("velocidade é {:.0f}km/h".format(v))