##############
# Librairies #
##############

import numpy as np
import matplotlib.pyplot as plt


############
# Fonction #
############
def theta(x, y, z):
    """
    params: coordonnées cartésiennes x, y, z
    return: angle theta des coordonnées cylindriques
    """
    return np.unwrap(np.angle(x+1j*y))

def FFT(t, signal):
    """
    Parameters
    ----------
    t : temps
    signal : grandeur
    
    Returns
    -------
    None.
    """
    fft_signal = np.fft.fft(signal)
    freqs = np.fft.fftfreq(len(signal), t[1] - t[0])
    mask = freqs > 0
    return [freqs[mask], fft_signal[mask]]


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
planete = "mercury"
data = np.loadtxt("data/"+planete+".csv", skiprows=18, max_rows=1000)
t          = data[:,0] - data[0,0]
x, y, z    = data[:,1], data[:,2], data[:,3]
vx, vy, vz = data[:,7], data[:,8], data[:,9]

#Traitements
r = np.sqrt(x**2+y**2+z**2)

############################
# Tracés de la trajectoire #
############################
fig = plt.figure(1)
plt.title("Trajectoire")
plt.xlabel("À compléter")
plt.ylabel("À compléter")
plt.scatter(0, 0)
plt.plot(x, y)
fig.axes[0].set_aspect("equal") # même échelle sur les deux axes
plt.show()

fig = plt.figure(2)
plt.plot(t, theta(x,y,z))
slope, offset = np.polyfit(t, theta(x,y,z), 1)
plt.plot(t, slope*t+offset)
plt.show()



"""
[freqs, fft_signal] = FFT(t,r)
fig = plt.figure(3)
plt.plot(freqs, np.abs(fft_signal))
plt.title("Frequency domain signal")
plt.xlabel("Frequency (1/day)")
plt.ylabel("Magnitude")
plt.show()

index = np.argmax(np.abs(fft_signal))
print(1/freqs[index])

fig = plt.figure(4)
plt.plot(freqs[0:100], np.abs(fft_signal[0:100]))
plt.title("Frequency domain signal")
plt.xlabel("Frequency (1/day)")
plt.ylabel("Magnitude")
plt.show()
"""