import turtle
from math import sin,pi

def draw_2circles(R):
    Nsteps=36
    angle=180-360/Nsteps
    a=2*R*sin(pi/Nsteps)
    for i in range(Nsteps):
        turtle.forward(a)
        turtle.left(180-angle)
    for i in range(Nsteps):
        turtle.forward(a)
        turtle.right(180-angle)

r=30
nspirals=3
angle=180/nspirals
for i in range(nspirals):
    draw_2circles(r)
    turtle.left(angle)
