# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 21:40:29 2022

@author: Vincent
"""

import numpy as np
import matplotlib.pyplot as plt
from collections import deque

#ATTENTION graphe orienté




###############################################################################


#   Q1 : charger les données


###############################################################################
data_node = np.loadtxt("Nancy_data_node",skiprows=1) #node_id	x	y
data_edge = np.loadtxt("Nancy_data_edges",skiprows=1) # node_idu	node_idv	longueur	vitesse(km/h)	temps de trajet

x = data_node[:,1]  #Attention, x et y sont des listes, choix de nom de var criticable
y = data_node[:,2]

def affiche_ville_lent():
    plt.figure()              
    for edge in data_edge:
        u = int(edge[0])
        v = int(edge[1])        
        plt.plot([x[u],x[v]],[y[u],y[v]],'-k')
    plt.axis("equal")
    #plt.show()
    
    
#affiche_ville_lent()
###############################################################################


#   Q2 : créer les liste adj et matrice d'adj (dico)


liste_adj = [[] for _ in range(len(data_node))]
matrice_adj_long = {}
matrice_adj_vit = {}
matrice_adj_temps = {}
for i,edge in enumerate(data_edge):
    u = int(edge[0])
    v = int(edge[1])
    liste_adj[u].append(v)
    matrice_adj_long[(u,v)] = data_edge[i,2]
    matrice_adj_vit[(u,v)] = data_edge[i,3]
    matrice_adj_temps[(u,v)] = data_edge[i,4]
    



###############################################################################


#   Q9 : test de parcours en profondeur physique comme suggéré par Laurent D.
#        pour l'affichage (un seul plot au lieu de plein de petit plot)


###############################################################################

def DFS_cree_liste_x_et_y(liste_adj,x,y,dep = 0):
    """
    Applique un parcours en profondeur «physique», c'est à dire en revenant sur
    ses pas lorsque l'on prend un autre point pour créer une liste de x et de y
    pour tracer la ville d'un coup plutôt qu'arête par arête. 
    Il y a de la redondance à cause des retours en arrière, mais c'est beaucoup
    plus rapide quand même
    
    prend en arg une liste d'adj, graphe orienté, une liste de x et de y
    correspondant aux coordonnées des différents points.
    """
    n = len(liste_adj)
    pred = [-1] * n #liste des prédécesseurs
    pile = deque()
    liste_x = []
    liste_y = []
    couleur = ["blanc"] * n
    pile.append(dep)
    couleur[dep] = "gris"
    while len(pile)>0:
        actuel = pile[-1]

        test = True
        liste_x.append(x[actuel])
        liste_y.append(y[actuel])
        for voisin in liste_adj[actuel]:
            if couleur[voisin] != "blanc":
                liste_x.append(x[voisin])
                liste_y.append(y[voisin])
                liste_x.append(x[actuel])
                liste_y.append(y[actuel])
                
            if couleur[voisin] == "blanc" and voisin != actuel:#2e condition ajoutée pour éviter les boucles infinis parce que par exemple pour 69, il est son propre voisin (rond point ? erreur dans la base ?)
                couleur[voisin] = "gris"
                pile.append(voisin)
                pred[voisin] = actuel
                test = False
                break
        if test:
            couleur[actuel] = "noir"
            #et il faut revenir en arrière
            actuel = pile.pop()
            while len(pile)>0 and actuel != pile[-1]:
                actuel = pred[actuel]
                liste_x.append(x[actuel])
                liste_y.append(y[actuel])
    return liste_x, liste_y
liste_x,liste_y = DFS_cree_liste_x_et_y(liste_adj,x,y)
def affiche_ville():
    plt.figure()
    plt.plot(liste_x,liste_y,"-k")
    plt.axis("equal")


affiche_ville()
plt.title("ville de Nancy, route")
##lycée HenriPoinca : 48.69158488083465, 6.178569396297109
plt.plot([6.178569396297109],[48.69158488083465],"o")
## don du sang Nancy : 48.68507039315556, 6.197033913695109
plt.plot([ 6.197033913695109],[48.68507039315556],"o")
#plt.show()

poinca=([6.178569396297109],[48.69158488083465])
don_sang=([ 6.197033913695109],[48.68507039315556])

def sommet_proche(x_ref,y_ref) :
    i_min=0
    d_min=(x[i_min]-x_ref)**2+(y[i_min]-y_ref)**2
    for i in range(len(x)) :
        d=(x[i]-x_ref)**2+(y[i]-y_ref)**2
        if d<=d_min :
            d_min=d
            i_min=i
    return i_min

sommet_poinca=sommet_proche(poinca[0],poinca[1])
sommet_don_sang=sommet_proche(don_sang[0],don_sang[1])






###############################################################################


#   Q3 : trouver les sommets les plus proches de Poinca et don du sang 


###############################################################################

# def plus_proche(xp, yp, x, y):
#     #dans les listes x,y trouve l'ind du point le plus proche de xp, yp
#     def distc(x1,y1,x2,y2):
#         #distance au carré
#         return (x1-x2)**2 + (y1-y2)**2
#     imin = ???
#     dmin = ???
#     for i in range(???):
#         d = distc(xp,yp,x[i],y[i])
#         if d < dmin:
#             dmin = ???
#             imin = ???
#     return ???

# id_lycee = plus_proche(6.178569396297109,48.69158488083465,x,y)
# id_don = plus_proche(6.197033913695109,48.68507039315556,x,y)


###############################################################################


#   Q4 : on donne une route par la liste des noeuds, tracer la routes 
# (en supposant pas de problème au niveau des noeuds, c'est à dire que 
# les noeuds successifs correspondent bien à des arêtes)


###############################################################################

route_exemple = [1,8,602,601,586]
def trace_route(route, x, y, couleur = "r"):
    """
    affiche une «route» sur une figure déjà existante 
    (appeler affiche_ville() avant pour avoir la supperposition 
     avec la carte de la ville)
    ------------------------------
    route est une liste de sommets,
    x et y sont les listes des coordonnées créées au début
    couleur est un paramètre optionnel qui permet de paramétrer
                la couleur de la ligne tracée
    """
    liste_x = []
    liste_y = []
    for node in route:
        liste_x.append(x[node])
        liste_y.append(y[node])
    plt.plot(liste_x,liste_y,"-",lw = 4,color = couleur)
trace_route(route_exemple,x,y)








###############################################################################


#   Q5 : trouver le chemin le plus court (distance) depuis le lycée jusqu'au 
#        don du sang et le tracer


###############################################################################



def Dijkstra(dep,arr,mat,list_adj):
    """ 
    dep : indice du sommet de départ
    arr : indice du sommet d'arrivée
    mat : «matrice» (ou dictionnaire) des distances entre sommets, non symétrique car orienté
    list_adj : liste d'adjacence, list_adj[u] = liste des sommets accessibles à partir de u
    """
    n = len(liste_adj)             #nombre de sommets dans le graphe
    couleur = ["blanc"] * n        #gestion des sommets déjà visités
    en_traitement = []             #liste des sommets en attente
    dist = [float("inf")] * n      #distance au sommet de départ trouvée
    predecesseur = [-1] * n        #liste des antécédents pour reconstruire le chemin
    
    #init à partir du sommet de départ
    couleur[dep] = "gris"             #traitement en cours 
    plt.plot([x[dep]],[y[dep]],"o",color="gray")
    dist[dep] = 0
    en_traitement.append(dep)
    #fonction pour trouver le prochain sommet à traiter
    def sommet_min(L,dist):
        #L une liste de sommet, renvoie celui de dist la plus faible, renvoie l'indice dans la liste L ainsi que l'id du noeud
        #on renvoie l'indice dans la liste L pour pouvoir le supprimer
        ind_min = 0
        id_som_min = L[0]
        for i,id_som in enumerate(L):
            if dist[id_som] < dist[id_som_min]:
                id_som_min = id_som
                ind_min = i
        return ind_min,id_som_min
    
    #boucle tant qu'on n'a pas atteint l'arr ou la fin
    while len(en_traitement)>0:
        indi, si = sommet_min(en_traitement,dist) #détermination du sommet de plus petite distance dans la liste en traitement
        del en_traitement[indi] #on le retire de la liste à traiter
        couleur[si] = "noir"  #traitement terminé
        plt.plot([x[si]],[y[si]],"o",color="black")
        if si == arr:
            break #on arrête l'algo
        for sj in list_adj[si]:
            if couleur[sj] != "noir": #voisin non déjà complètement traité
                if couleur[sj] == "blanc": #première fois qu'on le voit
                    couleur[sj] = "gris"
                    plt.plot([x[sj]],[y[sj]],"o",color="gray")
                    en_traitement.append(sj)
                temp = dist[si] + mat[(si,sj)] #distance pour aller à sj en passant par si
                if temp < dist[sj]:
                    dist[sj] = temp
                    predecesseur[sj] = si
    return predecesseur, dist

print(sommet_poinca)
print(sommet_don_sang)
print(len(liste_adj))
pred, dist = Dijkstra(sommet_poinca, sommet_don_sang, matrice_adj_long, liste_adj)

def trouve_route(pred,arr,dep = None):
    """ reconstruit le chemin (liste des sommets) depuis dep jusqu'à arr grâce à
    une liste de predécesseurs (pred) obtenue depuis un algorithme (Dijkstra ou A*)
    """
    id_node = arr   
    res = []
    while id_node != -1:
        res.append(id_node)
        id_node = pred[id_node]
    if len(res) == 0 or ( dep != None and res[-1] != dep):
        print("problème, graphe peut-être non connexe ?")
    return res[::-1] #retourne pour avoir le chemin dans le bon sens
route_lycee_sang = trouve_route(pred,sommet_don_sang,sommet_poinca)




# ###############################################################################


# #   Q6 : trouver le chemin le plus court (temps) depuis le lycée jusqu'au don 
# #        du sang et le tracer


# ###############################################################################
pred2, temps = Dijkstra(sommet_poinca,sommet_don_sang,matrice_adj_temps,liste_adj)

route_lycee_sang2 = trouve_route(pred2,sommet_don_sang,sommet_poinca)
trace_route(route_lycee_sang2,x,y,couleur = "b")
trace_route(route_lycee_sang,x,y)
plt.title("chemin le moins long(dist) en rouge, plus court(temps) en bleu")






###############################################################################


#   Q7 : modifie l'algo de Dijkstra pour afficher les noeuds visités
#        


###############################################################################



# def Dijkstra_affiche_noeud(dep,arr,mat,list_adj):
#     n = len(liste_adj)
#     couleur = ["blanc"] * n
#     en_traitement = []
#     dist = [float("inf")] * n
#     predecesseur = [-1] * n
    
#     #init à partir du sommet de départ
#     couleur[dep] = "gris"
#     dist[dep] = 0
#     en_traitement.append(dep)
#     #fonction pour trouver le prochain sommet à traiter
#     def sommet_min(L,dist):
#         #L une liste de sommet, renvoie celui de dist la plus faible
#         ind_min = 0
#         id_som_min = L[0]
#         for i,id_som in enumerate(L):
#             if dist[id_som]< dist[id_som_min]:
#                 id_som_min = id_som
#                 ind_min = i
#         return ind_min,id_som_min
#     #boucle tant qu'on n'a pas atteint l'arr ou la fin
#     while len(en_traitement)>0:
#         indi,si = sommet_min(en_traitement,dist)
#         del en_traitement[indi]
#         couleur[si] = "noir"
#         plt.plot([x[???]],[y[???]],"ko")
#         if si == arr:
#             break #on arrête l'algo
#         for sj in list_adj[si]:
#             if couleur[sj] != "noir":
#                 if couleur[sj] == "blanc": #première fois qu'on le voit
#                     couleur[sj] = "gris"
#                     plt.plot([x[???]],[y[???]],"o",mfc = [0.5, 0.5, 0.5])
#                     en_traitement.append(sj)
#                 temp = dist[si] + mat[(si,sj)]
#                 if temp < dist[sj]:
#                     dist[sj] = temp
#                     predecesseur[sj] = si
#     return predecesseur, dist

# affiche_ville()
# pred3, dist3 = Dijkstra_affiche_noeud(id_lycee, id_don, matrice_adj_long, liste_adj)

# plt.title("noeuds explorés par Dijkstra")


###############################################################################


#   Q8 : modifie l'algo de Dijkstra pour avoir A^* avec l'heuristique à vol 
#        d'oiseau. Attention, les coord x,y sont en fait des angles en degrés
#        (latitude, longitude) et il faut donc utiliser une conversion en rad
#        et le rayon de la Terre pour avoir une distance


###############################################################################

def dist_oiseau(u,v):
    """ renvoie la distance en mètre à vol d'oiseau entre les sommets u et v
    attention, les listes x et y représente en fait des angles (longitude et
    latitude) et une conversion est donc nécessaire
    """
    #conversion en rad puis m ; 
    Rt  = 6371*10**3
    yu_rad=y[u]*np.pi/180
    yv_rad=y[v]*np.pi/180
    xu =  x[u] * np.sin(yu_rad) * Rt *np.pi/180
    yu =  yu_rad *Rt
    xv =  x[v] * np.sin(yv_rad) *Rt *np.pi/180
    yv =  yv_rad *Rt
    return np.sqrt((xu-xv) ** 2 + (yu - yv)**2)
#print(dist_oiseau(1,8))
    

def A_etoile(dep,arr,mat,list_adj):
    n = len(liste_adj)
    couleur = ["blanc"] * n
    en_traitement = []
    dist = [float("inf")] * n
    predecesseur = [-1] * n
    
    #init à partir du sommet de départ
    couleur[dep] = "gris"
    dist[dep] = 0
    en_traitement.append(dep)
    #fonction pour trouver le prochain sommet à traiter
    #en tenant compte de la distance réellement parcourue et de l'estimation
    #de la distance restante à parcourir
    def sommet_min(L,dist,arr):
        #L une liste de sommet, renvoie celui de dist la plus faible 
        #(au sens distance réelle + estimation)
        ind_min = 0
        id_som_min = L[0]
        for i,id_som in enumerate(L):
            if dist[id_som]+dist_oiseau(id_som,arr) <= dist[id_som_min]+dist_oiseau(id_som_min,arr) :
                id_som_min = id_som
                ind_min = i
        return ind_min,id_som_min
    #boucle tant qu'on n'a pas atteint l'arr ou la fin
    while len(en_traitement)>0:
        indi,si = sommet_min(en_traitement,dist,arr)
        del en_traitement[indi]
        couleur[si] = "noir"
        plt.plot([x[si]],[y[si]],"ko")
        if si == arr:
            break #on arrête l'algo
        for sj in list_adj[si]:
            if couleur[sj] != "noir":
                if couleur[sj] == "blanc": #première fois qu'on le voit
                    couleur[sj] = "gris"
                    plt.plot([x[sj]],[y[sj]],"o",mfc = [0.5, 0.5, 0.5])
                    en_traitement.append(sj)
                temp = dist[si] + mat[(si,sj)]
                if temp < dist[sj]:
                    dist[sj] = temp
                    predecesseur[sj] = si
    return predecesseur, dist


affiche_ville()
pred4, dist4 = A_etoile(sommet_poinca, sommet_don_sang, matrice_adj_long, liste_adj)

route_lycee_sang = trouve_route(pred4,sommet_don_sang,sommet_poinca)
trace_route(route_lycee_sang,x,y)
plt.title("noeuds explorés par A^*")

plt.show()


def affiche_ville_rec(x,y,l_adj) :
    l_x=[]
    l_y=[]
    traites=[]
    def recDFS() :
        


