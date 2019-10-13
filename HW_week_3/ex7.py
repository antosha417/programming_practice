from turtle import *

shape('turtle')
n = 50
speed(0)
angle = 180 * (n - 2) / n
l = 1
for i in range(10 * n):
    forward(l)
    left(180 - angle)
    if i % 10 == 0:
        l += 1
mainloop()