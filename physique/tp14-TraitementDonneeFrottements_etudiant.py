#################
# Bibliothèques #
#################
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

############################
# PARAMETRES EXPERIMENTAUX #
############################
m = 0.2
delta_m = 0.001 # imprécision sur la mesure de m (kg)

#############################
# CHARGEMENT DU FICHIER CSV #
#############################

# A ADAPTER EN FONCTION DE VOS DONNEES

#dossier = "C:/CHEMIN/VERS/LE/DOSSIER/" # A MODIFIER
fichier = "relevé.csv"
data = np.loadtxt(fichier, skiprows=1, delimiter=",")#, max_rows = 2000
indStart = 450  #permet d'ajuster le premier point pour retirer les données ne correspondant pas aux oscillations
t    = data[indStart:,0] - data[indStart,0]
a    = data[indStart:,2]
a_abs = np.abs(a)



#####################################
# TRACE GRAPHIQUE DE L'ACCELERATION #
#####################################
fig = plt.figure(1)
plt.title("Oscillations d'un système masse-ressort")
plt.ylabel("Acceleration $m\cdot s^{-2}$") 
plt.xlabel("temps($s$)")



###############################
# RECHERCHE DES MAXIMA LOCAUX #
###############################
# max_index : liste contenant les indices des maxima locaux
# a_max : liste des maxima locaux
# t_max : liste des instants où ont lieu les maxima
max_index = []
a_max = []
t_max = []

i_zeroes=[]
for i in range(len(a)-1) :
    if a[i]*a[i+1]<0 :
        i_zeroes.append(i+1)

for i in range(len(i_zeroes)-1) :
    tab=[a_abs[e] for e in range(i_zeroes[i],i_zeroes[i+1])]
    a_max.append(np.max(tab))
    max_index.append(np.argmax(tab)+i_zeroes[i])
    t_max.append(t[np.argmax(tab)+i_zeroes[i]])

for i in range(len(a_max)-1) :
    a_max[i]=(a_max[i]+a_max[i+1])/2

#plt.plot(t_max,a_max)
plt.plot(t,a_abs)
plt.plot(t_max,a_max)
plt.show()
    
    
###############################
# DETERMINATION DE LA PERIODE #
###############################



T = 2*np.mean([t[max_index[i+1]]-t[max_index[i]] for i in range(len(max_index)-1)])   # A COMPLETER     # période en s
u_T =  0.1 # A COMPLETER    # incertitude sur la période
omega0 = 2*3.14159/T
u_omega0 = omega0*u_T/T
k = m*(omega0**2)

print(T)


# #####################################################
# # TRACE GRAPHIQUE DE L'ACCELERATION AVEC VALEUR MAX #
# #####################################################
# fig = plt.figure(2)
# plt.title("Oscillations d'un système masse-ressort")
# plt.ylabel("Acceleration $m\cdot s^{-2}$") 
# plt.xlabel("temps($s$)")
# plt.plot(t, a_abs)
# plt.scatter(t_max, a_max) 
# plt.show()

#############################
# TRAITEMENT DE DONNEES 1 : #
#############################
# Hypothèse frottement linéaire
# On applique le décrément logarithmique

CoeffDir, OrdOrigine = np.polyfit([(t_max[i+1]-t_max[i])/np.log(a_max[i+1]/a_max[i]) for i in range(len(max_index)-1)])# A COMPLETER # Déterminer le coefficient directeur et l'ordonnée à l'origne de la droite moyenne


fig = plt.figure(3)
plt.title("Hypothèse frottement linéaire")
plt.ylabel("") 
plt.xlabel("t") 
#plt.scatter(t_max,) # A COMPLETER) 
plt.plot(t_max, CoeffDir*np.array(t_max) + OrdOrigine , "r-" ) 
plt.show()

# #############################
# # TRAITEMENT DE DONNEES 2 : #
# #############################
# # Hypothèse frottement quadratique
# coeffDir, OrdOrigine = # A COMPLETER # Déterminer le coefficient directeur et l'ordonnée à l'origne de la droite moyenne


# fig = plt.figure(4)
# plt.title("Hypothèse frottement quadratique")
# plt.ylabel("") A COMPLETER) 
# plt.xlabel("t") 
# plt.scatter(t_max, # A COMPLETER) 
# plt.plot(t_max, coeffDir*np.array(t_max) + OrdOrigine, "r-" ) 
# plt.show()


# #############################
# # TRAITEMENT DE DONNEES 3 : #
# #############################
# # Hypothèse frottement en v^p

# # A COMPLETER SI BESOIN 


# #################################################################
# # AJUSTEMENT ET INCERTITUDES UTILISANT LA MATRICE DE COVARIANCE #
# #################################################################
# out,cov = np.polyfit(t_max,1/np.array(a_max)**(p-1),1,cov=True)  #note : les coefficients a et b sont dans out
# coeffDir = out[0]
# OrdOrigine = out[1]

# #la matrice de covariance cov permet d'extraire l'incertitude sur les paramètres du modèle linéaire
# U = np.sqrt(np.diag(cov))
# UcoeffDir = U[0]
# UOrdOrigine = U[1]

# print("PARAMÈTRES DE L'AJUSTEMENT")
# print("Coefficient directeur a    :", coeffDir)
# print("Ordonnée à l'origine  b    :", OrdOrigine)
# print("Incertitude sur le Coefficient directeur    : u(a) =", UcoeffDir)
# print("Incertitude sur l' Ordonnée à l'origine     : u(b) =", UOrdOrigine)


# fig = plt.figure(6)
# plt.scatter(t_max, 1/np.array(a_max)**(p-1)) 
# plt.plot(t_max, coeffDir*np.array(t_max)+OrdOrigine, "r-" , label="Ajustement 2")
# plt.title("Regression linéaire")
# plt.xlabel("x")
# plt.ylabel("y")
# plt.legend()
# plt.show()


# ############
# # FONCTION #
# ############

# #Calcul de Ip
# def I_p(p):
#     """
#     Calcul numérique de la valeur de Ip
#     quad(f,a,b) permet l'integration d'une fonction f entre deux bornes a et b
#     """
#     def fun_f(x):
#         return np.abs(np.sin(x))**(p+1)
#     return quad(fun_f, 0, 2*3.14159)[0]

# #On calcule la valeur de Ip numériquement
# Ip = I_p(p)


# #Calcul de alpha à partir du coefficient directeur
# def fun_alpha(omega0, m, coeffDir):
#     alpha = coeffDir*2*3.14159/(p-1)/Ip*m/omega0**(p-1)
#     return alpha


# # Simulation de n mesures à partir des données : méthode de Monté Carlo
# n = 10000
# omega0_s  = omega0 + np.random.normal(0, u_omega0, n)
# m_s =  m +  np.random.uniform(-delta_m, delta_m, n) 
# coeffDir_s = coeffDir + np.random.normal(0, UcoeffDir, n)
# alpha_s = fun_alpha(omega0_s, m_s, coeffDir_s)


# ###############################
# # Analyse des données simulée #
# ###############################
# alpha_moy = np.mean(alpha_s)
# u_alpha = np.std(alpha_s, ddof=1)
# print("Coefficient alpha      : ", alpha_moy)
# print("Incertitude sur alpha  : ", u_alpha)

















