import numpy as np
import matplotlib.pyplot as plt
a_etalonnage=2.114374434249408e-05
b_etalonnage=-5.607133674736671
nb_mes=5
Ne=75
tab_t=[]
tab_mes=[]
tab_cmd=[]
mes_moyenne=[]
t=[]

for i in range(nb_mes) :
    data=np.loadtxt(f"RepInd_1300_1500_{i}.txt")
    tab_t.append([(data[:,0]-data[0][0])[j] for j in range(Ne)])
    tab_cmd.append([(data[:,1])[j] for j in range(Ne)])
    tab_mes.append([-(data[:,2]*a_etalonnage+b_etalonnage)[j] for j in range(Ne)])

for j in range(Ne) :
    t_i=0
    mes_i=0
    n=0
    for i in range(nb_mes) :
        if abs(tab_mes[i][j])<20 :
            n+=1
            mes_i+=tab_mes[i][j]
            t_i+=tab_t[i][j]
    if n :
        mes_moyenne.append(mes_i/n)
        t.append(t_i/n)
mes_moyenne.pop(0)
t.pop(0)


rep_1300=np.mean([mes_moyenne[i] for i in range(21)])
rep_1500=np.mean([mes_moyenne[i] for i in range(-21,-1)])

tab_t=[]
tab_mes=[]
tab_cmd=[]
mes_moyenne=[]
t=[]

for i in range(nb_mes) :
    data=np.loadtxt(f"RepInd_1300_1400_{i}.txt")
    tab_t.append([(data[:,0]-data[0][0])[j] for j in range(Ne)])
    tab_cmd.append([(data[:,1])[j] for j in range(Ne)])
    tab_mes.append([-(data[:,2]*a_etalonnage+b_etalonnage)[j] for j in range(Ne)])

for j in range(Ne) :
    t_i=0
    mes_i=0
    n=0
    for i in range(nb_mes) :
        if abs(tab_mes[i][j])<20 :
            n+=1
            mes_i+=tab_mes[i][j]
            t_i+=tab_t[i][j]
    if n :
        mes_moyenne.append(mes_i/n)
        t.append(t_i/n)
mes_moyenne.pop(0)
t.pop(0)
plt.plot(t,mes_moyenne,'+r')

rep_1400=np.mean([mes_moyenne[i] for i in range(-21,-1)])

a,b,c=np.polyfit([1300,1400,1500],[rep_1300,rep_1400,rep_1500],2)

print(a)
print(b)
print(c)