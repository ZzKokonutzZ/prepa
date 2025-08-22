##############
# Librairies #
##############
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from scipy.integrate import quad

##############
# Paramètres #
##############
g = 9.81     #(ms-2) # accélération de la pesanteur
l = 1        #(m)    # longueur du pendule
m = 1        #(kg)   # masse 

###################################################
# Fonctions associées à l'équation différentielle #
###################################################
def oh(V,t):
    """
    Fonction associée au pendule linéarisé (oscillateur harmonique)
    """
    x, y = V
    dx = y
    dy = - g/l * x
    dV = [dx, dy]
    return dV

def pendule(V,t):
    x,y=V
    dx=y
    dy=-g/l * np.sin(x)
    dV=[dx,dy]
    return dV

########################
# Résolution numérique #
########################
#Paramètres
duree  = 10      #(s) # duree de la simulation
dt     = .01     #(s) # intervalle de temps entre deux instants successifs
t = np.linspace(0, duree, int(duree/dt))

# Résolution
V0     = [2, 0]  # conditions initiales (θ, v_θ)
V = odeint(oh, V0, t) # intégration numérique de l'équation différentielle
V_0 = odeint(pendule,V0,t)
theta_oh = V[:,0]  # valeurs de theta pour l'oscillateur harmonique
omega_oh = V[:,1]  # valeurs de omega pour l'oscillateur harmonique

thetanos=V_0[:,0]
omegod=V_0[:,1]



###################
# Tracé graphique #
###################
plt.figure(1)
#plt.plot(t, theta_oh)
plt.plot(t, thetanos)
plt.title("oscillations")
plt.xlabel("temps (s)")
plt.ylabel("θ (rad)")
plt.show()

######################################
# calcul de T en fonction de theta_0 #
######################################



####################
# Fonctions utiles #
####################

def periode_int(theta0):
    """
    Calcul numérique de la valeur de la période, pour une amplitude theta0
    theta0 doit être une valeur unique
    quad(f,a,b) permet l'integration d'une fonction f entre deux bornes a et b
    """
    def dt(theta):
        return -1 / np.sqrt(2 * (g/l) * (np.cos(theta) - np.cos(theta0)))
    return 4 * quad(dt, theta0, 0)[0]


plot=plt.figure(2)
degouT=[]
thetaclaque=np.linspace(0.01,3,100)
print(thetaclaque)
for i in thetaclaque :
    print(i)
    degouT.append(periode_int(i))

plt.title("T")
plt.xlabel("θ")
plt.ylabel("T")
plt.plot(thetaclaque,degouT)
Tfatigue=2*np.pi*np.sqrt(l/g)*(1+thetaclaque/16)
plt.plot(thetaclaque,Tfatigue)
plt.show()