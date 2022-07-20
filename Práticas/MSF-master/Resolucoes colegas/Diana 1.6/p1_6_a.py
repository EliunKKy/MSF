import numpy as np
import matplotlib.pyplot as plt

#a) Apresente estas medições num gráfico
y=np.array([0.00, 0.735, 1.363, 1.739, 2.805, 3.814, 4.458, 4.955, 5.666, 6.329])
npontos = len(y)
t = np.arange(0,npontos,1)

plt.scatter(t, y)
plt.xlabel("t (min)")
plt.ylabel("d (km)")
plt.show()

# RESPOSTA: Localmente nao é constante, mas podemos considerar uma relação entre o tempo e a distancia percorrida linear se nao formos minuciosos