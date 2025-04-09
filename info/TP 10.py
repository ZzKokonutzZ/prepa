#4 billets de 10, 1 billet de 5, 1 pièce de 2 -> optimale
#2 billets de 20, 3 pièces de 2, 1 pièce de 1...

monnaie_euro=[200,100,50,20,10,5,2,1]

def rendu(somme, monnaie) :
    r=[]
    for e in monnaie :
        while somme>=e :
            somme-=e
            r.append(e)
    return r

print(rendu(43,monnaie_euro))

monnaie_bof=[200,100,50,20,2,1]

print(rendu(63,monnaie_bof))

#la solution n'est pas optimale

monnaie_inca=[30,24,12,6,3,1]

print(rendu(49,monnaie_inca))

#2*12+1

##########################
def i_max(l) :
    i_m=0
    for i in range(len(l)) :
        if l[i]>l[i_m] :
            i_m=i
    return i_m

def eff(l_p,l_v) :
    l_e=[l_v[i]/l_p[i] for i in range(len(l_p))]
    print(l_e)
    return l_e

def sac_a_dos(l_p,l_v,p) :
    l_e=eff(l_p,l_v)
    v_tot=0
    p_tot=0

    while len(l_e)>0 and p-p_tot>max(l_p) :
        i=i_max(l_e)
        p_tot+=l_p[i]
        v_tot+=l_v[i]
        l_e.pop(i)
        l_p.pop(i)
        l_v.pop(i)
    return (p_tot,v_tot)

print(sac_a_dos([13,12,8,10],[70,40,30,30],30))

l_taches=[(1,4),(0,6),(3,5),(12,13),(8,11),(8,12),(3,13),(6,10),(5,9),(4,8),(5,7),(13,16),(15,17),(16,19)]



def mojito(l) :
    t=1
    size=len(l)
    while t!=0 :
        t=0
        for i in range(size-1) :
            if l[i+1][1]<l[i][1] :
                l[i],l[i+1]=l[i+1],l[i]
                t=1
        for i in range(size,0) :
            if l[i-1][1]>l[i][1] :
                l[i-1],l[i]=l[i],l[i-1]
                t=1
        

# l=[(1,5),(2,4),(3,3),(4,2),(5,1)]
# mojito(l)
# print(l)

def len_sort(l) :
    l_aux=[(i,l[i][1]-l[i][0]) for i in range(len(l))]
    mojito(l_aux)
    rep=[]
    for e in l_aux :
        t=1
        for k in rep :
            if k[0]<=l[e[0]][0]<k[1] or k[0]<=l[e[0]][1]<k[1] :
                t=0
                break
        if t :
            rep.append(l[e[0]])
    return rep

def deb_sort(l) :
    l_aux=[(i,l[i][0]) for i in range(len(l))]
    mojito(l_aux)
    rep=[]
    rep.append(l[l_aux[0][0]])
    for e in l_aux :
        if l[e[0]][0]>=rep[-1][1] :
            rep.append(l[e[0]])
    return rep

def fin_sort(l) :
    l_aux=[(i,-l[i][1]) for i in range(len(l))]
    mojito(l_aux)
    rep=[]
    rep.append(l[l_aux[0][0]])
    for e in l_aux :
        if l[e[0]][1]<=rep[-1][0] :
            rep.append(l[e[0]])
    return rep

print(len_sort(l_taches))
print(deb_sort(l_taches))
print(fin_sort(l_taches))