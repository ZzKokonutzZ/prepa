#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 10 11:01:22 2025

@author: dardevet
"""

from random import randint
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap, LinearSegmentedColormap
colors = ['blue','white', 'red']
custom_cmap = LinearSegmentedColormap.from_list('blue_white_red', colors)

"""
Données pour exercice 1
"""
Xdata = np.loadtxt('dataChiffres.txt').tolist()

print(len(Xdata))
print(len(Xdata[0]))
"""
Fonctions
"""

def d(x:list, y:list)-> float: 
    """
    x,y: deux vecteurs (liste) de dimension p
    renvoie la distance euclidienne entre x et y
    """
    p = len(x)	# dimension des données
    somme = 0	# initialisation accumulateur
    
    for i in range(p):
        somme += (x[i]-y[i])**2
    return somme**0.5
    

def plusProche(x: list, centres: list)-> int:
    """
    x : vecteur donnée de dimension p
    centres: liste des k-centres
    renvoie l'indice i du centre de la classe $i$ le plus proche de x.
    """
    imin = 0
    k = len(centres) # nombre de centre
    
    for i in range(k): # parcours des k centres
        if d(x, centres[i]) < d(x, centres[imin]): # recherche du plus proche
            imin = i
    return imin


""" 
A vous de jouer
"""

def initialisation(X: list, k: int)-> list:
    """
    X: liste de liste, ensemble de vecteurs (données)
    k : nombre de centre
    renvoie la liste des classes tirées au hasard
    """
    Y=[]
    for i in range(len(X)) :
        Y.append(randint(0,k-1))

    return Y


def calculerCentres(X: list, Y: list, k: int)-> list:
    """
    X: liste de listes, ensemble de vecteurs (données)
    Y: liste des étiquettes associées
    k:nombre de centres / de classe
    renvoie la liste des centres
    """
    n=len(X)
    p=len(X[0])
    centres=[[0]*p for _ in range(k)]
   
    nbc=[0]*k
    for i in range(n) :
        ci=Y[i]
        for j in range(p) :
            centres[ci][j]+=X[i][j]
        nbc[ci]+=1
    for i in range(k):
        if nbc[i]!=0 :
            for j in range(p) :
                centres[i][j]/=nbc[i]
    return centres

#ligne de test
Ydata=initialisation(Xdata, 10)
print(Ydata)
print(calculerCentres(Xdata, Ydata, 10))


def calculerClasses(X: list, centres:list)->int:
    """
    X: liste de liste, ensemble de vecteurs (données)
    centres: liste des k-centres
    renvoie la liste Y contenant les données par classe
    """
    n=len(X)
    Y=[None]*n
    for i in range(n) :
        Y[i]=plusProche(X[i], centres)
    return Y


def kmeans(X, k):
    """
    X: liste de liste, ensemble de vecteurs (données)
    centres : liste des k-centres initiaux
    renvoie la liste de liste classes, contenant les données par classe
    """
    centres=calculerCentres(Xdata,initialisation(X, k),k)
    Y=calculerClasses(X, centres)
    centres2=centres
    centres=calculerCentres(X, Y, k)
    while centres!=centres2 :
        centres2=centres
        Y=calculerClasses(X, centres2)
        centres=calculerCentres(X, Y, k)

    return Y, centres

# classes,centres=kmeans(Xdata,10)

# print(classes,centres)

def inertie(X, Y, centres):
    """
    classes: liste de liste, ensemble des données par classe
    centres : liste des k-centres 
    renvoie l'inertie I
    """
    I = 0 # initialisation de l'inertie
    n = len(X)  # nombre de données
    for i in range(n) :
        I+=d(X[i],centres[Y[i]])**2

    return I

# print(inertie(Xdata,classes,centres))

# I=[]
# for k in range(5,16) :
#     Y,centres=kmeans(Xdata,k)
#     I.append(inertie(Xdata,Y,centres))
# plt.plot([k for k in range(5,16)],I,'.')




def conversion(x:list)->list:
    n = int(len(x)**0.5)
    Mat=[[x[n*i+j] for j in range(n)] for i in range(n)]

    return Mat    

   
def afficherImage(M: list)-> list:
    plt.imshow(M, cmap='binary')
    plt.show()
    
# afficherImage(conversion(Xdata[0]))

# Y,centres=kmeans(Xdata, 10)
# for i in range(10) :
#     afficherImage(conversion(centres[i]))
"""
Exercice 2
"""
from PIL import Image

im = Image.open('montbeliarde_minus.jpg') # environ 10000 pixels
im.show()


nbCouleurs = 3

def reduit_image(im, nbCouleurs) :
    
    T = np.array(im) # transforme l'image en tableau numpy
    nl, nc , _ = np.shape(T) # nb de lignes et de colonnes
    T = T.tolist() # conversion en liste de liste
    
    # On aplatit la tableau
    pixels = []
    for i in range(nl) :
        for j in range(nc):
            pixels.append(T[i][j])
    
    etiquettes, palette = kmeans(pixels,nbCouleurs)
    
    #  tableau applati des nouveaux pixels
    
    nouvPixels = []
    for i in range(nl*nc) :
        nouvPixels.append(palette[etiquettes[i]])
    
    # tableau rectangul des nouveaux  triplets (n_l lignes, n_c colonnes)
    nouvT = [[nouvPixels[nc*i+j] for j in range(nc)] for i in range(nl)]
    
    # nouvelle image 
    nouv_im = Image.fromarray(np.uint8(nouvT), 'RGB')
    return nouv_im

nouvImage = reduit_image(im, nbCouleurs)
nouvImage.show()



