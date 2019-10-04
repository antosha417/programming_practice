n = 10
r = 10
import turtle as t
import math
for i in range(0, n):
    for j in range (0, 4):
        t.forward((2*i+1)*r)
        t.left(90)
    t.penup()
    t.right(135)
    t.forward(r*math.sqrt(2))
    t.left(135)
    t.pendown()
