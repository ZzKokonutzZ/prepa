from numpy import loadtxt,mean
from scipy.stats import linregress
nb_mesures=1
tab_a=[]
tab_b=[]
tab_r=[]
for i in range(nb_mesures) :
    data=loadtxt(f'etalonnage{i}.txt')
    a,b,r,trash,trash1=linregress(data[1:],[0.1*9.81*k for k in range(1,11)])
    tab_a.append(a)
    tab_b.append(b)
    tab_r.append(r)
print(f'F = {mean(tab_a)}*mesure + {b}')
print(f'r^2 = {mean(tab_r)**2}')
    