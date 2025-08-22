##############
# Librairies #
##############
import numpy as np
import matplotlib.pyplot as plt

########
# Data #
########
"""
Loadtxt permet de lire un fichier texte contenant des données
structurées. Il s'agit d'un fichier type "csv"
L'option skiprows permet de sauter les 18 premières lignes qui sont des 
information sur le formatage du fichier (ouvrir le fichier avec un éditeur
texte pour s'en convaincre.
Les données sont ensuites écrites dans un tableau 'data'
Ouvrir le dossier data pour connaitre le nom des fichiers utilisables.
"""
planete = "earth"
data = np.loadtxt("data/"+planete+".csv", skiprows=18, max_rows=1000)
t          = data[:,0] - data[0,0]
x, y, z    = data[:,1], data[:,2], data[:,3]
vx, vy, vz = data[:,7], data[:,8], data[:,9]

############################
# Tracés de la trajectoire #
############################
fig = plt.figure(1)
plt.title("Trajectoire de "+planete)
plt.xlabel(" ") #A COMPLETER
plt.ylabel(" ") #A COMPLETER
plt.scatter(0, 0) #Permet de tracer le centre O.
plt.plot(x, y)
fig.axes[0].set_aspect("equal") # Impose la même échelle sur les 2 axes.
# plt.show()

graph=plt.figure(2)
plt.title("variation de L")

 
def L(x,y,z,vx,vy,vz) :
    return np.sqrt((y*vz-z*vy)**2+(z*vx-x*vz)**2+(x*vy-y*vx)**2)
tab_l=L(x,y,z,vx,vy,vz)
plt.plot(t,tab_l)
# plt.show()

L_moy=sum(tab_l)/len(tab_l)

uL=np.std(tab_l,ddof=1)

E_n=(tab_l-L_moy)/uL
print(E_n)
E=plt.figure(3)
plt.plot(t,E_n)

def A(x1,y1,z1,x2,y2,z2) :
    m=[(x2+x1)/2,(y2+y1)/2,(z2+z1)/2]
    b=np.sqrt((x2-x1)**2+(y2-y1)**2+(z2-z1)**2)
    return b*np.sqrt(m[0]**2+m[1]**2+m[2]**2)/2

tab_a=A(x[:-1],y[:-1],z[:-1],x[1:],y[1:],z[1:])
a=plt.figure(4)
plt.plot(t[:-1],tab_a)
plt.show()

T=[14.53,36,37.3,43,190,2600,]