import numpy as np
import matplotlib.pyplot as plt
from numpy.fft import rfft,rfftfreq
import numpy.random as rd
S=10**-2*2*10**-2
l=np.pi*5*10**-2
V=S*l
N1=141
N2=1802
r=50
R=10**6
C=10**-6
f=50
Ta=20*10**-3
fe=10*10**3
Ne=int(Ta*fe)
Te=1/fe
mu0=4*np.pi*10**-7

data=np.loadtxt("courbes B H.txt",skiprows=1)

t=data[:,0]
x=data[:,1]
y=data[:,3]
i=x/r
tabSpectre=abs(rfft(x/r)/(Ne/2))
tabFreq=rfftfreq(Ne,Te)
B=-y*R*C/(N2*S)
H=N1*x/(r*l)

plt.plot(t,x,'+')
plt.plot(t,y,'+')
plt.figure()
plt.plot(tabFreq,tabSpectre)
plt.xlim([0,1000])
plt.figure()
plt.plot(H,B,'+r')
i_min=0
H_min=abs(H[0])
for i in range(Ne) :
    H_i=abs(H[i])
    if H_i<H_min :
        i_min=i
        H_min=H_i
Br=abs(B[i_min])
print(f'Br = {Br} T')
M=B/mu0-H
plt.figure()
plt.plot(H,M,'+')
plt.show()

A=0
for i in range(Ne-1) :
    dB=B[i+1]-B[i]
    H_i=(H[i]+H[i+1])/2
    dA=H_i*dB
    A+=dA
Phys_vol=f*A
print(f"pertes volumiques par hystérésis : {A} J/m^3 || {Phys_vol} W/m^3")

D_u=0.025
N=10000
tabD_u=np.array([0.025 for _ in range(Ne)])
tabPhys=[]
tabA=[]
for i in range(N) :
    x_i=x+rd.uniform(-tabD_u,tabD_u)
    y_i=y+rd.uniform(-tabD_u,tabD_u)
    B_i=-y_i*R*C/(N2*S)
    H_i=N1*x_i/(r*l)
    A=0
    for k in range(Ne-1) :
        dB=B_i[k+1]-B_i[k]
        H_k=(H_i[k]+H_i[k+1])/2
        dA=H_k*dB
        A+=dA
    Phys_vol=f*A
    tabA.append(A)
    tabPhys.append(Phys_vol)
u_Phys=np.std(tabPhys,ddof=1)
u_A=np.std(tabA,ddof=1)
print(f"u_A={u_A}")
print(f"u_Phys_vol={u_Phys}")
    