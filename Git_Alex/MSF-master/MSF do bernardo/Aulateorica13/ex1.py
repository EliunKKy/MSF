# -*- coding: utf-8 -*-
import numpy as np
from numpy import linalg as LA
#a)
marr = [1,2]
for m in marr:
    k = 0.00000001
    kl = 0.5
    
    array = [[(k+kl)/m,-kl/m,0],[-kl/m,2*kl/m, -kl/m], [0, -kl/m, (k+kl)/m]]
    
    w, v = LA.eig(array)
    
    
    #b)
    
    omega = np.sqrt(w)
    
    print("m=", m, "vibrations=", omega)

