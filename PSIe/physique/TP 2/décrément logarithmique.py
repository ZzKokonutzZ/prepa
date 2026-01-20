import numpy as np
import matplotlib.pyplot as plt
tab=np.loadtxt("pics.txt")
n=np.array([tab[k][0] for k in range(len(tab))])
s_t=np.array([tab[k][1] for k in range(len(tab))])

plt.plot(n,np.log(s_t/s_t[0]))
plt.show()