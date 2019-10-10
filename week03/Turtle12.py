import turtle
from math import sin, pi

def draw_arch(R):
    Nsteps=36
    angle=180-360/Nsteps
    a=2*R*sin(360/Nsteps*pi/180)
    for i in range(int(Nsteps/2)-1):
        turtle.right(180-angle)
        turtle.forward(a)
    turtle.right(180-angle)

nspirals=7
r1=30
r2=5
turtle.left(90)
for i in range(nspirals):
    draw_arch(r1)
    draw_arch(r2)
