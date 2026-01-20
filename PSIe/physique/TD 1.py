import numpy as np
import matplotlib.pyplot as plt
R=10
L=10*10**-3
E=10
tau=L/R
t=np.linspace(0,5*tau,1000)
dt=5*tau/1000
# i=[0]
# for k in range(999) :
#     i.append(i[k]+(E-R*i[k])/L*dt)

# i_th=E/R*(1-np.exp(-t/tau))

# plt.plot(t,i)
# plt.plot(t,i_th)
# plt.show()
K=0.001
i=[E/R]
for k in range(999) :
    i.append(i[k]-(R*i[k]+np.sqrt(i[k]/K))/L*dt)

plt.plot(t,i)
plt.show()