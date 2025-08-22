##############
# Librairies #
##############

import numpy as np
import matplotlib.pyplot as plt


########
# Data #
########
# Lecture du fichier de données
# ATTENTION : lors de l'export des données depuis Phyphox
#   - le fichier doit être au format CSV
#   - choisir ; comme séparateur de colonnes
#   - choisir . comme séparateur décimal
# => cocher CSV (Semicolon,decimal point)

data = np.genfromtxt('data.csv', delimiter=',')
t = data[1:,0]
omega_x = data[1:,1]
omega_y = data[1:,2]
omega_z = data[1:,3]
R=0.05

v=R*omega_y

plt.plot(t,v)
plt.show()
#################################################################
# AJUSTEMENT ET INCERTITUDES UTILISANT LA MATRICE DE COVARIANCE #
#################################################################
p,cov = np.polyfit(t,v,1,cov=True)  #note : les coefficients a et b sont dans p
a = p[0]
b = p[1]

U = np.sqrt(np.diag(cov))
Ua = U[0]
Ub = U[1]

print("PARAMÈTRES DE L'AJUSTEMENT")
print("Coefficient directeur a    :", a)
print("Ordonnée à l'origine  b    :", b)
print("Incertitude sur le Coefficient directeur a    : u(a) =", Ua)
print("Incertitude sur l' Ordonnée à l'origine  b    : u(b) =", Ub)


fig2 = plt.figure("Ajustement")
plt.errorbar(t,v, fmt="o", capsize=2, label="Données") 
plt.plot(t, a*t+b, label="Ajustement linéaire")

# Tracé limite en tenant compte de l'incertitude
#plt.plot(x, a*x+b-Ub)
#plt.plot(x, a*x+b+Ub)
#plt.plot(x, (a+Ua)*x+b)
#plt.plot(x, (a-Ua)*x+b)

plt.title("Regression linéaire")
plt.xlabel("t")
plt.ylabel("v")
plt.legend()
plt.show()
