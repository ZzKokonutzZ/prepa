from graph import *
import numpy as np
r=np.pi/180
alpha=np.array([10*r,20*r,30*r,40*r,50*r,60*r,65*r])
I=np.array([0.17,0.33,0.48,0.71,1.06,1.49,1.90])
muze=4*np.pi*10**-7
R=12*10**-2
N=5
B_1=muze*N*I/(2*R)
B_2=B_1/np.tan(alpha)

I_S=[0.87,1.07,1.27,1.98]

BTS=[]

for i in range(len(I_S)) :
    N=i+1
    BTS.append(muze*N*I_S[i]/(2*R))


print("B_T alpha : ",np.sum(B_2)/7)

print("B_T spire : ",np.sum(BTS)/7)

print(B_2)

print(lr_graph(np.linspace(2,5,4),BTS))