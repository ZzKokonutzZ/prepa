# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

import numpy as np 
import matplotlib.pyplot as plt

Mes = np.loadtxt("donees.txt")
i = Mes[:,1]
u = Mes[:,0]

R_th=083 #ohms
E_th=0.4 #volts

u_th=np.linspace(0.4,1.6)
i_th=1**3*(u_th-E_th)/R_th

plt.figure()
plt.xlabel("Tension u en V")
plt.ylabel("Intensité i en mA")
plt.title("Caractéristique de i=f(u)")
plt.plot(u,i)
plt.plot(u_th,i_th)
plt.show()