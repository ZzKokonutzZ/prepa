import numpy.random as rd
import numpy as np
import matplotlib.pyplot as plt
N=100000
R1=10**3
R2=2*10**3
u_R1=0.05*R1
u_R2=0.05*R2
tabR1=rd.normal(R1,u_R1,N)
tabR2=rd.normal(R2,u_R2,N)
tab_H=1+tabR2/tabR1
H_moy=np.average(tab_H)
u_H=np.std(tab_H,ddof=1)

print('H_0=',H_moy,'+/-',u_H)
plt.hist(tab_H,bins='rice',histtype='step')
plt.axvline(H_moy,color='r',ls='--')
plt.show()