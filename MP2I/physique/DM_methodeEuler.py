##############
# Librairies #
##############
import numpy as np
import matplotlib.pyplot as plt

##############################
# Paramètre de la résolution #
##############################
t0 = 0                  #(s)  # bornes inf de l'intervalle de résolution
tf = 5                  #(s)  # bornes sup de l'intervalle de résolution
dt = 10e-4               #(s)  # pas de temps
n  = int((tf-t0)/dt + 1)  # nombre de points de la base de temps
t = np.linspace(t0,tf,n)  #(s) # base de temps

###########################
# Paramètre du circuit RC #
###########################
u0  = 0   #(V) # u(0) (Condition Initiale)
R=10*10**6 #(Ohm) résitance du circuit
RL=10*10**3 #(Ohm) résistance de la lampe
C=150*10**-9 #(F) capacité du condensateur
tau_E = R*C  #(s) # temps caractéristique du circuit lorsque la lampe est éteinte
tau_A = (RL*R*C)/(R+RL) #(s) temps caractéristique du circuit lorsque la lampe est allumée
uA=90 #(V) tension d'allumage de la lampe
uE=70 #(V) tension où la lampe s'éteint après avoir été allumée

########################
# Signal du générateur #
########################
E   = 200  #(V)

###################
# Méthode d'Euler #
###################
u = np.zeros(len(t))  # préparation du tableau
u[0] = u0             # initialisation en fonction de la condition initiale
a=False               # variable contenant l'état de la lampe (false : éteinte, true : allumée)
for i in range(n-1):  # méthode d'Euler explicite
    if u[i]>uA : 
        a=True #on allume la lampe si la tension dépasse uA
    if u[i]<uE :
        a=False #on l'éteint si la tension dépasse uE
    if a :
        u[i+1] = (RL*E)/(R+RL) * dt / tau_A + u[i] * (1 - dt / tau_A)
    else :
        u[i+1] = (dt/tau_E)*E + u[i]*(1-dt/tau_E)

############################
# Représentation graphique #
############################
plt.figure(figsize=(6, 4), dpi=120)
plt.plot(t,u, label="u(t)")
plt.xlabel("Temps (s)")
plt.ylabel("Tension (V)")
plt.legend()
plt.show() # pour afficher le graphique

