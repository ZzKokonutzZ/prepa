##############
# Librairies #
##############
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
##############
# Paramètres #
##############
ti = 0                #s   # bornes de l'intervalle de résolution
tf = 5                #s   # en secondes
dt = 1e-3             #s   # pas de temps en secondes
n  = int((tf-ti)/dt + 1) # nombre de points
t = np.linspace(ti,tf,n) #s # temps en secondes
V0 = [0,0]               #V # conditions initiales : [u(0), du(0)/dt]
r=6 #Ohm, résistance interne du circuit
C=10*10**-6 #Farad, capacité du condensateur
L=5 #Henri, inductance de la bobine
E=12 #V, tension du générateur
omega0 = 1/np.sqrt(L*C)   #s^-1 # pulsation propre
Q=(1/r)*np.sqrt(L/C) #facteur de qualité
q_0=-C*E #coulombs, charge maximale atteinte par le condensateur
mu=omega0/(2*Q) #s^-1, inverse du temps caractéristique
omega=omega0*np.sqrt(1-(1/(4*Q**2))) #s^-1, pulsation propre de l'oscillateur amorti

###################################################
# Fonctions associées à l'équation différentielle #
###################################################
def fun_F(V, t):
    x, y = V        # vecteur V : v[0] = u, v[1] = du/dt
    dx = y          # dx/dt
    dy = -(omega0/Q)*y-omega0**2*x+omega0**2*q_0# dy/dt
    dV = [dx, dy]   # vecteur dV/dt : dV[0] = du/dt, dV[1] = d2u/dt2 
    return dV
###############
# Résolution  #
###############
X = odeint(fun_F, V0, t) # résolution
u = X[:,0]           # récupération des données

#####################
#solution analytique#
#####################
a=[]
for i in range(len(t)) :
    #a+=[(-q_0*np.cos(omega*t[i])-mu*q_0*np.sin(omega*t[i]))*np.exp(-mu*t[i])+q_0]
    a+=[q_0*(1-(np.cos(omega*t[i])+(mu*q_0/omega)*np.sin(omega*t[i]))*np.exp(-mu*t[i]))]

###################
# Tracé graphique #
###################
plt.figure(figsize=(8, 6), dpi=150)
plt.plot(t, u)
plt.plot(t,a)
plt.ylabel("Charge (C)")
plt.xlabel("Temps (s)")
plt.show()