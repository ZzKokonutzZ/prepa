import numpy as np
import matplotlib.pyplot as plt
U=np.array( [1.02, 1.51, 1.98, 2.47, 3.05, 3.50, 3.97, 4.63, 5.00, 5.52, 6.03, 7.04, 7.62])
I=np.array( [1.2, 2.4, 3.4, 5.2, 7.4, 10.0, 12.5, 17.7, 20.6, 26.2, 32.0, 47.5, 59.8])
plt.plot(np.log(U),np.log(I))
# print(np.polyfit(np.log(U) ,np.log(I),1,full=True))
(alpha,lnK),(residu),a,b,c=np.polyfit(np.log(U) ,np.log(I),1,full=True)
print(residu)
plt.plot(np.log(U),alpha*np.log(U)+lnK)
plt.show()