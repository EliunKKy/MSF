import matplotlib.pyplot as plt
import numpy as np
x = np.array([])
y = np.array([])

v=6.8
g=9.8
t=0
while t < 2.2:
    y = np.append(y, v**2/g*np.log(np.cosh(g*t/v)))
    x = np.append(x, t)
    t = t+0.1


fig1, ax = plt.subplots(1, 2, figsize=(21,9), layout="constrained")
ax[0].plot(x,y,"o")
ax[1].plot(x,y)
