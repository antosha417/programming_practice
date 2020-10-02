import turtle
from math import sin,pi, sqrt

def draw_circle(R,k):
    Nsteps=36
    angle=180-360/Nsteps
    a=2*R*sin(360/Nsteps*pi/180)
    for i in range(int(Nsteps/k)):
        turtle.left(180-angle)
        turtle.forward(a)
    turtle.right(180-angle)

def draw_in_position(color1,color2,x,y,r,k):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.color(color1, color2)
    turtle.begin_fill()
    draw_circle(r,k)
    turtle.end_fill()

R=50

draw_in_position('black','yellow',0,0,R,1)
r=10
draw_in_position('black','blue',-R,2.5*R,r,1)
draw_in_position('black','blue',R/2,2.5*R,r,1)

turtle.penup()
turtle.goto(-r,2*R)
turtle.pendown()
turtle.color('black')
turtle.width(10)
turtle.goto(-r,R)

r=20
turtle.right(65)
turtle.penup()
turtle.goto(-2.5*r, R)
turtle.pendown()
turtle.width(10)
turtle.color('red')
draw_circle(r,2)