import numpy as np

d=np.array([0.00, 0.735, 1.363, 1.739, 2.805, 3.814, 4.458, 4.955, 5.666, 6.329])
npontos = len(d)
t = np.arange(0,npontos,1)
#Truque para não ter de alterar o código abaixo: identificar x e y corretamente
x=t
y=d

#SOMAS
xy=x*y # element by element product
x2=x*x
y2=y*y

sx=x.sum()
sy=y.sum()
sxy=xy.sum()
sxx=x2.sum()
syy=y2.sum()

#b)  Encontre o declive, a ordenada na origem, os erros respetivos e o coeficiente de determinação. 

n=npontos
rn=n*sxy-sx*sy
rd=(n*sxx-sx**2)*(n*syy-sy**2)
r2=rn**2/rd
r=np.sqrt(r2)
m=(n*sxy-sx*sy)/(n*sxx-sx**2)
dm=abs(m)*np.sqrt((1/r**2-1)/(n-2))
bn=sxx*sy-sx*sxy  
bd=n*sxx-sx**2
b=bn/bd
db=dm*np.sqrt(sxx/n)

print()
print("m +/-dm = {:0.8f} +/- {:0.8f}".format(m,dm))
print("b +/-db = {:0.8f} +/- {:0.8f}".format(b,db))
print("r2 = {:0.8f}".format(r2))

#Sim, pq o r**2 é muito próximo de um.
#alinea c) A velocidade média é o declive da reta logo é 0.7km/min
