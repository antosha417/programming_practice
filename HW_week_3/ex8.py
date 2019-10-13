from turtle import *

shape('turtle')
n = 50
speed(0)
l = 1
for i in range(n):
    forward(l)
    left(90)
    l += 4
mainloop()