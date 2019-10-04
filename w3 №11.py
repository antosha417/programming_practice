import turtle
turtle.shape('turtle')
from math import sin, pi

n=10
k=30
turtle.left(90)
for i in range(n):
    turtle.circle(k)
    turtle.circle(-k)
    k+=5
