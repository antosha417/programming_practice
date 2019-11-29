def step(len,angle):
    turtle.forward(len)
    turtle.left(angle)

import turtle
turtle.shape('classic')
n=10
a=10
inc=10
for i in range(n):
    for j in range(2):
        step(a,90)
        a=a+inc
        step(a,90)
