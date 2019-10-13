from turtle import *
n = int(input())
angle = 360 / n
shape('turtle')
speed(0)
for _ in range(n):
    forward(90)
    stamp()
    right(180)
    forward(90)
    left(180 - angle)
mainloop()