import turtle
from math import sin, pi

#def getR(st,Nst):
 #   R=st/2/sin(360/Nst*pi/180)
  #  return R

def draw_spiral(R):
    Nsteps=36
    angle=180-360/Nsteps
    step=2*R*sin(360/Nsteps*pi/180)
    for i in range(Nsteps):
        turtle.forward(step)
        turtle.left(180-angle)
        step+=0.5


nspirals=4
r=10
for i in range(nspirals):
    draw_spiral(r)