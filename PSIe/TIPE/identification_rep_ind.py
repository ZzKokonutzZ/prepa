import numpy as np
import matplotlib.pyplot as plt

a_etalonnage=2.114374434249408e-05
b_etalonnage=-5.607133674736671
nb_mes=5
Ne=75
for i in range(nb_mes) :
    data=np.loadtxt(f"RepInd_1300_1500_{i}.txt")
    t=data[:,0]-data[0][0]
    cmd=data[:,1]*0.001
    mes=-(data[:,2]*a_etalonnage+b_etalonnage)
    tab_t=[]
    tab_cmd=[]
    tab_mes=[]
    for j in range(4,Ne) :
        if abs(mes[j])<20 :
            tab_t.append(t[j])
            tab_mes.append(mes[j])
    plt.plot(tab_t,tab_mes,'+')
    plt.plot(t,cmd,'+')
plt.figure()
tab_t=[]
tab_mes=[]
tab_cmd=[]
mes_moyenne=[]
t=[]

for i in range(nb_mes) :
    data=np.loadtxt(f"RepInd_1300_1500_{i}.txt")
    tab_t.append([(data[:,0]-data[0][0])[j] for j in range(Ne)])
    tab_cmd.append([(data[:,1])[j] for j in range(Ne)])
    tab_mes.append([(-data[:,2]*a_etalonnage-b_etalonnage)[j] for j in range(Ne)])

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
t=np.array(t)
rep_0=np.mean(mes_moyenne[:20])
rep_f=np.mean([mes_moyenne[i] for i in range(len(mes_moyenne)) if t[i]>=4500])
cmd_0=tab_cmd[0][0]
cmd_f=tab_cmd[0][-1]
u_rep=rep_f-rep_0
rep_max=max(mes_moyenne)
D_rel=(rep_max-rep_f)/u_rep
z=np.sqrt(np.log10(D_rel)**2/(1+np.log10(D_rel)**2))
T=2*(t[26]-t[20])
w=2*np.pi/T
w0=w/np.sqrt(1-z**2)

print(z)
print(w0)

def K(cmd) :
    return 1.2888193024824312e-05*cmd**2-0.0236179376313443*cmd+9.46878125952518
u=cmd_f-cmd_0
plt.plot(t[20:],K(cmd_0)+(K(cmd_f)-K(cmd_0))*(1-np.e**(-w0*z*(t[20:]-t[20]))/np.sqrt(1-z**2)*np.sin(w0*np.sqrt(1-z**2)*(t[20:]-t[20])+np.arctan(np.sqrt(1-z**2)/z))))

plt.show()
