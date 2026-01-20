import pygame as pg
import numpy as np
pg.init()
clock=pg.Clock()
screen=pg.display.set_mode((800,500))
screen.fill((0,0,0))
check=False
J=1000
l=600
t_0=1
dt=1/60
theta=1
dtheta=0
d2theta=0
F=0
a=5*J/(l*t_0)
k=l*a**2/(4*J)

while not check :
    screen.fill((0,0,0))
    F=-a*dtheta-k*theta
    d2theta=l*F/J
    dtheta+=d2theta*dt
    theta+=dtheta*dt
    pg.draw.aaline(screen,(0,100,200),(0,250),(np.cos(theta)*600,250-np.sin(theta)*600))
    pg.display.flip()
    clock.tick(60)
    for event in pg.event.get() :
        if event.type == pg.QUIT :
            check=True
        if event.type==pg.MOUSEBUTTONDOWN :
            x,y=pg.mouse.get_pos()
            y=250-y
            theta=np.arctan(y/x)