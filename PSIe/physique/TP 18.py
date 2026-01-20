import numpy as np
import  matplotlib.pyplot as plt
donnees=np.loadtxt("conductivite.txt")
V=donnees[:,0]
sigma=donnees[:,1]
plt.plot(V,sigma,'+')
D_V=[np.sqrt(0.1**2+0.05**2)]
plt.errorbar(V,sigma,yerr=0.002*sigma+0.3,xerr=[D_V for _ in range(len(sigma))],fmt='+r')
plt.grid()
plt.show()
c0=0.01
D_c0=0.0005
V0=20
D_V0=0.03

Veq=12
C_Ba=c0*Veq/(2*V0)
print(C_Ba)
Vmin=7.9
Vmax=12.6
N=10000
tabc0=np.random.uniform(c0-D_c0,c0+D_c0,N)
tabV0=np.random.uniform(V0-D_V0,V0+D_V0,N)
tabVeq=np.random.uniform(Vmin,Vmax,N)
tabC=tabc0*tabVeq/(2*tabV0)
u_C=np.std(tabC,ddof=1)
print(f'C={C_Ba}+/-{u_C}')

Veq_c=7.9
C_I2=c0*Veq_c/(6*V0)
Ks=C_Ba*C_I2**2
print(Ks)
