import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

############################ initialisation #############################

nbmesures=5 #nombre de fichiers donnees
nbpoints=1 #nombre de points par échelon de commande

mesures=[] #tableau des mesures du format [[[commandes],[valeurs mesurées]],[[commandes],[valeurs mesurées]],...]

########################### récupération des données ##########################

for i in range(nbmesures) :
    tab=np.loadtxt(f"donnees{i}.txt")
    tabcommande=[]
    tabcapteur=[]
    for i in range(len(tab)//nbpoints) :
        
        commande=tab[nbpoints*i][1]
        capteur=np.mean(tab[nbpoints*i:nbpoints*(i+1),:1])
        tabcommande.append(commande)
        tabcapteur.append(capteur)
    mesures.append([tabcommande[:],tabcapteur[:]])
plt.figure(0)
for i in range(nbmesures) :
    plt.plot(mesures[i][0],mesures[i][1],'+',label=f"mesure {i}")

plt.title("données brutes")
plt.xlabel("commande")
plt.ylabel("valeurs mesurées (UA)")
#plt.legend()



######################### traitement des données ##########################
    ### 0 : redressement des données et troncage de la saturation ###

seuil=1750 #à confirmer au stroboscope

imax=mesures[1][0].index(seuil)+1



for i in range(nbmesures) :
    while len(mesures[i][0])>imax :
        mesures[i][0].pop(-1)
        mesures[i][1].pop(-1)
for e in mesures :
    print(e)
    print()
commande_ref=np.array(mesures[1][0][:])

coef_etalonnage=2.114374434249408e-05 #à définir expérimentalement

for i in range(nbmesures) :
    for j in range(imax) :
        mesures[i][1][j]=coef_etalonnage*(mesures[i][1][j]-5.607133674736671)

plt.figure(1)
for i in range(nbmesures) :
    plt.plot(mesures[i][0],mesures[i][1],'+',label=f"mesure {i}")

plt.title("données redressées et tronquées")
plt.xlabel("commande")
plt.ylabel("valeurs mesurées (N)")
#plt.legend()


    ### I : élimination des valeurs abherrantes ###

#calcul de la moyenne et de l'écart-type
mesure_moyenne=[]
m=0
for i in range(imax) :
    m=sum([mesures[k][1][i] for k in range(nbmesures)])/nbmesures
    mesure_moyenne.append(m)

m=0
for i in range(nbmesures) :
   m+=np.std([mesures[i][1][k]-mesure_moyenne[k] for k in range(imax)],ddof=1) 
ecart_type_moyen=m/nbmesures

a,b,c=np.polyfit(commande_ref,mesure_moyenne,2)
modele_brut=np.array([a*commande_ref[i]**2+b*commande_ref[i]+c for i in range(imax)])


#élimination des valeurs abherrantes
coef_abherration=3

plt.figure(2)
for i in range(nbmesures) :
    plt.plot(mesures[i][0],mesures[i][1],'+')

plt.plot(commande_ref,modele_brut,color='blue',label="modèle quadratique brut")
plt.plot(commande_ref,modele_brut+coef_abherration*ecart_type_moyen,linestyle='dotted',color='red',label="modèle + écart-type*coefficient d'abherration")
plt.plot(commande_ref,modele_brut-coef_abherration*ecart_type_moyen,linestyle='dotted',color='red')



for i in range(nbmesures) :
    j_trash=[]
    for j in range(imax) :
        if abs(mesures[i][1][j]-modele_brut[j])>ecart_type_moyen*coef_abherration :
            j_trash.append(j)
    for k in range(len(j_trash)) :
        x=mesures[i][0].pop(j_trash[k]-k)
        y=mesures[i][1].pop(j_trash[k]-k)
        plt.plot(x,y,'+r')

plt.title("valeurs abherrantes")
plt.ylabel("force (N)")
plt.xlabel("commande")
#plt.legend()

    ### II détermination des modèles linéaires et quadratiques sur les données traitées ###
#moyenne des mesures filtrées
mesuref_moyenne=[]
for i in range(imax) :
    m=0
    nb=0
    for j in range(nbmesures) :
        print(f'mesures {j} : {mesures[j][0]}')
        if commande_ref[i] in mesures[j][0] :
            i_commande=mesures[j][0].index(commande_ref[i])
            m+=mesures[j][1][i_commande]
            nb+=1
    assert nb>0, f"commande_ref : {commande_ref[i]}"
    mesuref_moyenne.append(m/nb)
mesuref_moyenne=np.array(mesuref_moyenne)

plt.plot(commande_ref,mesuref_moyenne,'+',color='black')

plt.figure(3)
for i in range(nbmesures) :
    plt.plot(mesures[i][0],mesures[i][1],'+')
plt.plot(commande_ref,mesuref_moyenne,'+',color='black')

#modèle linéaire :
k,N0=np.polyfit(commande_ref,mesuref_moyenne,1)
plt.plot(commande_ref,k*commande_ref+N0,color='blue',label='modèle linéaire')

#modèle quadratique :
a,b,c=np.polyfit(commande_ref,mesuref_moyenne,2)
print(a)
print(b)
print(c)
plt.plot(commande_ref,a*commande_ref*commande_ref+b*commande_ref+c,color='red',label='modèle quadratique')

plt.title('modèles quadratiques et linéaires')


plt.xlabel('commande')
plt.ylabel('force (N)')
#plt.legend()

plt.figure(4)
plt.title('écarts au modèle')
fig,(ax1,ax2)=plt.subplots(2)
ax1.set_title('modèle linéaire')
for i in range(nbmesures) :
    ax1.plot(mesures[i][0],mesures[i][1]-k*np.array(mesures[i][0])-N0,'+')
ax1.plot(commande_ref,mesuref_moyenne-k*commande_ref-N0,'+',color='black')

ax1.plot(commande_ref,np.zeros(len(commande_ref)),color='blue')

ax1.set_xlabel('commande')
ax1.set_ylabel('force (N)')

ax2.set_title('modèle quadratique')
for i in range(nbmesures) :
    ax2.plot(mesures[i][0],mesures[i][1]-a*np.array(mesures[i][0])**2-b*np.array(mesures[i][0])-c,'+')
ax2.plot(commande_ref,mesuref_moyenne-a*commande_ref*commande_ref-b*commande_ref-c,'+',color='black')

ax2.plot(commande_ref,np.zeros(len(commande_ref)),color='red')

ax2.set_xlabel('commande')
ax2.set_ylabel('force (N)')

#plt.legend()

commande_lin=commande_ref[:]
mesure_lin=a*commande_ref[:]*commande_ref[:]+b*commande_ref[:]+c
r=0
n_min=len(commande_lin)
while r<0.99 and len(commande_lin)!=0 :
    commande_lin=commande_lin[:-1]
    mesure_lin=mesure_lin[:-1]
    n_min-=1
    a_lin,b_lin,r,trash1,trash2=linregress(commande_lin,mesure_lin)
print(n_min)

if len(commande_lin) ==0 :
    print('dommage...')
else :
    plt.figure(6)
    plt.plot(commande_lin,mesure_lin,'+')
    plt.plot(commande_lin,a_lin*commande_lin+b_lin)
plt.show()