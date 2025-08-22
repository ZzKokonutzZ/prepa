import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint
# x=np.linspace(-5,10)
# def f(x) :
#     return np.exp(-x**2)

# F=[1]

# for i in range(len(x)-1) :
#     F.append(F[i]+f(x[i])/(len(x)-1)*15)
    
# plt.plot(x,F)
# plt.show()

# t=np.linspace(0,5,100)

# v=[5]


# for i in range(len(t)-1) :
#     v.append(v[i]+ (-abs(v[i])*v[i]-10) *5/(len(t)-1))
    
# plt.plot(t,v)
# plt.show()

# omega=1

# t=np.linspace(0,5*2*np.pi/omega,500)

# u=[0]

# for i in range(len(t)-1) :
#     u.append(u[i]+ (np.cos(omega*t[i])-u[i])*(5*2*np.pi/omega)/(len(t)-1))

# plt.plot(t,u)
# plt.plot(t,(np.cos(omega*t-np.arctan(omega))-np.exp(-t)/np.sqrt(1+omega**2))/np.sqrt(1+omega**2))
# plt.show()

# t=np.linspace(0,10,4000)
# omega_0=5
# epsilon=2
# x=[0.5]
# v=[0]

# for i in range(len(t)-1) :
#     dv=epsilon*omega_0*(1-x[i]**2)*v[i]-omega_0**2*x[i]
#     dx=v[i]
#     x.append(x[i]+dx*10/(len(t)-1))
#     v.append(v[i]+dv*10/(len(t)-1))

# plt.plot(t,x)
# plt.plot(t,v)
# fig=plt.figure()
# plt.plot(x,v)
# plt.show()

# def eq(y,t) :
#     theta=y[0]
#     omega=y[1]
#     dtheta=omega
#     domega=-0.01*abs(omega)*omega-np.sin(theta)
#     return [dtheta, domega]

# t=np.linspace(0,100,1000)

# values=odeint(eq,[3,0],t)
# theta=[values[i][0] for i in range(len(values))]
# omega=[values[i][1] for i in range(len(values))]
# plt.plot(t,theta)
# plt.plot(t,omega)
# figure=plt.figure()
# plt.plot(theta,omega)
# plt.show()

# x=np.linspace(-1,4,100)

# y=[0]
# dy=0

# dt=5/(len(x)-1)

# y.append(y[0]+dy*5/(len(x)-1)+0.5*(np.sin(x[0])+y[0]-y[0]**3)*dt**2)

# for i in range(1,len(x)-1) :
#     y.append(2*y[i]-y[i-1]+(dt**2*(y[i]-y[i]**3+np.sin(x[i]))))

# plt.plot(x,y)
# plt.show()

t=np.linspace(0,13,1000)

y=[-1]
dy=[2]
dt=13/(len(t)-1)
for i in range(len(t)-1) :
    y.append(y[i]+dy[i]*dt)
    dy.append(dy[i]+(dy[i]+6*y[i])*dt)

plt.plot(t,y)
plt.plot(t,-np.exp(-2*t))
plt.show()