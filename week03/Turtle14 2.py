import turtle

from math import pi,sin

def draw_circle(R,Nsteps):
    mas_pos=[[0]*2 for i in range(Nsteps)]
    angle = 180 - 360 / Nsteps
    a = 2 * R * sin(pi / Nsteps)
    turtle.penup()
    for i in range(Nsteps):
        mas_pos[i]=turtle.pos()
        turtle.forward(a)
        turtle.left(180 - angle)
    turtle.pendown()
    return mas_pos

def draw_star(R,Nsteps):
    arr_pos=draw_circle(R,Nsteps)
    k=0
    num_inc=Nsteps//2
    for i in range(Nsteps+1):
        turtle.goto(arr_pos[k])
        k=(k+num_inc)%Nsteps
r=100
n=5
draw_star(r,n)
turtle.penup()
turtle.forward(4*r)
turtle.pendown()
r=150
n=11
draw_star(r,n)
