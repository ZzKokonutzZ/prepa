##############
# Librairies #
##############
import numpy as np
import matplotlib.pyplot as plt

##############
# Paramètres #
##############
#Signal  réel
U0 = 10   # amplitude du signal u(t) en volts
f0 = 50   # fréquence du signal u(t) en hertz
Vs = 0.6  # tension de seuil des diodes en volts
fe = 100    # Fréquence du fondamental pour e(t) #A modifier

#Coefficients série de Fourier
cn   = [10.4242, 4.1528, 0.7588, 0.2759] # coefficients cn en volts
phin = [      0,  np.pi,  np.pi,  np.pi] # coefficients phin en radians

#############
# Fonctions #
#############

def u(t):
    """
    params: temps t en secondes
    returns: tension u(t) à la sortie du transformateur en volts
    """
    return U0 * np.sin(2*np.pi*f0 * t)

def e(t):
    """
    params: temps t en secondes
    returns: tension e(t) à la sortie du pont de Graëtz en volts
    """
    output = []
    for ti in t:
        value = np.abs(u(ti))- 2*Vs
        if(value > 0):
            output.append(value)
        else:
            output.append(0)
    return output

def e3(t):
    """
    params: temps t en secondes
    returns: tension e(t) à la sortie du pont de Graëtz en volts calculé à 
             partir des 3 premiers coefficients de sa série de Fourier            
    """
    #A COMPLETER
    e3a=[]
    for i in range(len(t)) :
        e3a+=[cn[0]/2+cn[1]*np.cos(2*np.pi*fe*t[i]+phin[1])+cn[2]*np.cos(4*np.pi*fe*t[i]+phin[2])+cn[3]*np.cos(6*np.pi*fe*t[i]+phin[3])]
    return e3a

R=100
L=500e-4
omega0=1/L

def G(omegatés) :
    return 1/np.sqrt(1+(omegatés**2)/(omega0**2))

def phibonacci(omegatés) :
    return -np.arctan((omegatés)/(omega0))

cthuluh=[cn[i]*G(i*fe) for i in range(len(cn))]

phifi=[phin[i]+phibonacci(i*fe) for i in range(len(phin))]

def dehors(t) :
    troishors=[]
    for i in range(len(t)) :
        troishors+=[cthuluh[0]/2+cthuluh[1]*np.cos(2*np.pi*fe*t[i]+phifi[1])+cthuluh[2]*np.cos(4*np.pi*fe*t[i]+phifi[2])+cthuluh[3]*np.cos(6*np.pi*fe*t[i]+phifi[3])]
    return troishors

#####################
# Tracés graphiques #
#####################
plt.figure(1)
plt.clf()
t = np.linspace(0,2/f0, 1000) # instants t en secondes pour les graphes
plt.title("Évolution temporelle des différents signaux")
plt.plot(t, u(t), label="$u(t)$")
plt.plot(t, e(t), label="$e(t)$")
plt.plot(t,e3(t),label="$e3(t)$")
plt.plot(t,dehors(t),label="$DEHORS !$")
#plt.plot(t, e3(t), label="$e3(t)$")
plt.xlabel("Temps (s)")
plt.ylabel("Signal (V)")
plt.legend()
plt.grid(which="both")
plt.show()
