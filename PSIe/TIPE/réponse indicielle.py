from numpy import loadtxt
import matplotlib.pyplot as plt
for i in range(5) :
    data=loadtxt(f"RepInd_1300_1400_{i}.txt")
    t=data[:,0]-data[0][0]
    cmd=data[:,1]*100
    mes=data[:,2]
    tab_t=[]
    tab_cmd=[]
    tab_mes=[]
    for j in range(len(mes)) :
        if abs(mes[j])<2.5e5 :
            tab_t.append(t[j])
            tab_mes.append(mes[j])
    plt.plot(tab_t,tab_mes,'+')
    plt.plot(t,cmd,'+')

for i in range(5) :
    data=loadtxt(f"RepInd_1300_1500_{i}.txt")
    t=data[:,0]-data[0][0]
    cmd=data[:,1]*100
    mes=data[:,2]
    tab_t=[]
    tab_cmd=[]
    tab_mes=[]
    for j in range(len(mes)) :
        if abs(mes[j])<2.5e5 and mes[j]!=-1:
            tab_t.append(t[j])
            tab_mes.append(mes[j])
    plt.plot(tab_t,tab_mes,'+')
    plt.plot(t,cmd,'+')
    
for i in range(5) :
    data=loadtxt(f"RepInd_1300_1700_{i}.txt")
    t=data[:,0]-data[0][0]
    cmd=data[:,1]*100
    mes=data[:,2]
    tab_t=[]
    tab_cmd=[]
    tab_mes=[]
    for j in range(len(mes)) :
        if abs(mes[j])<2.5e5 and mes[j]!=-1:
            tab_t.append(t[j])
            tab_mes.append(mes[j])
    plt.plot(tab_t,tab_mes,'+')
    plt.plot(t,cmd,'+')
    
plt.xlim(1750,4500)
# plt.ylim(-10000,0.25e6)

plt.show()