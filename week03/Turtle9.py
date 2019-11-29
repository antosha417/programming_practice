import turtle
from math import sin,pi

inc=10

def draw(n,R):
    angle=180-360/n
    turtle.left(180-angle/2)
    a=2*R*sin(360/n/2*pi/180)
    for i in range(n):
        turtle.forward(a)
        turtle.left(180-angle)
    turtle.right(180-angle/2)
    turtle.penup()
    turtle.forward(inc)
    turtle.pendown()

turtle.shape('arrow')
r=5
for i in range(3,14):
    draw(i,r)
    r=r+inc
