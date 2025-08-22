def perrier(l) :
    t=0
    k=0
    size=len(l)
    while (not t) or k<size :
        t=0
        for i in range(size-1-k) :
            if l[i]>=l[i+1] :
                l[i],l[i+1]=l[i+1],l[i]
                t=1
        k+=1

def sampellegrino(l) :
    for i in range(len(l)) :
        for j in range(len(l-1-i)) :
                if l[i]>=l[i+1] :
                    l[i],l[i+1]=l[i+1],l[i]

def scweppes(l) :
    t=0
    deb=0
    fin=len(l)-1
    while deb!=fin and t!=0 :
        for i in range(deb,fin) :
            if l[i]>=l[i+1] :
                l[i],l[i+1]=l[i+1],l[i]
                t=1
        fin-=1
        for i in range(fin,deb) :
            if l[i]>=l[i+1] :
                l[i],l[i+1]=l[i+1],l[i]
                t=1
        deb+=1