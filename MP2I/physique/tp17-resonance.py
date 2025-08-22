#################
# BIBLIOTHEQUES #
#################

import numpy as np
import matplotlib.pyplot as plt

#################################
# Lecture du fichier de données #
#################################
# data = np.loadtxt("data.txt",skiprows=1)
# f = data[:,0] # première colonne : fréquence en Hz
# e = data[:,1] # deuxième colonne : tension aux bornes du GBF en V
# u = data[:,2] # troisième colonne : tension aux bornes de R ou C en V
# G = u/e

f=np.array([0.3,1,3,5,7,8,10,11,13,15,20,30,50,70,100,103,115,120,130,200,300,1000,3000])
e=np.array([5.0]*23)
u=np.array([4.8,6,6.8,7.8,25.3,14.5,13.3,7.9,1.6,4.4,2.65,0.63,0.6,0.3,0.16,0.5])
#G=20*np.log(u/e)

u_r=np.array([4.4,4.4,4.4,4.4,4,3.6,3,2.7,2.2,1.8,1.2,0.7,0.43,0.2,0.04,0.038,0.03,0.025,0.015,0.015,0.02,0.015,0.8])

G_r=20*np.log(u_r/e)
############################
# Représentation graphique #
############################
# avec une échelle logarithmique pour la fréquence
# Il suffit de remplacer plt.plot par plt.semilogx
# Pour que l'axe des ordonnées soit en échelle log, utiliser plt.semilogy
# Pour un tracer loglog, utiliser plt.loglog
#plt.semilogx(f,G,"o")
plt.semilogx(f,G_r,"o")
plt.xlabel('f (Hz)')
plt.ylabel('Gdb')
plt.show()

# À compléter (titre, nom des axes, etc.)