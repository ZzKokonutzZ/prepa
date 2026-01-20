import matplotlib.pyplot as plt
import numpy as np
x = 125
XHD = 675
YHD = 775
a = 50
b = 25
y_tab = np.linspace(0, 600)
L_min = 0
L_max = 1200
rp = 15


def f(L):
    return (XHD-a-x)**2+(YHD-b-y)**2-rp**2-L**2


LHD = []
for y in y_tab:
    deb = L_min
    fin = L_max
    while fin-deb > 10e-6:
        m = (deb+fin)/2
        if f(deb)*f(m) < 0:
            fin = m
        elif f(m)*f(fin) < 0:
            deb = m
        else:
            deb = fin = m
    LHD.append(m)

LHD_exp=[
    526.6-rp*18.35*np.pi/180,
    555.84-rp*25.8*np.pi/180,
    591.39-rp*32.44*np.pi/180,
    634.83-rp*38.25*np.pi/180,
    683.84-rp*43.26*np.pi/180,
    737.3-rp*47.58*np.pi/180,
    794.31-rp*51.29*np.pi/180,
    854.15-rp*54.49*np.pi/180,
    916.25-rp*57.26*np.pi/180
    ]

y_exp=[600,525,450,375,300,225,150,75,0]
plt.plot(y_tab, LHD)
plt.plot(y_exp,LHD_exp)
plt.show()
