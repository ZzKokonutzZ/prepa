import numpy as np
import matplotlib.pyplot as plt

"""
Etude statique d'un systeme masse/ressort
Ajustement linéaire de l'alongement en fonction de la masse.
Evaluation des incertitudes sur la pente et l'ordonnée à l'origine d'un 
ajustement linéaire par simulation type Monte-Carlo

"""



# Constantes
g = 9.81       # accélération de pesanteur (m.s^-2)

########################
# MESURES ET IMPRÉCISION
########################
# masses (kg)
m = np.array([50,100,120,150,200,250,300,350,400,450,498])*1e-3
delta_m = 1e-3 # imprécision sur la mesure de m (kg)
# longueurs du ressort (m)
l = np.array([7.25,8,8.25,8.5,9.5,10.4,10.75,11.25,12.25,12.75,13.5])*1e-2 
delta_l = 2e-3 # imprecision sur la mesure de L (m)

##############################################
# ESTIMATION DE L'INCERTITUDE SUR L'AJUSTEMENT
##############################################
tab_a, tab_b = [], []
for n in range(10000):
    # Simulation d'un grand nombre de mesures pour estimer
    # l'incertitude sur les paramètres de l'ajustement 
    m_sim = m + np.random.uniform(-delta_m,delta_m,len(m))
    l_sim = l + np.random.uniform(-delta_l,delta_l,len(l))
    a, b = np.polyfit(m_sim,l_sim,1)
    tab_a.append(a) # coefficient directeur
    tab_b.append(b) # ordonnée à l'origine
k_sim = g/np.array(tab_a) # constantes de raideur (N/m)
print("Estimation de type de B :")
print("k    = {:.2f} N/m".format(np.mean(k_sim)))
print("u(k) = {:.2f} N/m".format(np.std(k_sim,ddof=1)))

######################################
# REPRÉSENTATION GRAPHIQUE DES DONNÉES
######################################
plt.xlabel("Masse (kg)")
plt.ylabel("Alongement (m)")
plt.plot(m,l,"o")
a = np.mean(a) # meilleure estimation du coeficient directeur
b = np.mean(b) # meilleure estimation de l'ordonnée à l'origine
plt.plot(m,a*m+b)