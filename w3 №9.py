import turtle
turtle.shape('turtle')
from math import sin, pi

def ppp(n):
    r = 50 * (n - 2)
    turtle.up()
    turtle.goto(r, 0)
    turtle.down()
    k = 360 / n
    t = pi / n
    f = 180 - 90 * (n - 2) / n
    a = 2 * r * sin(t)
    turtle.left(f)
    for i in range(n):
        turtle.forward(a)
        turtle.left(k)
    turtle.right(f)

for l in range (3, 10):
    ppp(l)

