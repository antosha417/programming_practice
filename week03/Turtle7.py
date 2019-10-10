import turtle
from math import sin, pi

def draw_spiral(step,Nst,inc):
    angle=180-360/Nst
    for i in range(Nst):
        turtle.forward(step)
        turtle.left(180-angle)
        step+=inc


nspirals=10
r=1
Nsteps=36
inc=0.05
step=2*r*sin(360/Nsteps*pi/180)
turtle.left(90)
for i in range(nspirals):
    draw_spiral(step,Nsteps,inc)
    step+=inc*Nsteps