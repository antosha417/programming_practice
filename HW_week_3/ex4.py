from turtle import *

shape('turtle')
n = 1000
speed(0)
angle = 180 * (n - 2) / n
for _ in range(n):
    forward(1)
    left(180 - angle)

mainloop()