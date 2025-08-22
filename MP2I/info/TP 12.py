from random import randint
import numpy as np
from matplotlib import pyplot as plt
from time import perf_counter as t
def mini(L) :
    i_min=0
    for i in range(len(L)) :
        if L[i]<L[i_min] :
            i_min=i
    return (i_min,L[i_min])

def tri_selection1(L) :
    new=[]
    while len(L)>0 :
        i,e=mini(L)
        new.append(e)
        del L[i]
    return new

L=[randint(0,500) for N in range(25)]
print(tri_selection1(L))

#ce tri n'est pas en place
#tri_selection1 est stable

#Q7 : tri stable
# n=np.linspace(1,100)
# plt.loglog(n,n**4)
# plt.show()

#Q8 log

# def tri_insertion1(L) :
#     for k,v in enumerate(L) :
#         j=k
#         while j>0 and v<L[j-1] :
#             L[j]=L[j-1]
#             j=j-1
#         L[j]=v
#     return L

# perfs_selection=[]
# perfs_insertion=[]

# for n in range(1000) :
#     l1=[randint(0,1000) for i in range(n)]
#     l2=[randint(0,1000) for i in range(n)]
    
#     t1=t()
#     tri_selection1(l1)
#     t2=t()
#     perfs_selection.append(t2-t1)
    
#     t1=t()
#     tri_insertion1(l2)
#     t2=t()
#     perfs_insertion.append(t2-t1)

# n=np.linspace(1,1000,1000)

# plt.loglog(n,perfs_selection)
# plt.loglog(n,perfs_insertion)
# plt.show()
    
def fusion(L11,L22) :
    L2=L22[:]
    L1=L11[:]
    new=[]
    while len(L1)>0 or len(L2)>0 :
        if len(L1)>0 and len(L2)>0 :
            if L1[0]<=L2[0] :
                new.append(L1[0])
                del L1[0]
            else :
                new.append(L2[0])
                del L2[0]
        else :
            if len(L1)==0 :
                new.append(L2[0])
                del L2[0]
            else :
                new.append(L1[0])
                del L1[0]
    return new

def tri_fusion(L) :
    l=len(L)
    if l <= 1 :
        return L
    else :
        return fusion(tri_fusion(L[:l//2]),tri_fusion(L[l//2:]))
#print(tri_fusion(L))
print(fusion([1,2,3],[2,5,9]))
