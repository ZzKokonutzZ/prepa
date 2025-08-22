import numpy as np
import matplotlib.pyplot as plt
pKa1,pKa2=6.4,10.3

def alpha(pH) :
    return 1/(1+10**(pH-pKa1)+10**(2*pH-pKa1-pKa2))

def beta(pH) :
    return 1/(10**(pKa1-pH)+1+10**(pH-pKa2))
 
def gamma(pH) :
    return 1/(10**(-2*pH+pKa1+pKa2)+10**(pKa2-pH)+1)

pH=np.linspace(0,14,100)
plt.plot(pH,alpha(pH),'r',label='H2CO3')
plt.plot(pH,beta(pH),'g',label='HCO3-')
plt.plot(pH,gamma(pH),'b',label='CO32-')
plt.show()