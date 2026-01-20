import numpy as np
import matplotlib.pyplot as plt

tab=np.loadtxt("frequ res.txt",skiprows=1)

n=tab[:,:1]
nu=tab[:,1:]*10**3

tabv=2*100*nu/n

sigma=np.std(tabv,ddof=1)

u=sigma/np.sqrt(10)
v=np.mean(tabv)
z=np.abs((1.87e8-v)/np.sqrt(u**2+0.7**2))


plt.plot(n,nu,'+r')
plt.show()

tab=np.loadtxt("rho exp.txt",skiprows=1)

tabR=tab[:,:1]
tabA0=tab[:,1:2]
tabAs=tab[:,2:]
tabX=(tabAs+0.8*tabA0)/(0.8*tabA0-tabAs)
plt.plot(tabX,tabR,'*r')
plt.show()

zc=np.mean(tabR/tabX)