import matplotlib.pyplot as plt
import numpy as np
T_n=[]
n_values=[i for i in range(1,50,5)]
L=1
g=9.81
theta_0=np.pi/180*2

def f(x) :
    return np.sqrt(3*g/L*(np.cos(theta_0)-np.cos(x)))

for n in n_values:
    theta=np.linspace(theta_0,np.pi/2,n)
    omega=[]
    for i in range(len(theta)-1) :
        omega.append(f((theta[i]+theta[i+1])/2))

    T_n.append((np.pi/2-theta_0)/n*np.sum(omega))

plt.plot(n_values,T_n)
plt.show()
    
