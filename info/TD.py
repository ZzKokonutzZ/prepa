
def appartient(x,l) :
    for i in range(len(l)) :
        if x==l[i] :
            return True
    return False

def suppr_doublon(l) :
    d=[]
    for i in range(len(l)) :
        if not appartient(l[i],d) :
            d.append(l[i])
    return d

def multiple7(l) :
    m=[]
    for i in range(len(l)) :
        if not l[i]%7 :
            m.append(l[i])
    return m

def somme_carre(n,m) :
    s=0
    for i in range(1,n+1) :
        for j in range(1,m+1) :
            s+=(i+j)**2

def maxi2a(L) :
    m=0
    for i in range(len(L)):
        if L[m]<L[i]:
            m=i
    return m

def maxi2a(L) :
    m=0
    for i in range(len(L)):
        if L[m]<=L[i]:
            m=i
    return m

def syracuseNext(u) :
    if u%2!=0 :
        return 3*u+1
    else :
        return u//2

def syracuseTempsDeVol(p) :
    u=p
    i=0
    while u!=1 :
        u=syracuseNext(u)
        i+=1
    return i
        
def syracuseTempsDeVolEnAltitude(p) :
    u=syracuseNext(p)
    i=1
    while p<=u :
        u=syracuseNext(u)
        i+=1
    return i-1
def f(mu,x) :
    return mu*x*(1-x)
def limite(mu,x_0) :
    x_n=x_0
    x_n1=f(x_0)
    i=0
    while abs(x_n1-x_n)>10e-6 :
        x_n=x_n1
        x_n1=f(x_n1)
    return x_n

def plus_grand_n(N) :
    i=0
    s=0
    while s<=N :
        i+=1
        s+=i**2
    return i-1

d={}
d["k"]="v"
d["k"]="v2"

# x in dict : teste si x appartient aux clés du dictionnaire
# for a in d : a itère sur toutes les clés du dictionnaire

from random import randint

def permut_alea(l) :
    for i in range(len(l),0,-1) :
        j=randint(0,i)
        l[i],l[j]=l[j],l[i]

    return l

def cree_dico(noms) :
    l=len(noms)
    d={}
    for i in range(l) :
        d[noms[i]]=d[noms[(i+1)%l]]

def trouve_espace(ch) :
    spaces=[]
    for i in range(len(ch)) :
        if ch[i]==' ' :
            spaces.append(i)
    return spaces

def coupe_chaine(ch) :
    spaces=[0]
    spaces+=trouve_espace(ch)
    spaces.append(len(ch))
    words=[]
    for i in range(len(spaces)-1) :
        word=""
        if spaces[i+1]-spaces[i]>1 :
            for j in range(spaces[i],spaces[i+1]) :
                word+=ch[j]
        words.append(word)

    return words

def envoie_mail(d,nom_fichier) :
    f=open(nom_fichier,"r")
    liste=f.readlines()
    f.close()
    for e in liste :
        adnom=coupe_chaine(e)
        if adnom[0] in d :
            mail(adnom[1],d[adnom[0]])
   




    


