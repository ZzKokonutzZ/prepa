import numpy.random as rd
import numpy as np
ceau=4.18
M=101.1

def deltaH0(t0,t1,t2,t3,T0,T1,T2,T3,ms,me,mc) :
    phith=-ceau/2*((me+mc)*(T1-T0)/(t1-t0)+(me+mc+ms)*(T3-T2)/(t3-t2))
    n=ms/M
    return (t2-t1)/n*(-phith-(me+mc+ms)*ceau*(T2-T1)/(t2-t1))
N=10000000
T0=52.5
ms=15.36
me=99
mc=26.56
t0=57
t1=11*60+50
t2=12*60+58
t3=21*60+50
T1=47.5
T2=37.25
T3=35.6



deltaT=1
deltams=0.2
deltame=1
deltat=0.5
u_mc=0.6
tabT0=T0+rd.uniform(-deltaT,deltaT,N)
tabT1=T1+rd.uniform(-deltaT,deltaT,N)
tabT2=T2+rd.uniform(-deltaT,deltaT,N)
tabT3=T3+rd.uniform(-deltaT,deltaT,N)

tabms=ms+rd.uniform(-deltams,deltams,N)
tabme=me+rd.uniform(-deltame,deltame,N)
tabmc=mc+rd.normal(0,u_mc,N)

tabt0=t0+rd.uniform(-deltat,deltat,N)
tabt1=t1+rd.uniform(-deltat,deltat,N)
tabt2=t2+rd.uniform(-deltat,deltat,N)
tabt3=t3+rd.uniform(-deltat,deltat,N)

tab_deltarH0=deltaH0(tabt0,tabt1,tabt2,tabt3,tabT0,tabT1,tabT2,tabT3,tabms,tabme,tabmc)
deltarH0=np.mean(tab_deltarH0)
u_deltarH0=np.std(tab_deltarH0,ddof=1)
print(f"deltarH0 = {deltarH0} +/- {u_deltarH0} Jmol^-1")
print(f"Z-score={abs(deltarH0-34900)/u_deltarH0}")