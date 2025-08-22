##############
# Librairies #
##############
import numpy as np
from scipy.integrate import quad

####################
# Fonctions utiles #
####################

def periode_int(theta0,g,l):
    """
    Calcul numérique de la valeur de la période, pour une amplitude theta0
    theta0 doit être une valeur unique
    quad(f,a,b) permet l'integration d'une fonction f entre deux bornes a et b
    """
    def dt(theta):
        return -1 / np.sqrt(2 * (g/l) * (np.cos(theta) - np.cos(theta0)))
    return 4 * quad(dt, theta0, 0)[0]

def euler_deuxieme_ordre(f, V0, t):
    """
    Intègre numériquement une équation du second ordre
    en utilisant la méthode d'euler explicite.
        PARAMÈTRES :
        f : fonction associée à l'équation différentielle
        V0: conditions initiales
        t : tableau des instants auxquels évaluer la solution x(t)
        RENVOIE :
        Tableau contenant les valeurs de x(t) et de sa dérivée
    """
    dt = t[1] - t[0]
    x  = np.zeros(len(t))
    v = np.zeros(len(t))
    x[0] = V0[0]
    v[0] = V0[1]
    V = [np.array([x[0],v[0]])]
    for i in range(len(t)-1):
        dx, dv = f([x[i], v[i]], t[i])
        x[i+1] = x[i] + dt * dx
        v[i+1] = v[i] + dt * dv
        V.append(np.array([x[i+1],v[i+1]]))
    return np.array(V)

