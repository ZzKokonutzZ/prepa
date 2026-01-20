import numpy as np
import matplotlib.pyplot as plt

C=100*10**-12 #F
R=50 #ohms

donnees=np.loadtxt('donnees.txt',skiprows=1)
t_i=donnees[:,0]
s=donnees[:,1]
x=t_i
y=np.log(s[0]/s)
x_ref=x[1:]
y_ref=y[1:]
tab=y_ref/x_ref
A=np.mean(tab)

sigma_exp=np.std(tab,ddof=1)

u_A=sigma_exp/len(tab)**0.5

y_th=A*x
print('A:',A)
print('u_A:',u_A)
plt.plot(x,y,'r+',label='points expérimentaux')
plt.plot(x,y_th)
plt.figure()
plt.plot(x_ref,tab,'r+')
plt.axhline(y=A)
plt.show()