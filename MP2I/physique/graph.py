import numpy as np
from matplotlib import pyplot as plt
def lr_graph(x,y) :
    plt.plot(x,y)
    plt.show()
    a,b=np.polyfit(x,y,1)
    return (a,b)