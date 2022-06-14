import matplotlib.pyplot as plt
import numpy as np

# variáveis
v = 6.80
delta_t = 0.1
n = 40
t = np.linspace(0, n*delta_t, n)
t = np.array(t)
g = 9.8


# função
y = (v**2/g)*np.log(np.cosh((g*t)/v))

            
                    
# gráfico  
plt.plot(t, y)       