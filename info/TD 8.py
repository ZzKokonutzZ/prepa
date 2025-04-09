k=0
def fibo_naïf(n) :
    global k
    k+=1
    if n<=1 :
        return n
    else :
        return fibo_naïf(n-1)+fibo_naïf(n-2)
    
    

fibo_naïf(10)
print(k)

#nombre d'appels : O(2^n-1)
t=0
def rec_fibo(a,b,k,n) :
    global t
    t+=1
    if k==n : 
        return a
    else :
        return rec_fibo(b,a+b,k+1,n)

def fibo(n) :
    return rec_fibo(0,1,0,n)

fibo(10)
print(t)

def binom(n,k) :
    if n==0 and k==0 :
        return 1
    elif k<0 or n<k :
        return 0
    else :
        return binom(n-1,k)+binom(n-1,k-1)

def rec_in(x,L) :
    if len(L)==1 and L[0]!=x :
        return False
    e=L[len(L)//2]
    if e==x :
        return True
    elif x<e :
        return rec_in(x,L[:len(L)//2])
    else :
        return rec_in(x,L[len(L)//2:])
    
#def rec_in_annexe(x,L,d,f):

    
print(rec_in(2,[1,3,5,7,9]))
    
    
def fastexp(a,b) :
    if b==0 :
        return 1
    elif b%2==0:
        return fastexp(a*a,b//2)
    else :
        return a*fastexp(a,b-1)

# def monoï(L) :
    
#     def move(n,p1,p2,p3) :
#         if n==len(L[p1])-1 :
#             if len(L[p2])==0 or L[p1][n]<L[p2][-1] :
#                 L[p2].append(L[p1].pop())
#             else :
#                 move(len(L[p2])-1,p2,p3,p1)
#                 move(n,p1,p2,p3)
#         else :
#             move(n+1,p1,p3,p2)
#             move(n,p1,p2,p3)
    
#     while len(L[0])!=0 or len(L[1])!=0 :
#         if len(L[1])==0 :
#             move(0,0,2,1)
#         elif len(L) :
#             move(0,1,2,0)
#     return L
            
# print(monoï([[3,2,1],[],[]]))

def hanoi(L) :
    
    def solve(n,p1,p2,p3) :
        if n==1 :
            L[p2].append(L[p1].pop())
            print(L)
        else :
            solve(n-1,p1,p3,p2)
            L[p2].append(L[p1].pop())
            print(L)
            solve(n-1,p3,p2,p1)
    
    solve(len(L[0]),0,2,1)
    return L
#print(hanoi([[3,2,1],[],[]]))


# def perm(L) :
#     def auxperm(l) :
#         if len(l)==0 :
#             return []
#         else :
#             t=[]
#             for e in l :
#                 templ=auxperm(l[:].remove(e))
#                 for i in range(len(templ)) :
#                     t+=[e]+templ[i]
#             return t
    
#     return auxperm(L)
# perm([1,2,3])

def perm2(L) :
    def auxperm2(l) :
        if len(l)<=1 :
            return [l]
        else :
            templ=auxperm2(l[1:])
            newl=[]
            for i in range(len(templ)) :
                for j in range(len(templ[i])+1):
                    newl+=[templ[i][:j]+[l[0]]+templ[i][j:]]
            return newl
    
    return auxperm2(L)

print(perm2([1,2,3]))

