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
print(z)
M=z[0] #declive (velocidade em Km/min)
B=z[1] #ordenada na origem

plt.scatter(x, y) #Desenho do gráfico de pontos
plt.plot(x,x*M+B) #Desenho da reta que mais se aproxima das medições
plt.xlabel("t (min)")
plt.ylabel("d (km)")
plt.show()

#Sim o declive e a ordenada na origem concordam com os valores calculados na alinea b)