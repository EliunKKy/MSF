import matplotlib.pyplot as plt
import numpy as np

# variaveis 
va = 19.44
vp = 0
a = 2.0

# intervalo
delta_t = 0.1
n = 250
t = np.linspace(0, n*delta_t, n)

# instante de intercepção
I = (2*va)/a
X = va*I

# leis de movimento
xa = va*t
xp = 1/2*(a*(t**2))

# gráfico
plt.plot(t, xa, label = "xa")
plt.plot(t, xp, label = "xp")
plt.xlabel("s")
plt.ylabel("m/s")
plt.title("Patrulha")
plt.legend()