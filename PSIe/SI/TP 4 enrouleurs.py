import numpy as np
import matplotlib.pyplot as plt
def zero_dicho(f,x_min,x_max) :
    deb=x_min
    fin=x_max
    while abs(deb-fin)>10**(-10) :
        m=(deb+fin)/2
        if f(deb)*f(m)<0 :
            fin=m
        elif f(fin)*f(m)<0 :
            deb=m
        elif f(m)!=0 :
            return -100
        else :
            return m
    return m
        
x=125
y_tab=np.linspace(0,600,600)

X_HD=675
Y_HD=775
rd=15
a=50
b=25

def loi_LHD1(L) :
    return L**2-(X_HD-a-x)**2-(Y_HD-b-y)**2-rd**2

L=[]

for y in y_tab :
        L.append(zero_dicho(loi_LHD1,0,1000))
l_th=np.sqrt((X_HD-a-x)**2+(Y_HD-b-y_tab)**2+rd**2)
plt.plot(y_tab,L)
plt.plot(y_tab,l_th)
plt.show()

# for e in theta_HD :
#     if theta_HD[e]!='error' :
#         print(theta_HD)
