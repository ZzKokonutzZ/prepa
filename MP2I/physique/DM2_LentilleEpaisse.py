##############
# Librairies #
##############
import numpy as np
import matplotlib.pyplot as plt

##############
# PARAMÈTRES #
##############
R = 1       #(m) # rayon du dioptre sphérique
n = 1.5     #()  # indice de la lentille
hmax = 0.11   #(m) # distance maximale du rayon incident
N = 100        #

######################
# TRACÉ DE LA FIGURE #
######################
fig = plt.figure(figsize=(10,6))
plt.plot([-2*R, 5*R], np.zeros(2), "--k") # axe optique
fig.axes[0].set_aspect("equal")           # échelle identique sur les deux axes
plt.xlim(-2*R, 5*R)
plt.xlabel("x (m)")
plt.ylabel("y (m)")
# Dioptre sphérique
theta = np.linspace(-np.pi/2, np.pi/2, 101)
xd = R * np.cos(theta) - R
yd = R * np.sin(theta)
plt.plot(xd, yd, "k")
plt.plot([xd[0], xd[-1]], [yd[0], yd[-1]], "k")

####################
# TRACÉ DEs RAYONS #
####################
for h in np.linspace(-hmax, hmax, N):
    # Coordonnées des points
    xA, yA = (-2*R, h)                   # point A
    xI, yI = (-R, h)                     # point I
    xJ, yJ = (np.sqrt(R**2 - h**2)-R, h) # point J
    # Angles au niveau du dioptre sphérique
    i = np.arcsin(h / R)     # angle d'incidence
    r = np.arcsin(n * h / R) # angle de réfraction
    xK, yK = (xJ + h / np.tan(r-i), 0)   # point K
    xB, yB = (2*xK-xJ, -h)               # point B
    # Tracé de la marche des rayons
    x = [xA, xI, xJ, xK, xB]
    y = [yA, yI, yJ, yK, yB]
    plt.plot(x, y, "red")
plt.show()


######################################################
# Recherche position et dimension de la tache focale #
######################################################

Nx = 1000

x_list = np.linspace(0,5*R, num=Nx)
a_rayons=[]
b_rayons=[]
for h in np.linspace(-hmax, hmax, N):
    # Coordonnées des différents points
    xA, yA = (-2 * R, h)                 # coordonnées du point A
    xI, yI = (-R, h)                     # coordonnées du point I
    xJ, yJ = (np.sqrt(R**2 - h**2)-R, h) # coordonnées du point J
    # Angles au niveau du dioptre sphérique
    i = np.arcsin(h / R)     # angle d'incidence
    r = np.arcsin(n * h / R) # angle de réfraction
    xK, yK = (xJ + h / np.tan(r-i), 0)   # coordonnées du point K
    xB, yB = (2*xK-xJ, -h)               # coordonnées du point B
    #Coefficient directeur et ordonnée origine de la droite passant par B et K
    a_rayon = (yB-yK)/(xB-xK)
    b_rayon = yB-a_rayon*xB
    a_rayons.append(a_rayon) #Ajoute la variable a_rayon à la liste a_rayons
    b_rayons.append(b_rayon) #Ajoute la variable b_rayon à la liste b_rayons

#Conversion liste en tableau
a_rayons = np.array(a_rayons)
b_rayons = np.array(b_rayons)

#Initialisation des variables
d_min = 2*R
x_tache = 0

#Recherche de d_min et x_tache
for x in x_list:
    y = a_rayons*x + b_rayons
    d_tache = np.max(y) - np.min(y)
    if(d_min> d_tache):
        d_min = d_tache
        x_tache = x


#Tracé de la tache sur le graphique
plt.plot([x_tache,x_tache], [-d_min/2, d_min/2], "green")

#Affichage des valeurs dans la console
print(d_min)
print(x_tache)
