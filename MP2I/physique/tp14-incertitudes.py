import numpy as np

"""
Etude dynamique des oscillations d'un systeme masse/ressort.
Script pour l'analyse de donnée de la mesure d'une constante de raideur
de ressort.
"""


########################
# MESURES ET IMPRÉCISION
########################
T = 0.61          # période des oscillations (s)
delta_T = 0.01   # imprecision sur la mesure de T (s)
m = 642.36*10**-3     # masse (kg)
delta_m = 0.01*10**-3 # imprécision sur la mesure de m (kg)

def raideur(T, m):
    """calcule la constante de raideur k d'un ressort, en N/m
        T : période des oscillations (s)
        m : masse (kg)
    """
    return (4 * np.pi**2 * m) / T**2

#######################################
# ESTIMATION DE L'INCERTITUDE DE TYPE B
#######################################
N = 10000
T_sim = T + np.random.uniform(-delta_T,delta_T,N)
m_sim = m + np.random.uniform(-delta_m,delta_m,N)
k_sim = raideur(T_sim,m_sim)

print("Estimation de type de B :")
print("k    = {:.2f} N/m".format(np.mean(k_sim)))
print("u(k) = {:.2f} N/m".format(np.std(k_sim,ddof=1)))