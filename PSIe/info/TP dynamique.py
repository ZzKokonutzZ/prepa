M=[
    [1,4,6,8,2],
    [2,4,0,2,4],
    [3,5,0,8,9],
    [8,0,7,6,0],
    [0,9,5,9,1],
    [2,7,5,5,2]
]

def poids_min_rec(M) :
    n=len(M)
    p=len(M[0])
    def cout(i,j) :
        if (i,j) == (n-1,p-1) :
            return M[i][j]
        if i==n-1 :
            return M[i][j]+cout(i,j+1)
        if j==p-1 :
            return M[i][j]+cout(i+1,j)
        else :
            return M[i][j]+min(cout(i+1,j),cout(i,j+1))
    return cout(0,0)

def poids_min_rec_mem(M) :
    n=len(M)
    p=len(M[0])
    tabCout=[]
    for i in range(n) :
        tabCout.append([None]*p)
    def memcout(i,j) :
        if tabCout[i][j]==None :
            if (i,j) == (n-1,p-1) :
                tabCout[i][j] = M[i][j]
            elif i==n-1 :
                tabCout[i][j] = M[i][j]+memcout(i,j+1)
            elif j==p-1 :
                tabCout[i][j] = M[i][j]+memcout(i+1,j)
            else :
                tabCout[i][j] = M[i][j]+min(memcout(i+1,j),memcout(i,j+1))
        return tabCout[i][j]
    return memcout(0,0)

def poids_min_iter(M) :
    n=len(M)
    p=len(M[0])
    tabCout=[[None]*p for _ in range(n)]
    for i in range(1,n+1) :
        for j in range(1,p+1) :
            if (i,j)==(1,1) :
                tabCout[n-i][p-j]=M[n-i][p-j]
            elif i==1 :
                tabCout[n-i][p-j]=M[n-i][p-j]+tabCout[n-i][p-j+1]
            elif j==1 :
                tabCout[n-i][p-j]=M[n-i][p-j]+tabCout[n-i+1][p-j]
            else :
                tabCout[n-i][p-j]=M[n-i][p-j]+min(tabCout[n-i+1][p-j],tabCout[n-i][p-j+1])
    return tabCout[0][0]

def construire_tableaux(M) :
    n=len(M)
    p=len(M[0])
    tabCout=[[None]*p for _ in range(n)]
    tabChoix=[[None]*p for _ in range(n)]
    for i in range(1,n+1) :
        for j in range(1,p+1) :
            if (i,j)==(1,1) :
                tabCout[n-i][p-j]=M[n-i][p-j]
            elif i==1 :
                tabCout[n-i][p-j]=M[n-i][p-j]+tabCout[n-i][p-j+1]
                tabChoix[n-i][p-j]='>'
            elif j==1 :
                tabCout[n-i][p-j]=M[n-i][p-j]+tabCout[n-i+1][p-j]
                tabChoix[n-i][p-j]='V'
            else :
                a=tabCout[n-i+1][p-j]
                b=tabCout[n-i][p-j+1]
                tabCout[n-i][p-j]=M[n-i][p-j]+min(a,b)
                tabChoix[n-i][p-j]='>'*(a>=b)+'V'*(a<b)
    return (tabCout[0][0],tabCout,tabChoix)

def reconstruction_chemin(M) :
    n,p=len(M),len(M[0])
    _,tabCout,tabChoix=construire_tableaux(M)
    l=[]
    i=j=0
    while tabChoix[i][j]!=None :
        l.append((i,j))
        if tabChoix[i][j]=='>' :
            j+=1
        else :
            i+=1
    l.append((n-1,p-1))
    return l

def construire_tableaux_mem(M) :
    n=len(M)
    p=len(M[0])
    tabCout=[]
    for i in range(n) :
        tabCout.append([None]*p)
    tabChoix=[[None]*p for _ in range(n)]
    def memcout(i,j) :
        if tabCout[i][j]==None :
            if (i,j) == (n-1,p-1) :
                tabCout[i][j] = M[i][j]
            elif i==n-1 :
                tabCout[i][j] = M[i][j]+memcout(i,j+1)
                tabChoix[i][j] = '>'
            elif j==p-1 :
                tabCout[i][j] = M[i][j]+memcout(i+1,j)
                tabChoix[i][j] = 'V'
            else :
                a=memcout(i+1,j)
                b=memcout(i,j+1)
                tabCout[i][j] = M[i][j]+min(a,b)
                tabChoix[n-i][p-j]='>'*(a>=b)+'V'*(a<b)
        return tabCout[i][j]
    m=memcout(0,0)
    return (m,tabCout,tabChoix)



