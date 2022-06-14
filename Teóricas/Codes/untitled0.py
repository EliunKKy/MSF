import matplotlib.pyplot as plt
import numpy as np

g = 9.8
delta_t = 0.1
n = 40
t = np.linspace(0, n*delta_t, n+1)
xt = 1/2*(g*(t**2))
vt = g*t

apr = [0]*(n+1)

for i in range(1, n+1):
    vplaceholder = g*(i-1)*delta_t
    apr[i] = apr[i-1] + vplaceholder * delta_t


plt.plot(t, xt)
plt.plot(t, vt)
plt.plot(t, apr, "x")

