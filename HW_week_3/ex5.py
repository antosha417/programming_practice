from turtle import *

shape('turtle')
speed(0)
x = y = 0
l = 5
delta = 2
for _ in range(10):
    for _ in range(4):
        forward(l)
        left(90)
    l += (delta * 2)
    x -= delta
    y -= delta
    goto(x, y)

mainloop()