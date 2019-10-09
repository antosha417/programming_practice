import turtle
from math import sin,pi

def draw_2circles(R):
    n=36
    angle=360/n
    a=2*R*sin(angle/2*pi/180)
    for i in range(n):
        turtle.forward(a)
        turtle.left(angle)
    for i in range(n):
        turtle.forward(a)
        turtle.right(angle)
N=4
r=20
dr=10
turtle.left(90)
for i in range(N):
    draw_2circles(r)
    r+=dr