##############
# Librairies #
##############
import numpy as np
import matplotlib.pyplot as plt

########
# Data #
########
a = np.array([919.0,1680.0,1720.0,1900.0,5100.0,30000.0,70000.0]) # ua # À compléter
T = np.array([14.53,36,37.3,43,190,2600,9900]) # Year # À compléter

K = np.power(T,2)/np.power(a,3) # À compléter


#####################
# Tracés graphiques #
#####################
plt.figure(1)
plt.plot(T,K ) # À compléter
plt.ylim(0, 5E-6)
plt.show()

plt.figure(2)
plt.plot([T[i]**2 for i in range(len(T))],[a[i]**3 for i in range(len(a))] ) # À compléter
plt.ylim(0, 5E14)
plt.show()


######################
# Analyse de données #
######################
#print(np.mean(K))
#print(np.std(K, ddof = 1))

coeff = (1.496E11)**3/(365*24*3600)**2
G = 6.67E-11
Ms = 1.988E30
M = 4*(3.1415**2)*np.mean(K)*coeff/G/Ms/1E6
eM = 4*(3.1415**2)*np.std(K, ddof = 1)*coeff/G/Ms/1E6

print(M)
print(eM)


R0 = 8178*(3.09E16)/(1.496E11) #ua
T = np.sqrt(R0**3 / (np.mean(K)))
print(T/1E6)